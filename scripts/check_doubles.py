"""Find cross-country duplicate tournaments, teams and players by external ids."""
from __future__ import annotations

import argparse
import sys

import _bootstrap  # noqa: F401

from counting.doubles import check_doubles_cli


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Find entities that share ts_id, uz_id or ua_id across country tabs "
            "and write them to the doubles sheet."
        )
    )
    parser.add_argument(
        "--read-only-sheets",
        action="store_true",
        help="Print pairs without writing the doubles tab",
    )
    args = parser.parse_args()
    ok = check_doubles_cli(read_only=args.read_only_sheets)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
