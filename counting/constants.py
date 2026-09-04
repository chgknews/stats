from enum import Enum
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# anchors
TEAMS_ANCHORS = "teams"
PLAYERS_ANCHORS = "players"
MISSING_DATA_ANCHORS = "missing-data"
SOURCES_ANCHORS = "sources"
CONTENTS_ANCHOR = "contents"
BACK_TO_CONTENTS = "К оглавлению"

# context
TEAMS_CONTEXT = "Команды"
PLAYERS_CONTEXT = "Игроки"
MISSING_DATA_TAB = "Проблемы"
SOURCES_TAB = "Источники и благодарности"
CHAMPIONSHIPS_TAB = "Чемпионаты"
TOURNAMENTS_TAB_PREFIX = "Турниры по "
ALL_MEDALS_HEADER = "Все медали"
CONTACT_EMAIL = "chgknews.info@gmail.com"
MORE_INFO_LABEL = "Больше информации о турнире — "
VIDEO_ONE_LABEL = "Также доступно связанное с турниром видео: "
VIDEO_MANY_LABEL = "Также доступны связанные с турниром видео: "
FULL_RESULTS_LEAD = "Полные результаты можно найти"
PHASE_RESULTS_LEAD = "Результаты {ordinal} этапа можно найти"
PLAYERS_ERROR = (
    "Состав победителей неизвестен. Если вы что-то о нём знаете, "
    f"напишите, пожалуйста, на <{CONTACT_EMAIL}>."
)
INDIVIDUAL_PRIZERS_INCOMPLETE = (
    "На этом турнире часть призёров неизвестна. Если вы что-то о них знаете, "
    f"напишите, пожалуйста, на <{CONTACT_EMAIL}>."
)
UNCOUNTABLE_NOTE = "Турнир не учитывается в общей медальной статистике."
CITY_UNKNOWN = "Город проведения пока неизвестен."
RESULTS_NOT_COUNTED = "Результаты пока не учтены в статистике."
PLAYERS_STATS_ERROR = (
    "Статистика неполна, поскольку на следующих турнирах пока нет составов:\n"
)
MISSING_DATA_INTRO = (
    "Ниже собрана информация о том, каких данных не хватает "
    "в том или ином турнире."
)
MISSING_DATA_YEAR = "Год"
MISSING_DATA_TOURNAMENT = "Турнир"
MISSING_DATA_WHAT = "Чего не хватает"
SOURCES_INTRO = (
    "Здесь указан список источников, откуда взята та или иная информация "
    "на этой странице. "
)
SOURCES_YEAR = "Год"
SOURCES_TOURNAMENT = "Турнир"
SOURCES_ONE = "Источник"
SOURCES_MANY = "Источники"

# games
DEFAULT_GAME = "chgk"
GAMES_SHORT_NAMES = {
    "chgk": "спортивному ЧГК",
    "kvrm": "КВРМ",
    "zakovat": "«Заковату»",
    "od": "ОД",
    "brain": "БР",
    "tables": "ДС",
    "kinsbf": "КИнСбФ",
    "brain_wf": "БРБФ",
    "troyka": "«Тройке»",
    "hamsa": "«Хамсе»",
    "ksi": "КСИ",
    "ek": "ЭК",
    "ssi": "ССИ",
    "ssi_f": "ССИ с фальстартами",
}
GAMES_FULL_NAMES = {
    "chgk": "Спортивное «Что? Где? Когда?»",
    "kvrm": "Командная викторина с раундами по минуте",
    "zakovat": "«Заковат»",
    "od": "Основная дисциплина",
    "brain": "Брейн-ринг",
    "tables": "«Два стола»",
    "kinsbf": "Командная игра на скорость без фальстартов",
    "brain_wf": "Брейн-ринг без фальстартов",
    "troyka": "Тройка",
    "hamsa": "Хамса",
    "ksi": "Командная «Своя игра»",
    "ek": "Эрудит-квартет",
    "ssi": "Спортивная «Своя игра»",
    "ssi_f": "Спортивная «Своя игра» с фальстартами",
}
GAMES_FULL_NAMES_CASE = {
    "chgk": "спортивному «Что? Где? Когда?»",
    "kvrm": "командной викторине с раундами по минуте",
    "zakovat": "«Заковату»",
    "ii": "интеллектуальным играм",
    "od": "основной дисциплины чемпионата",
    "brain": "брейн-рингу",
    "tables": "игре «Два стола»",
    "kinsbf": "командной игре на скорость без фальстартов",
    "brain_wf": "брейн-рингу без фальстартов",
    "troyka": "«Тройке»",
    "hamsa": "«Хамсе»",
    "ksi": "командной «Своей игре»",
    "ek": "эрудит-квартету",
    "ssi": "спортивной «Своей игре»",
    "ssi_f": "спортивной «Своей игре» с фальстартами",
}
# ages
DEFAULT_AGE = "adult"
AGES = ("adult", "youth", "student", "school", "juvenal", "child")
# Inserted before «чемпионат»: «молодёжный чемпионат».
AGE_CHAMPIONSHIP_PREFIX = {
    "youth": "молодёжный ",
    "student": "студенческий ",
    "school": "школьный ",
    "child": "детский ",
}
# Appended after «чемпионат {country}»: «чемпионат Армении среди ювеналов (8–9 классы)».
AGE_CHAMPIONSHIP_SUFFIX = {
    "juvenal": " среди ювеналов (8–9 классы)",
}
# Plural section titles: «Студенческие чемпионаты России».
AGE_CHAMPIONSHIPS_HEADING = {
    "adult": "Чемпионаты {country}",
    "youth": "Молодёжные чемпионаты {country}",
    "student": "Студенческие чемпионаты {country}",
    "school": "Школьные чемпионаты {country}",
    "child": "Детские чемпионаты {country}",
    "juvenal": "Чемпионаты {country} среди ювеналов (8–9 классы)",
}

