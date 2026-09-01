"""Detect Google Sheets changes for CI sync."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import _bootstrap  # noqa: F401

from counting import constants
from counting.google_sheets_exporter import GoogleSheetsExporter

STATE_PATH = constants.REPO_ROOT / ".github" / "sheets_state.json"


def _hash_worksheet_rows(rows: List[List[str]]) -> str:
    payload = json.dumps(rows, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def load_state() -> Dict[str, Any]:
    if not STATE_PATH.exists():
        return {"spreadsheet_modified_time": "", "countries": {}}
    with open(STATE_PATH, encoding="utf-8") as handle:
        return json.load(handle)


def save_state(state: Dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2, ensure_ascii=False)


def get_country_hashes(exporter: GoogleSheetsExporter) -> Dict[str, str]:
    hashes: Dict[str, str] = {}
    if not exporter.is_available():
        return hashes
    for ws in exporter.spreadsheet.worksheets():
        if ws.title.startswith("_"):
            continue
        hashes[ws.title] = _hash_worksheet_rows(ws.get_all_values())
    return hashes


def get_changed_countries(
    exporter: Optional[GoogleSheetsExporter] = None,
) -> tuple[List[str], Dict[str, Any]]:
    exporter = exporter or GoogleSheetsExporter()
    previous = load_state()
    modified_time = exporter.get_spreadsheet_modified_time()
    current_hashes = get_country_hashes(exporter)

    changed: List[str] = []
    if modified_time != previous.get("spreadsheet_modified_time"):
        changed = list(current_hashes.keys())
    else:
        for country, digest in current_hashes.items():
            if previous.get("countries", {}).get(country) != digest:
                changed.append(country)

    new_state = {
        "spreadsheet_modified_time": modified_time,
        "countries": current_hashes,
    }
    return changed, new_state


def main() -> int:
    exporter = GoogleSheetsExporter()
    if not exporter.is_available():
        print("Google Sheets not available")
        return 1
    changed, state = get_changed_countries(exporter)
    if changed:
        print("CHANGED:" + ",".join(changed))
    else:
        print("UNCHANGED")
    save_state(state)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
