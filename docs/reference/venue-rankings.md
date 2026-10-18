# Venue rankings

The catalog exposes an explicit venue-ranking table at [`data/venue_ranks.json`](../../data/venue_ranks.json). It is a lookup layer for filtering and display; ranks are not copied into every paper record.

## Source and scope

- The primary source is the official [ICORE conference portal](https://portal.core.edu.au/conf-ranks/), using the `ICORE2026` edition.
- ICORE is conference-focused. Journals and preprints are marked `not-covered`, not assigned an inferred conference rank.
- `core_rank_raw` preserves the source label. `core_rank_band` is the normalized filter value (`A*`, `A`, `B`, `C`, `regional`, `other`, or `unranked`).
- `Unranked` is a source result, not a quality judgment. `not-covered` means the source does not rank that publication class.
- Workshops, tracks, companion proceedings, and year-qualified variants remain separate rows in the source table. The Explorer may nest them under a parent venue (for example `A* → NeurIPS → NeurIPS Workshop`) as a browsing shortcut, but their raw `core_rank_raw`/`core_rank_band` values are not rewritten or silently treated as independently ranked.
- Parent-only conference rows are included when the catalog contains only a workshop or companion variant (for example ACL, CCS, and RSS). ACL and CCS are ICORE2026 A*; RSS is currently TBR and therefore remains in the unranked/other group, despite its A* rank in older CORE editions.

Each row also records `canonical_name`, `aliases`, `venue_type`, `ranking_edition`, `ranking_status`, `source_url`, and `checked_date`. The validator requires one row for every venue string currently used by `data/papers.json`.

## Current ranked venues in this catalog

| Catalog venue | ICORE2026 | Status |
| --- | --- | --- |
| AAAI | A* | ranked |
| CVPR | A* | ranked |
| ECCV | A* | ranked |
| EMNLP | A* | ranked |
| HRI | A* | ranked |
| ICCV | A* | ranked |
| ICLR | A* | ranked |
| ICRA | A* | ranked |
| IROS | A | ranked |
| ISRR | C | ranked |
| ICSE | A* | ranked |
| NeurIPS | A* | ranked |
| CoRL | Unranked | unranked |

The Explorer's `VENUE RANK (ICORE)` filter derives its value from this table and falls back to `unranked` when a paper's venue is not mapped.
