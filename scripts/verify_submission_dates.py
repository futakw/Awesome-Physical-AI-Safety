#!/usr/bin/env python3
"""Verify populated initial submission dates; does not replace bibliography checks."""
import concurrent.futures
import json
from verify_bibliography import DATA_PATH, source_metadata


def check(record):
    url = record['first_submission_source']
    try:
        actual = source_metadata(url).first_submission_date
        if actual != record['first_submission_date']:
            return f"{record['id']}: catalog={record['first_submission_date']}, source={actual}, URL={url}"
    except Exception as exc:
        return f"{record['id']}: {url}: {exc}"
    return None


def main():
    records = json.loads(DATA_PATH.read_text())
    dated = [r for r in records if r.get('first_submission_date')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        errors = [error for error in pool.map(check, dated) if error]
    for error in errors:
        print(error)
    print(f"Submission dates: {len(dated)-len(errors)} verified, {len(errors)} failed, {len(records)-len(dated)} unknown")
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
