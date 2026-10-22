# Shared Curation Queue

State and logs live outside this public checkout. Both schedules must use the **same absolute state path**, supplied in their automation prompts; never commit the queue. The standard-library helper uses POSIX `flock`, an atomic JSON replacement, and a persistent guard process. Initialize once during setup, not on each run:

```bash
python3 scripts/curation_queue.py --state "$QUEUE_STATE" init
```

## Hold the lock across the complete run

Use a fresh run ID (UTC timestamp plus UUID). Start this command with an interactive terminal session (`tty: true`, short initial yield) and keep its returned session ID alive:

```bash
python3 scripts/curation_queue.py --state "$QUEUE_STATE" --run-id "$RUN_ID" guard --lane new
```

Use `maintenance` for biweekly. Wait for `LOCKED` before any queue or catalog mutation. The guard holds the lock through all subsequent tool calls, source review, validation, commit and push. Do not wait for it to finish before doing the work. Other commands below run in separate short tool calls with the same state path and run ID. A competing guard fails immediately: report read-only counts and exit without editing. A dead guard cannot authorize mutations; a later guard marks the interrupted run and preserves unresolved candidates.

After all work, send `success` followed by newline to the guard session; on any failure send `failed` followed by newline. EOF and termination also fail the run. It persists final counts, releases the lock, and prints the Japanese report. On setup errors or to obtain a fresh snapshot:

```bash
python3 scripts/curation_queue.py --state "$QUEUE_STATE" --run-id "$RUN_ID" report
```

`report --json` returns machine-readable counts. A missing, malformed or unreadable queue returns a nonzero exit code and unknown counts; never initialize it over an error. Read-only reports are allowed during another run. No idle lease timeout permits concurrent writers. If a tool session is lost while the guard is still live, explicitly terminate that guard session before recovery; do not delete its lock file.

## Ingest metadata deltas transactionally

Prepare an external JSON batch with `candidates` and optional `checkpoints`:

```json
{
  "candidates": [{"id":"arxiv:2610.12345","paper_url":"https://arxiv.org/abs/2610.12345","title":"Example robot reliability study","source_version":"v1","reason":"direct physical-agent robustness"}],
  "checkpoints": [{"source":"robotics-listing","cursor":"successful-listing-fingerprint","success":true}]
}
```

```bash
python3 scripts/curation_queue.py --state "$QUEUE_STATE" --run-id "$RUN_ID" ingest --batch "$BATCH" --catalog data/papers.json
```

The helper deduplicates source identities and normalized titles, reconciles already-cataloged new candidates, and routes known records only when `signal` is one of `revision`, `venue`, `code`, `correction`, `invalid-metadata`. Supply a specific `evidence_key` (source version, official announcement URL plus content fingerprint, or verified restoration signal) to distinguish genuinely new evidence. An identical held/terminal item is not reactivated. Successful source cursors are saved only with the enqueued batch; unsuccessful source cursors remain unchanged. Caller must set `success: true` only after retrieval and parsing both succeed. Keep listing fingerprints per source so unchanged feeds need no repeated model screening.

## Reserve before reading; resolve after decisions

```bash
python3 scripts/curation_queue.py --state "$QUEUE_STATE" --run-id "$RUN_ID" claim
```

Returns the next FIFO pending entry, or JSON null when empty or the 20-record budget is exhausted. `claim --id <canonical-id>` selects one eligible entry. Every claim counts even if review later holds/rejects it. Do not open primary paper bodies without a claim. Holds are not automatically retried. Whole-document source downloads may be cached, but only necessary sections should enter model context.

```bash
python3 scripts/curation_queue.py --state "$QUEUE_STATE" --run-id "$RUN_ID" resolve --id <canonical-id> --outcome held --reason "primary source unavailable"
```

Outcomes: `held`, `rejected`, `unchanged`, `added` (new lane only), `updated` (maintenance only). Publication candidates stay pending until all publication gates and push succeed, then resolve added/updated. An uncommitted or failed change is not done. Terminal entries remain for deduplication, but do not count toward remaining work. Unresolved claims stay pending after interruption. Run counters are separate from remaining counts; the final report includes both lanes even if only one was processed. Archive that exact snapshot at every exit, including no-change and failed runs.

The version-1 state contains entries, per-source successful cursors, an active run ID and the latest 50 run summaries. There are no host-specific default paths in the helper. State initialization/migration must preserve known ID-based unresolved work; do not populate the queue merely from absent venue/code metadata.
