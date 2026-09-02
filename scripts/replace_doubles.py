"""Merge duplicate entities marked replace?=yes on the doubles sheet."""
from __future__ import annotations

import argparse
import sys

import _bootstrap  # noqa: F401

from counting import constants
from counting.doubles import replace_doubles_cli


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Replace id2 with id1 for doubles rows where replace? is yes, "
            "then move those rows to the end of the doubles sheet."
        )
    )
    parser.add_argument(
        "--read-only-sheets",
        action="store_true",
        help="Show which countries would change without writing Sheets",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Use the test Google Spreadsheet (GOOGLE_SHEETS_TEST_SPREADSHEET_ID)",
    )
    args = parser.parse_args()
    spreadsheet_id = (
        constants.GOOGLE_SHEETS_TEST_SPREADSHEET_ID if args.test else None
    )
    if args.test:
        print(f"Using test Google Spreadsheet: {spreadsheet_id}")
    ok = replace_doubles_cli(
        read_only=args.read_only_sheets,
        spreadsheet_id=spreadsheet_id,
        test=args.test,
    )
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