GAMES_COLUMN_NAMES = {
    "chgk": "ЧГК",
    "kvrm": "КВРМ",
    "zakovat": "«Заковат»",
    "od": "ОД",
    "brain": "БР",
    "tables": "ДС",
    "kinsbf": "КИнСбФ",
    "brain_wf": "БРБФ",
    "troyka": "«Тройка»",
    "hamsa": "«Хамса»",
    "ksi": "КСИ",
    "ek": "ЭК",
    "ssi": "ССИ",
    "ssi_f": "ССИ с фальстартами",
}
# Medal-table groups, in column order. Medals from every member are summed
# into one I/II/III block. If two or more members have medals, the block is
# named by the merge key (kvrm → «КВРМ», brain → «БР», …).
GAME_MEDAL_GROUPS = (
    ("kvrm", ("chgk", "kvrm", "zakovat", "od")),
    ("brain", ("brain", "tables")),
    ("brain_wf", ("kinsbf", "brain_wf")),
    ("ek", ("ek",)),
    ("hamsa", ("hamsa",)),
    ("ksi", ("ksi",)),
    ("ssi", ("ssi", "ssi_f")),
    ("troyka", ("troyka",)),
)
# Multi-game medal-table tie-break, and tournament-tab merge, for these games.
PRIMARY_MEDAL_GAMES = ("chgk", "zakovat", "od", "kvrm")
# Shared tab id when two or more PRIMARY_MEDAL_GAMES are on the page.
PRIMARY_GAMES_ANCHOR = "kvrm"
# Individual games: medals go to the player table only, never the team table.
# Editions and medalists are sheet-only (Tournaments + Individuals); no rating API.
INDIVIDUAL_GAMES = frozenset({"ssi", "ssi_f"})

# Individuals sheet: grammatical gender for individual-game place verbs.
DEFAULT_SEX = "male"
SEXES = ("male", "female", "other")
SEX_PLACE_VERB = {
    "male": "занял",
    "female": "заняла",
    "other": "заняли",
}

#other
OUTPUT_MD = str(REPO_ROOT / "content" / "info" / "countries") + "/"
# Country pages written here when count_champions.py / replace_doubles.py run with --test.
OUTPUT_MD_TEST = str(REPO_ROOT / "content" / "test") + "/"
# One public dump of every country tab (sheet sections, not computed stats).
# Production recounts rewrite this file; ``--test`` does not.
OUTPUT_JSON = str(REPO_ROOT / "content" / "info" / "data.json")
NATIONAL_TEAM_FLAG_ID = 50  # Flag ID for national teams ('ЧСт')
TOP_PLACES = 3  # Number of top places to track (gold, silver, bronze)

# External identity sources (extensible). One entity may have at most one id per source.
EXTERNAL_ID_TS = "ts_id"  # rating.chgk.info
EXTERNAL_ID_UZ = "uz_id"  # turnirlar.uz
EXTERNAL_ID_UA = "ua_id"  # Ukrainian rating site
# Tournament page for ua_id (missing-data name links when there is no ts URL).
UA_TOURNAMENT_URL_TEMPLATE = "https://rating.chgk.com.ua/tournament/{id}"
EXTERNAL_ID_SOURCES = (EXTERNAL_ID_TS, EXTERNAL_ID_UZ, EXTERNAL_ID_UA)

# Global internal-id counters live on this spreadsheet tab (name starts with _).
ENTITY_IDS_WORKSHEET = "_entity_ids"
# Cross-country duplicate pairs (ts_id / uz_id / ua_id). Not a country tab.
DOUBLES_WORKSHEET = "doubles"
# Global entity catalogs used by doubles search (one tab per kind).
TOURNAMENT_SET_WORKSHEET = "tournaments"
TEAM_SET_WORKSHEET = "teams"
PLAYER_SET_WORKSHEET = "players"
# Country-data dump skips these tab titles (plus any title starting with _).
SKIP_WORKSHEET_TITLES = frozenset({
    ENTITY_IDS_WORKSHEET,
    DOUBLES_WORKSHEET,
    TOURNAMENT_SET_WORKSHEET,
    TEAM_SET_WORKSHEET,
    PLAYER_SET_WORKSHEET,
    "backup",
})

KIND_TOURNAMENT = "tournament"
KIND_TEAM = "team"
KIND_PLAYER = "player"
ENTITY_KINDS = (KIND_TOURNAMENT, KIND_TEAM, KIND_PLAYER)
ENTITY_SET_WORKSHEETS = {
    KIND_TOURNAMENT: TOURNAMENT_SET_WORKSHEET,
    KIND_TEAM: TEAM_SET_WORKSHEET,
    KIND_PLAYER: PLAYER_SET_WORKSHEET,
}

# Google Sheets configuration
GOOGLE_SHEETS_CREDENTIALS = str(REPO_ROOT / "credentials.json")
GOOGLE_SHEETS_SPREADSHEET_ID = "1ejR6qsDeICtN-ILoVRknTibgQ-MFBv1YUNw6hK_R5fM"
GOOGLE_SHEETS_TEST_SPREADSHEET_ID = "1HKNi0YXYkvhcV76DsW25hzvvbJ190cLWTWcbYuO4yC4"