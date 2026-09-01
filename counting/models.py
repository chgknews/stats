"""Data models for championship statistics."""
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional, Tuple

from counting import constants
from counting.external_ids import normalize_external_ids
from counting.languages import normalize_languages
from counting.sheet_utils import default_links, merge_links, normalize_age, normalize_sex, parse_bool_flag
from counting.t_fashion import iso_date_year, normalize_tournament_dates


@dataclass
class Awardee:
    """Aggregated medal stats for a team or player (keyed by internal id)."""
    id: int
    name: str = ""
    city: str = ""
    game: str = constants.DEFAULT_GAME
    sum: int = 0
    gold: int = 0
    silver: int = 0
    bronze: int = 0
    external_ids: Dict[str, str] = field(default_factory=dict)
    # Teams only: optional non-Russian display name from the Teams registry.
    non_russian_name: str = ""
    # Per-game medal counts: {game: {"gold", "silver", "bronze"}}.
    by_game: Dict[str, Dict[str, int]] = field(default_factory=dict)

    def add_place(self, place: int, game: str) -> None:
        """Record one medal in the overall totals and in ``game``."""
        bucket = self.by_game.setdefault(game, {"gold": 0, "silver": 0, "bronze": 0})
        match place:
            case 0:
                self.gold += 1
                bucket["gold"] += 1
            case 1:
                self.silver += 1
                bucket["silver"] += 1
            case 2:
                self.bronze += 1
                bucket["bronze"] += 1
            case _:
                print(f"Invalid placement {place} for awardee {self.id}")
                return
        self.sum += 1

    def counts_for(self, games: Iterable[str]) -> Tuple[int, int, int, int]:
        """Return gold, silver, bronze, sum for the given games."""
        gold = silver = bronze = 0
        for game in games:
            bucket = self.by_game.get(game) or {}
            gold += int(bucket.get("gold", 0) or 0)
            silver += int(bucket.get("silver", 0) or 0)
            bronze += int(bucket.get("bronze", 0) or 0)
        return gold, silver, bronze, gold + silver + bronze

    def games_with_medals(self) -> List[str]:
        games: List[str] = []
        for game, bucket in self.by_game.items():
            total = (
                int(bucket.get("gold", 0) or 0)
                + int(bucket.get("silver", 0) or 0)
                + int(bucket.get("bronze", 0) or 0)
            )
            if total:
                games.append(game)
        return games

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "game": self.game,
            "sum": self.sum,
            "gold": self.gold,
            "silver": self.silver,
            "bronze": self.bronze,
            "external_ids": normalize_external_ids(self.external_ids),
            "non_russian_name": self.non_russian_name,
            "by_game": {game: dict(counts) for game, counts in self.by_game.items()},
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Awardee":
        raw_by_game = data.get("by_game") or {}
        by_game = {
            str(game): {
                "gold": int(counts.get("gold", 0) or 0),
                "silver": int(counts.get("silver", 0) or 0),
                "bronze": int(counts.get("bronze", 0) or 0),
            }
            for game, counts in raw_by_game.items()
            if isinstance(counts, dict)
        }
        return cls(
            id=data["id"],
            name=data.get("name", ""),
            city=data.get("city", ""),
            game=data.get("game", constants.DEFAULT_GAME),
            sum=data.get("sum", 0),
            gold=data.get("gold", 0),
            silver=data.get("silver", 0),
            bronze=data.get("bronze", 0),
            external_ids=normalize_external_ids(data.get("external_ids")),
            non_russian_name=data.get("non_russian_name", ""),
            by_game=by_game,
        )


@dataclass
class Player:
    """Player with internal id; roster rows may carry per-tournament old names."""
    id: int
    name: str
    surname: str
    external_ids: Dict[str, str] = field(default_factory=dict)
    # Registry-only (Players section); not used in markdown yet.
    non_russian_name: str = ""
    non_russian_surname: str = ""
    # Per-tournament historical names from Rosters (not stored on Players registry).
    old_name: str = ""
    old_surname: str = ""

    def roster_display_name(self) -> str:
        """Name shown in year-section rosters: old names when present."""
        old = f"{self.old_name.strip()} {self.old_surname.strip()}".strip()
        if old:
            return old
        return f"{self.name} {self.surname}".strip()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "external_ids": normalize_external_ids(self.external_ids),
            "non_russian_name": self.non_russian_name,
            "non_russian_surname": self.non_russian_surname,
            "old_name": self.old_name,
            "old_surname": self.old_surname,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Player":
        return cls(
            id=data["id"],
            name=data["name"],
            surname=data["surname"],
            external_ids=normalize_external_ids(data.get("external_ids")),
            non_russian_name=data.get("non_russian_name", ""),
            non_russian_surname=data.get("non_russian_surname", ""),
            old_name=data.get("old_name", ""),
            old_surname=data.get("old_surname", ""),
        )


@dataclass
class Team:
    """Team with internal id and optional non-Russian display name."""
    id: int
    name: str
    city: str
    players: List[Player] = field(default_factory=list)
    external_ids: Dict[str, str] = field(default_factory=dict)
    non_russian_name: str = ""

    def display_name(self, cyrillic_name: str = "") -> str:
        """Markdown team label; non-Russian name wraps the Cyrillic one when set."""
        cyrillic = (cyrillic_name or self.name).strip()
        non_ru = self.non_russian_name.strip()
        if non_ru:
            return f"{non_ru} («{cyrillic}»)"
        return cyrillic

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "players": [p.to_dict() for p in self.players],
            "external_ids": normalize_external_ids(self.external_ids),
            "non_russian_name": self.non_russian_name,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Team":
        return cls(
            id=data["id"],
            name=data["name"],
            city=data["city"],
            players=[Player.from_dict(p) for p in data.get("players", [])],
            external_ids=normalize_external_ids(data.get("external_ids")),
            non_russian_name=data.get("non_russian_name", ""),
        )


