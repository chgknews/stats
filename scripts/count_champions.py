import argparse
import sys

import _bootstrap  # noqa: F401

from counting import constants
from counting.country_registry import resolve_country_slug
from counting.stats_generator import StatsGenerator


def main():
    parser = argparse.ArgumentParser(description="Process championship statistics")
    parser.add_argument("-f", "--file", help="Input file with tournament IDs")
    parser.add_argument(
        "-n", "--number", type=int,
        help="Number of last championship to process (if some data lost)",
    )
    parser.add_argument(
        "-g", "--game", default=None,
        help="Game type: chgk (default for -f/-at/-et), brain, ssi/ssi_f (sheet-only), hamsa, tr, ek, ksi",
    )
    parser.add_argument(
        "-at", "--add_tournament",
        help="Add tournament from rating.chgk.info by id",
    )
    parser.add_argument(
        "-et", "--empty_tournament",
        help='Add empty tournament, date like «25 февраля 2026 года» or «2026-04-21»',
    )
    parser.add_argument("-cn", "--country_name", help="Country slug in English (e.g. poland, testing)")
    parser.add_argument("-p", "--place", type=str, help="City in prepositional case, e.g. «Варшаве»")
    parser.add_argument(
        "-u", "--update",
        help="Update tournament: ts, results, place, announce, tg, fb, vk, site, recap, letopis, photos, questions",
    )
    parser.add_argument("-ui", "--update_info", help="Value for -u depending on type")
    parser.add_argument(
        "-ug", "--update_from_google_sheets",
        help="Rebuild stats from Google Sheets for country slug",
    )
    parser.add_argument(
        "--read-only-sheets", action="store_true",
        help="Do not write back to Google Sheets (for CI)",
    )
    parser.add_argument(
        "--cross-country-stats", action="store_true",
        help="Print cross-country player participation summary",
    )
    parser.add_argument(
        "--check-doubles", action="store_true",
        help="Scan all country tabs for duplicate ts_id/uz_id/ua_id and write the doubles sheet",
    )
    parser.add_argument(
        "--replace-doubles", action="store_true",
        help="Merge entities marked replace?=yes on the doubles sheet (id2 → id1)",
    )
    parser.add_argument(
        "--test", action="store_true",
        help="Use the test Google Spreadsheet (GOOGLE_SHEETS_TEST_SPREADSHEET_ID)",
    )

    args = parser.parse_args()
    read_only = args.read_only_sheets
    spreadsheet_id = (
        constants.GOOGLE_SHEETS_TEST_SPREADSHEET_ID
        if args.test
        else None
    )
    if args.test:
        print(f"Using test Google Spreadsheet: {spreadsheet_id}")

    if args.cross_country_stats:
        from cross_country_stats import print_cross_country_summary
        print_cross_country_summary()
        return

    if args.check_doubles:
        from counting.doubles import check_doubles_cli
        ok = check_doubles_cli(read_only=read_only, spreadsheet_id=spreadsheet_id)
        sys.exit(0 if ok else 1)

    if args.replace_doubles:
        from counting.doubles import replace_doubles_cli
        ok = replace_doubles_cli(
            read_only=read_only, spreadsheet_id=spreadsheet_id, test=args.test
        )
        sys.exit(0 if ok else 1)

    if args.file:
        slug, tournament_ids = resolve_country_slug(args.file, args.country_name)
        if not tournament_ids:
            print("Error: no tournament ids found in file", file=sys.stderr)
            sys.exit(1)
        generator = StatsGenerator(
            slug,
            read_only_sheets=read_only,
            spreadsheet_id=spreadsheet_id,
            test=args.test,
        )
        generator.generate_stats(
            tournament_ids=tournament_ids,
            number_champ=args.number,
            game=args.game or constants.DEFAULT_GAME,
        )
    elif args.update_from_google_sheets:
        slug = args.update_from_google_sheets
        generator = StatsGenerator(
            slug, read_only_sheets=read_only, spreadsheet_id=spreadsheet_id, test=args.test
        )
        ok = generator.update_from_google_sheets()
        print("Country stats updated successfully" if ok else "Failed to update country stats")
        sys.exit(0 if ok else 1)
    else:
        if not args.country_name:
            print("Error: -cn country slug required", file=sys.stderr)
            sys.exit(1)
        generator = StatsGenerator(
            args.country_name,
            read_only_sheets=read_only,
            spreadsheet_id=spreadsheet_id,
            test=args.test,
        )
        if args.add_tournament:
            ok = generator.add_tournament(
                args.add_tournament, args.game or constants.DEFAULT_GAME
            )
            print("Tournament added successfully" if ok else "Failed to add tournament")
        elif args.empty_tournament:
            ok = generator.add_empty_tournament(
                args.empty_tournament,
                args.country_name,
                args.place,
                args.game or constants.DEFAULT_GAME,
            )
            print("Empty tournament added successfully" if ok else "Failed to add empty tournament")
        elif args.update:
            ok = generator.update_tournament(
                args.update, args.update_info, game=args.game
            )
            print("Tournament updated successfully" if ok else "Failed to update tournament")
        else:
            parser.print_help()
            sys.exit(1)


if __name__ == "__main__":
    main()
