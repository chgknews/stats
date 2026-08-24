#!/usr/bin/env python3
"""Generate filter-page data from the chgk_calendar Google Sheet."""

from __future__ import annotations

import argparse
import csv
import html
import io
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

SPREADSHEET_ID = "14jKSV5PGslleGbuKaK7p9nCCBoX5PNnnJy9X8xsT4MM"
SHEET_GID = "0"
SHEET_CSV_URL = (
    f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export"
    f"?format=csv&gid={SHEET_GID}"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
CALENDAR_DIR = REPO_ROOT / "content" / "info" / "calendar"
CALENDAR_JSON_PATH = REPO_ROOT / "data" / "calendar.json"

MONTHS_GENITIVE = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря",
}

EMBEDDED_LINK_RE = re.compile(r"\s*\(https?://[^)]+\)\s*$")
TOKEN_SPLIT_RE = re.compile(r"[,;|]+|\s+")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

AGE_TAGS = frozenset({"youth", "student", "school"})
GAME_TAGS = frozenset({"ssi", "kvrm"})


@dataclass(frozen=True)
class Event:
    date_start: date
    date_end: date
    name: str
    place: str
    link: str
    comment: str
    champs: bool
    geographies: frozenset[str]
    ages: frozenset[str]
    games: frozenset[str]


def parse_date(value: str) -> date | None:
    value = value.strip()
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


def parse_tokens(*values: str) -> list[str]:
    tokens: list[str] = []
    for value in values:
        for part in TOKEN_SPLIT_RE.split(value.strip().lower()):
            if part:
                tokens.append(part)
    return tokens


def is_yes(value: str) -> bool:
    return value.strip().lower() == "yes"


def first_value(columns: dict[str, list[str]], *keys: str) -> str:
    for key in keys:
        for value in columns.get(key, []):
            if value.strip():
                return value.strip()
    return ""


def classify_tags(columns: dict[str, list[str]]) -> tuple[frozenset[str], frozenset[str], frozenset[str]]:
    geographies = set(parse_tokens(*columns.get("geography", [])))
    ages = set(parse_tokens(*columns.get("age", [])))
    games = set(parse_tokens(*columns.get("game", [])))

    # Old sheets kept mixed flags in a single "type" column.
    for token in parse_tokens(*columns.get("type", [])):
        if token in AGE_TAGS:
            ages.add(token)
        elif token in GAME_TAGS:
            games.add(token)
        else:
            geographies.add(token)

    return frozenset(geographies), frozenset(ages), frozenset(games)


def parse_events(rows: list[dict[str, list[str]]]) -> list[Event]:
    events: list[Event] = []

    for row in rows:
        date_start = parse_date(first_value(row, "date_start"))
        date_end = parse_date(first_value(row, "date_end")) or date_start
        name = first_value(row, "name")
        place = first_value(row, "place")
        link = first_value(row, "link")
        comment = first_value(row, "comment")
        champs = is_yes(first_value(row, "champ?", "champs", "champs?"))
        geographies, ages, games = classify_tags(row)

        if not date_start or not name:
            continue

        if date_end < date_start:
            date_end = date_start

        events.append(
            Event(
                date_start=date_start,
                date_end=date_end,
                name=name,
                place=place,
                link=link,
                comment=comment,
                champs=champs,
                geographies=geographies,
                ages=ages,
                games=games,
            )
        )

    return events


def drop_past_events(events: list[Event], today: date) -> list[Event]:
    return [event for event in events if event.date_end >= today]


def sort_events(events: list[Event]) -> list[Event]:
    return sorted(events, key=lambda event: (event.date_start, event.date_end, event.name.casefold()))


def format_event_date(date_start: date, date_end: date, today: date) -> str:
    event_year = max(date_start.year, date_end.year)
    year_suffix = f" {event_year} года" if event_year > today.year else ""

    if date_start == date_end:
        return f"{date_start.day} {MONTHS_GENITIVE[date_start.month]}{year_suffix}"

    if date_start.month == date_end.month and date_start.year == date_end.year:
        month = MONTHS_GENITIVE[date_start.month]
        return f"{date_start.day}–{date_end.day} {month}{year_suffix}"

    start_part = f"{date_start.day} {MONTHS_GENITIVE[date_start.month]}"
    end_part = f"{date_end.day} {MONTHS_GENITIVE[date_end.month]}"
    return f"{start_part}–{end_part}{year_suffix}"


