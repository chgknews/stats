"""Processes raw tournament data into structured objects."""
from typing import Dict, List, Optional, Tuple, Any

from counting import constants
from counting.languages import normalize_languages
from counting.tournament_api import TournamentAPI
from counting.models import Team, Player
from counting.t_fashion import (
    transform_date,
    inflect_town,
    get_city_tournament,
    get_tournament_date,
)


class TournamentProcessor:
    """Processes raw tournament data into structured objects."""

    def extract_team_data(self, raw_team: Dict[str, Any]) -> Team:
        """Extract team data from raw API response (rating.chgk.info ids as ts_id)."""
        team_ts_id = str(raw_team["team"]["id"])
        team_name = raw_team["team"]["name"]
        town_name = raw_team["team"]["town"]["name"]
        players = [
            Player(
                id=0,
                name=p["player"]["name"],
                surname=p["player"]["surname"],
                external_ids={constants.EXTERNAL_ID_TS: str(p["player"]["id"])},
            )
            for p in raw_team.get("teamMembers", [])
        ]
        return Team(
            id=0,
            name=team_name,
            city=town_name,
            players=players,
            external_ids={constants.EXTERNAL_ID_TS: team_ts_id},
        )

    def process_tournament(
        self, tournament_id: int
    ) -> Tuple[Optional[Dict[str, Any]], Optional[List[Dict[str, Any]]]]:
        """Process a tournament and return info and results."""
        info = TournamentAPI.get_tournament_info(tournament_id)
        if not info:
            return None, None

        try:
            date_start = info["dateStart"]
            date_end = info["dateEnd"]
            city_id = info["idtown"]
            city_name = inflect_town(get_city_tournament(city_id))
            tournament_date = get_tournament_date(date_start, date_end)
            year = transform_date(date_end).year
        except KeyError as exc:
            print(f"Missing data in tournament {tournament_id}: {exc}")
            return None, None

        results = TournamentAPI.get_tournament_results(tournament_id)
        country_contributors = [
            team for team in results
            if any(flag["id"] == constants.NATIONAL_TEAM_FLAG_ID for flag in team.get("flags", []))
        ]
        if not country_contributors:
            country_contributors = results

        return (
            {
                "date": tournament_date,
                "start_date": date_start[:10],
                "end_date": date_end[:10],
                "city": city_name,
                "year": year,
                "ts_id": str(tournament_id),
                "languages": normalize_languages(
                    entry.get("id") or entry.get("value") or entry.get("name")
                    for entry in info.get("languages", [])
                    if isinstance(entry, dict)
                ),
            },
            country_contributors,
        )
