#!/usr/bin/env python3
"""Generate calendar markdown files from the chgk_calendar Google Sheet."""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Callable
from urllib.error import URLError
from urllib.request import urlopen

SPREADSHEET_ID = "14jKSV5PGslleGbuKaK7p9nCCBoX5PNnnJy9X8xsT4MM"
SHEET_GID = "0"
SHEET_CSV_URL = (
    f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export"
    f"?format=csv&gid={SHEET_GID}"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
CALENDAR_DIR = REPO_ROOT / "content" / "tournaments" / "calendar"
INDEX_WINDOW_DAYS = 45

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


@dataclass(frozen=True)
class Event:
    date_start: date
    date_end: date
    name: str
    place: str
    link: str
    comment: str
    champs: bool
    types: frozenset[str]


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


def parse_types(value: str) -> frozenset[str]:
    parts = re.split(r"[,;|]+|\s+", value.strip().lower())
    return frozenset(part for part in parts if part)


def is_yes(value: str) -> bool:
    return value.strip().lower() == "yes"


def parse_events(rows: list[dict[str, str]]) -> list[Event]:
    events: list[Event] = []

    for row in rows:
        date_start = parse_date(row.get("date_start", ""))
        date_end = parse_date(row.get("date_end", "")) or date_start
        name = (row.get("name") or "").strip()
        place = (row.get("place") or "").strip()
        link = (row.get("link") or "").strip()
        comment = (row.get("comment") or "").strip()
        champs = is_yes(row.get("champ?", "") or row.get("champs", ""))
        types = parse_types(row.get("type", ""))

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
                types=types,
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


def event_to_table_row(event: Event, today: date) -> str:
    return (
        "| "
        + " | ".join(
            [
                format_event_date(event.date_start, event.date_end, today),
                format_name(event.name, event.link, event.comment),
                event.place,
            ]
        )
        + " |"
    )


def read_header(markdown_path: Path) -> str:
    text = markdown_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    for index, line in enumerate(lines):
        if line.startswith("| ----"):
            return "".join(lines[: index + 1]).rstrip("\n") + "\n"

    raise ValueError(f"Could not find table header in {markdown_path}")


def build_markdown(header: str, events: list[Event], today: date) -> str:
    body = "\n".join(event_to_table_row(event, today) for event in events)
    if body:
        body += "\n"
    return header + body


def fetch_sheet_csv(url: str = SHEET_CSV_URL) -> str:
    with urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8-sig")


def load_rows(csv_text: str) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(csv_text))
    return [dict(row) for row in reader]


def has_type(event: Event, type_name: str) -> bool:
    return type_name in event.types


def within_index_window(event: Event, today: date) -> bool:
    return event.date_start <= today + timedelta(days=INDEX_WINDOW_DAYS)


OUTPUTS: list[tuple[str, Callable[[Event, date], bool]]] = [
    ("_index.md", within_index_window),
    ("champs.md", lambda event, today: event.champs),
    ("russia_belarus.md", lambda event, today: has_type(event, "russia_belarus")),
    ("europe.md", lambda event, today: has_type(event, "europe")),
    ("asia.md", lambda event, today: has_type(event, "asia")),
    ("ukraine.md", lambda event, today: has_type(event, "ukraine")),
    ("caucasus.md", lambda event, today: has_type(event, "caucasus")),
    ("america.md", lambda event, today: has_type(event, "america")),
    ("synch.md", lambda event, today: has_type(event, "synch")),
    ("youth.md", lambda event, today: has_type(event, "youth")),
    ("school.md", lambda event, today: has_type(event, "school")),
    ("all.md", lambda event, today: True),
]


def generate_all(
    calendar_dir: Path,
    csv_text: str,
    today: date | None = None,
) -> dict[str, str]:
    today = today or date.today()
    events = sort_events(drop_past_events(parse_events(load_rows(csv_text)), today))

    result: dict[str, str] = {}
    for filename, predicate in OUTPUTS:
        markdown_path = calendar_dir / filename
        header = read_header(markdown_path)
        filtered = [event for event in events if predicate(event, today)]
        result[filename] = build_markdown(header, filtered, today)

    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate calendar markdown files from Google Sheets."
    )
    parser.add_argument(
        "--calendar-dir",
        type=Path,
        default=CALENDAR_DIR,
        help=f"Directory with calendar markdown files (default: {CALENDAR_DIR})",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        help="Read events from a local CSV file instead of Google Sheets",
    )
    parser.add_argument(
        "--date",
        type=parse_date,
        help="Override current date (YYYY-MM-DD) for filtering and formatting",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print generated markdown to stdout instead of writing files",
    )
    args = parser.parse_args()

    calendar_dir = args.calendar_dir
    if not calendar_dir.is_dir():
        print(f"Calendar directory not found: {calendar_dir}", file=sys.stderr)
        return 1

    missing = [name for name, _ in OUTPUTS if not (calendar_dir / name).exists()]
    if missing:
        print(f"Missing markdown files in {calendar_dir}: {', '.join(missing)}", file=sys.stderr)
        return 1

    try:
        csv_text = (
            args.csv.read_text(encoding="utf-8-sig")
            if args.csv
            else fetch_sheet_csv()
        )
    except (OSError, URLError) as exc:
        print(f"Failed to read sheet data: {exc}", file=sys.stderr)
        return 1

    generated = generate_all(calendar_dir, csv_text, today=args.date)

    if args.stdout:
        for filename in generated:
            sys.stdout.write(f"===== {filename} =====\n")
            sys.stdout.write(generated[filename])
            if not generated[filename].endswith("\n"):
                sys.stdout.write("\n")
        return 0

    for filename, markdown in generated.items():
        output_path = calendar_dir / filename
        output_path.write_text(markdown, encoding="utf-8")
        print(f"Wrote {output_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