def clean_name(name: str) -> str:
    return EMBEDDED_LINK_RE.sub("", name.strip())


def format_name(name: str, link: str, comment: str) -> str:
    name = clean_name(name)
    if link:
        cell = f"[{name}]({link.strip()})"
    else:
        cell = name
    comment = comment.strip()
    if comment:
        cell += f" ({comment})"
    return cell


def markdown_inline_to_html(text: str) -> str:
    parts: list[str] = []
    last = 0
    for match in MARKDOWN_LINK_RE.finditer(text):
        parts.append(html.escape(text[last : match.start()]))
        parts.append(
            f'<a href="{html.escape(match.group(2), quote=True)}">'
            f"{html.escape(match.group(1))}</a>"
        )
        last = match.end()
    parts.append(html.escape(text[last:]))
    return "".join(parts)


def fetch_sheet_csv(url: str = SHEET_CSV_URL) -> str:
    with urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8-sig")


def load_rows(csv_text: str) -> list[dict[str, list[str]]]:
    reader = csv.reader(io.StringIO(csv_text))
    try:
        raw_header = next(reader)
    except StopIteration:
        return []

    header = [name.strip().lower() for name in raw_header]
    rows: list[dict[str, list[str]]] = []

    for raw_row in reader:
        if not any(cell.strip() for cell in raw_row):
            continue
        columns: dict[str, list[str]] = defaultdict(list)
        for key, value in zip(header, raw_row):
            if key:
                columns[key].append(value.strip())
        rows.append(columns)

    return rows


def collect_events(csv_text: str, today: date | None = None) -> tuple[list[Event], date]:
    today = today or date.today()
    events = sort_events(drop_past_events(parse_events(load_rows(csv_text)), today))
    return events, today


def event_to_dict(event: Event, today: date) -> dict[str, object]:
    return {
        "date": format_event_date(event.date_start, event.date_end, today),
        "date_start": event.date_start.isoformat(),
        "date_end": event.date_end.isoformat(),
        "place": event.place,
        "name": format_name(event.name, event.link, event.comment),
        "place_html": markdown_inline_to_html(event.place),
        "name_html": markdown_inline_to_html(format_name(event.name, event.link, event.comment)),
        "geography": sorted(event.geographies),
        "age": sorted(event.ages),
        "game": sorted(event.games),
        "champ": event.champs,
    }


def events_to_json(events: list[Event], today: date) -> str:
    payload = {
        "generated": today.isoformat(),
        "events": [event_to_dict(event, today) for event in events],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def generate_filter_json(csv_text: str, today: date | None = None) -> str:
    events, today = collect_events(csv_text, today)
    return events_to_json(events, today)


def sheet_csv_url(gid: str) -> str:
    return (
        f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export"
        f"?format=csv&gid={gid}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate calendar filter data from Google Sheets."
    )
    parser.add_argument(
        "--csv",
        type=Path,
        help="Read events from a local CSV file instead of Google Sheets",
    )
    parser.add_argument(
        "--gid",
        default=SHEET_GID,
        help=f"Google Sheet tab gid (default: {SHEET_GID})",
    )
    parser.add_argument(
        "--date",
        type=parse_date,
        help="Override current date (YYYY-MM-DD) for filtering and formatting",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=CALENDAR_JSON_PATH,
        help=f"Write filter data JSON here (default: {CALENDAR_JSON_PATH})",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print generated JSON to stdout instead of writing a file",
    )
    args = parser.parse_args()

    try:
        csv_text = (
            args.csv.read_text(encoding="utf-8-sig")
            if args.csv
            else fetch_sheet_csv(sheet_csv_url(args.gid))
        )
    except (OSError, URLError) as exc:
        print(f"Failed to read sheet data: {exc}", file=sys.stderr)
        return 1

    json_text = generate_filter_json(csv_text, today=args.date)

    if args.stdout:
        sys.stdout.write(json_text)
        return 0

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json_text, encoding="utf-8")
    print(f"Wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