@dataclass
class TournamentAwardee:
    """Represents a team's placement in a tournament."""
    team: Team
    place: int
    old_name: str = ""
    roster_complete: bool = False
    # True for SSI and other individual games: the "team" wraps one player.
    individual: bool = False
    # Individuals sheet only: male / female / other (verbs занял / заняла / заняли).
    sex: str = constants.DEFAULT_SEX

    def get_cyrillic_name(self) -> str:
        """Cyrillic label for this podium row (historical old name if set)."""
        old_name = self.old_name.strip()
        return old_name if old_name else self.team.name

    def get_display_name(self) -> str:
        """Markdown-facing team name, including non-Russian form when set."""
        return self.team.display_name(self.get_cyrillic_name())

    def individual_player(self) -> Optional[Player]:
        """The single medalist for an individual-game row, if present."""
        if not self.team.players:
            return None
        return self.team.players[0]

    def to_dict(self) -> Dict[str, Any]:
        # Keep team.name and old_name separate: old_name is display-only
        # (markdown via get_display_name); Sheets round-trips both columns as-is.
        return {
            "team": self.team.to_dict(),
            "place": self.place,
            "old_name": self.old_name,
            "roster_complete": self.roster_complete,
            "individual": self.individual,
            "sex": self.sex,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TournamentAwardee":
        return cls(
            team=Team.from_dict(data["team"]),
            place=data.get("place", 0),
            old_name=data.get("old_name", ""),
            roster_complete=bool(data.get("roster_complete", False)),
            individual=bool(data.get("individual", False)),
            sex=normalize_sex(data.get("sex", constants.DEFAULT_SEX)),
        )


@dataclass
class TournamentData:
    """Represents data for a single tournament."""
    number: int
    city: str
    year: int
    id: int = 0
    date: str = ""
    start_date: str = ""
    end_date: str = ""
    game: str = constants.DEFAULT_GAME
    awardees: Dict[int, TournamentAwardee] = field(default_factory=dict)
    links: Dict[str, str] = field(default_factory=default_links)
    external_ids: Dict[str, str] = field(default_factory=dict)
    # Only tournaments explicitly marked countable award medals in the
    # team/player podium tables; anything unmarked stays out of them.
    countable: bool = False
    # ISO 639-1 codes; several languages per tournament are allowed.
    languages: List[str] = field(default_factory=list)
    # Complete title override, e.g. «Кубок Армении»; empty → numbered championship title.
    display_name: str = ""
    # Free-text note from the Tournaments sheet; not set by the API or CLI.
    comment: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "number": self.number,
            "date": self.date,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "city": self.city,
            "year": self.year,
            "game": self.game,
            "countable": self.countable,
            "languages": list(self.languages),
            "display_name": self.display_name,
            "comment": self.comment,
            "awardees": {str(p): a.to_dict() for p, a in self.awardees.items()},
            "links": self.links,
            "external_ids": normalize_external_ids(self.external_ids),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TournamentData":
        awardees = {
            int(place): TournamentAwardee.from_dict(awardee_data)
            for place, awardee_data in data.get("awardees", {}).items()
        }
        if "links" in data:
            links = merge_links(data["links"] if isinstance(data["links"], dict) else {})
        elif "link" in data:
            links = merge_links({"results": data["link"]})
        else:
            links = default_links()
        start_date, end_date, display_date = normalize_tournament_dates(
            data.get("start_date", ""),
            data.get("end_date", ""),
            data.get("date", ""),
        )
        year_raw = data.get("year", 0)
        year = int(year_raw) if year_raw else 0
        if not year:
            year = iso_date_year(end_date or start_date)
        return cls(
            id=int(data.get("id") or 0),
            number=data["number"],
            date=display_date,
            start_date=start_date,
            end_date=end_date,
            city=data["city"],
            year=year,
            game=data.get("game", constants.DEFAULT_GAME),
            awardees=awardees,
            links=links,
            external_ids=normalize_external_ids(data.get("external_ids")),
            countable=parse_bool_flag(data.get("countable"), default=False),
            languages=normalize_languages(data.get("languages")),
            display_name=str(data.get("display_name", "") or "").strip(),
            comment=str(data.get("comment", "") or "").strip(),
        )


@dataclass
class MetaData:
    """Metadata about the generated statistics."""
    country: str
    generated_at: str
    statistics: Dict[str, int]
    numbers_champ: Dict[str, int]
    # Opening sentence for markdown, e.g. «Чемпионаты Армении проводятся с 2018 года.»
    intro: str = ""
    # Country-wide age category used in championship titles.
    age: str = constants.DEFAULT_AGE

    def to_dict(self) -> Dict[str, Any]:
        return {
            "country": self.country,
            "generated_at": self.generated_at,
            "statistics": self.statistics,
            "numbers_champ": self.numbers_champ,
            "intro": self.intro,
            "age": self.age,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MetaData":
        return cls(
            country=data["country"],
            generated_at=data["generated_at"],
            statistics=data["statistics"],
            numbers_champ=data.get("numbers_champ", {}),
            intro=str(data.get("intro", "") or "").strip(),
            age=normalize_age(data.get("age", constants.DEFAULT_AGE)),
        )
