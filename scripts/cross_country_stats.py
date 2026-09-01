"""Cross-country player statistics from merged roster data."""
from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Tuple

import _bootstrap  # noqa: F401

from counting import constants
from counting.external_ids import get_external_id
from counting.google_sheets_exporter import GoogleSheetsExporter


def collect_cross_country_rosters() -> List[dict]:
    exporter = GoogleSheetsExporter()
    if not exporter.is_available():
        return []
    rows: List[dict] = []
    for country in exporter.list_country_worksheets():
        data = exporter.load_data(country)
        if not data:
            continue
        for game_list in data["tournaments"].values():
            for tournament in game_list:
                for awardee in tournament.awardees.values():
                    for player in awardee.team.players:
                        ts_id = get_external_id(player.external_ids, constants.EXTERNAL_ID_TS)
                        rows.append({
                            "country": country,
                            "year": tournament.year,
                            "game": tournament.game,
                            "place": awardee.place,
                            "player_id": player.id,
                            "ts_id": ts_id,
                            "player_name": f"{player.name} {player.surname}".strip(),
                        })
    return rows


def summarize_by_player_year(rows: List[dict]) -> Dict[Tuple[str, int], List[str]]:
    """Map (identity, year) -> list of countries played.

    Prefer rating.chgk.info ``ts_id`` for cross-country identity; fall back to
    internal id only when no external id is present.
    """
    index: Dict[Tuple[str, int], set] = defaultdict(set)
    for row in rows:
        identity = f"ts:{row['ts_id']}" if row.get("ts_id") else f"id:{row['player_id']}"
        index[(identity, row["year"])].add(row["country"])
    return {key: sorted(countries) for key, countries in index.items() if len(countries) > 1}


def print_cross_country_summary() -> None:
    rows = collect_cross_country_rosters()
    multi = summarize_by_player_year(rows)
    if not multi:
        print("No cross-country player participation found.")
        return
    print("Players in multiple countries' championships (same year):")
    for (identity, year), countries in sorted(multi.items()):
        name = next(
            (
                r["player_name"]
                for r in rows
                if (
                    (f"ts:{r['ts_id']}" if r.get("ts_id") else f"id:{r['player_id']}")
                    == identity
                    and r["year"] == year
                )
            ),
            identity,
        )
        print(f"  {year}: {name} ({identity}) -> {', '.join(countries)}")


if __name__ == "__main__":
    print_cross_country_summary()
