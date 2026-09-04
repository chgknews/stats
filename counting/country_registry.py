"""Country slug registry and Cyrillic name resolution."""
from pathlib import Path
from typing import List, Optional, Tuple

from counting import constants

COUNTRY_REGISTRY: dict[str, dict[str, str]] = {
    "testing": {"nominative": "Тест", "genitive": "Теста"},
    "testing2": {"nominative": "Тест 2", "genitive": "Теста 2"},
    "poland": {"nominative": "Польша", "genitive": "Польши", "title": "Польша", "header": "Польша"},
    "russia": {"nominative": "Россия", "genitive": "России"},
    "armenia": {"nominative": "Армения", "genitive": "Армении", "title": "Армения", "header": "Армения"},
    "azerbaijan": {"nominative": "Азербайджан", "genitive": "Азербайджана", "title": "Азербайджан", "header": "Азербайджан"},
    "russia_01_19": {
        "nominative": "Россия",
        "genitive": "России",
        "title": "2001–2019",
        "header": "Россия (2001–2019)",
        "output_subdir": "russia",
    },
    "russia_igra_tv": {
        "nominative": "Россия",
        "genitive": "России",
        "title": "От «Игры-ТВ»",
        "header": "Чемпионаты России, проводящиеся по лицензии «Игра-ТВ»",
        "output_subdir": "russia",
    },
    "russia_kvrm": {
        "nominative": "Россия",
        "genitive": "России",
        "title": "ЧР по ИИ",
        "header": "ЧР по интеллектуальным играм",
        "output_subdir": "russia",
    },
    "belarus": {"nominative": "Беларусь", "genitive": "Беларуси", "title": "Беларусь", "header": "Беларусь"},
    "ukraine": {"nominative": "Украина", "genitive": "Украины", "title": "Украина", "header": "Украина"},
    "georgia": {"nominative": "Грузия", "genitive": "Грузии", "title": "Грузия", "header": "Грузия"},
    "qazaqstan": {"nominative": "Казахстан", "genitive": "Казахстана", "title": "Казахстан", "header": "Казахстан"},
    "eesti": {"nominative": "Эстония", "genitive": "Эстонии", "title": "Эстония", "header": "Эстония"},
    "lithuania": {"nominative": "Литва", "genitive": "Литвы", "title": "Литва", "header": "Литва"},
    "moldova": {"nominative": "Молдова", "genitive": "Молдовы", "title": "Молдова", "header": "Молдова"},
    "germany": {"nominative": "Германия", "genitive": "Германии", "title": "Германия", "header": "Германия"},
    "israel": {"nominative": "Израиль", "genitive": "Израиля", "title": "Израиль", "header": "Израиль"},
    "cesko": {"nominative": "Чехия", "genitive": "Чехии", "title": "Чехия", "header": "Чехия"},
    "canada": {"nominative": "Канада", "genitive": "Канады", "title": "Канада", "header": "Канада"},
    "latvija": {"nominative": "Латвия", "genitive": "Латвии", "title": "Латвия", "header": "Латвия"},
    "montenegro": {"nominative": "Черногория", "genitive": "Черногории", "title": "Черногория", "header": "Черногория"},
    "finland": {"nominative": "Финляндия", "genitive": "Финляндии", "title": "Финляндия", "header": "Финляндия"},
    "swiss": {"nominative": "Швейцария", "genitive": "Швейцарии", "title": "Швейцария", "header": "Швейцария"},
    "kyrgyzstan": {"nominative": "Кыргызстан", "genitive": "Кыргызстана", "title": "Кыргызстан", "header": "Кыргызстан"},
    "turkey": {"nominative": "Турция", "genitive": "Турции", "title": "Турция", "header": "Турция"},
    "uzbekiston": {"nominative": "Узбекистан", "genitive": "Узбекистана", "title": "Узбекистан", "header": "Узбекистан"},
    "tojikiston": {"nominative": "Таджикистан", "genitive": "Таджикистана", "title": "Таджикистан", "header": "Таджикистан"},
    "turkmaniston": {"nominative": "Туркменистан", "genitive": "Туркменистана", "title": "Туркменистан", "header": "Туркменистан"},
    "cyprus": {"nominative": "Кипр", "genitive": "Кипра", "title": "Кипр", "header": "Кипр"},
    'uk': {'nominative': 'Великобритания', 'genitive': 'Великобритании', 'title': 'Великобритания', 'header': 'Великобритания'},
}


def validate_country_slug(slug: str) -> None:
    """Raise ValueError if the slug is not present in COUNTRY_REGISTRY."""
    if slug not in COUNTRY_REGISTRY:
        raise ValueError(
            f"Unknown country slug '{slug}'. Add an entry to COUNTRY_REGISTRY."
        )


def get_country_nominative(slug: str, override: Optional[str] = None) -> str:
    """Return Cyrillic nominative country name for page titles."""
    if override:
        return override
    validate_country_slug(slug)
    return COUNTRY_REGISTRY[slug]["nominative"]

def get_country_genitive(slug: str, override: Optional[str] = None) -> str:
    """Return Cyrillic genitive country name for markdown."""
    if override:
        return override
    validate_country_slug(slug)
    return COUNTRY_REGISTRY[slug]["genitive"]

def get_country_title(slug: str, override: Optional[str] = None) -> str:
    """Return Cyrillic title country name for page titles."""
    if override:
        return override
    validate_country_slug(slug)
    return COUNTRY_REGISTRY[slug]["title"]

def get_country_header(slug: str, override: Optional[str] = None) -> str:
    """Return Cyrillic header country name for page titles."""
    if override:
        return override
    validate_country_slug(slug)
    return COUNTRY_REGISTRY[slug]["header"]


def get_markdown_output_path(slug: str, *, test: bool = False) -> Path:
    """Hugo markdown path for this country slug.

    ``--test`` writes under ``constants.OUTPUT_MD_TEST`` (``test/``) so
    production pages in ``content/info/countries/`` are left alone.
    """
    validate_country_slug(slug)
    base = Path(constants.OUTPUT_MD_TEST if test else constants.OUTPUT_MD)
    subdir = COUNTRY_REGISTRY[slug].get("output_subdir", "")
    if subdir:
        return base / subdir / f"{slug}.md"
    return base / f"{slug}.md"

def resolve_country_slug(
    file_path: Optional[str] = None,
    explicit_slug: Optional[str] = None,
) -> Tuple[str, List[str]]:
    """
    Resolve country slug and tournament id list from bulk input file.

    Returns (slug, tournament_ids). Supports optional header:
      country: poland
      or bare slug on first line before numeric ids.
    """
    if explicit_slug:
        slug = explicit_slug
    elif file_path:
        slug = Path(file_path).stem
    else:
        raise ValueError("Country slug required: use -cn or -f with a file path")

    if not file_path:
        return slug, []

    tournament_ids: List[str] = []
    with open(file_path, encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            lower = stripped.lower()
            if lower.startswith("country:"):
                if not explicit_slug:
                    slug = lower.split(":", 1)[1].strip()
                continue
            if not explicit_slug and not tournament_ids and not stripped.isdigit():
                slug = stripped
                continue
            tournament_ids.append(stripped)
    return slug, tournament_ids
