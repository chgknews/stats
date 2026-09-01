"""API client for fetching tournament data from rating.chgk.net."""
from typing import Dict, List, Optional, Any
import requests
from requests.exceptions import RequestException


class TournamentAPI:
    """API client for fetching tournament data from rating.chgk.net."""
    BASE_URL = "https://api.rating.chgk.net"
    TIMEOUT = 10
    _session = None

    @classmethod
    def get_session(cls):
        """Get or create a requests session with retry logic."""
        if cls._session is None:
            cls._session = requests.Session()
            retry = requests.adapters.Retry(
                total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504]
            )
            adapter = requests.adapters.HTTPAdapter(max_retries=retry)
            cls._session.mount("http://", adapter)
            cls._session.mount("https://", adapter)
        return cls._session

    @classmethod
    def get_tournament_results(cls, tournament_id: int) -> List[Dict[str, Any]]:
        """Fetch tournament results from the API."""
        url = f"{cls.BASE_URL}/tournaments/{tournament_id}/results.json"
        params = {"includeTeamMembers": 1, "includeTeamFlags": 1}
        try:
            response = cls.get_session().get(url, params=params, timeout=cls.TIMEOUT)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"API Error for tournament {tournament_id}: {str(e)}")
            return []

    @classmethod
    def get_tournament_info(cls, tournament_id: int) -> Optional[Dict[str, Any]]:
        """Fetch tournament information from the API."""
        url = f"{cls.BASE_URL}/tournaments/{tournament_id}.json"
        try:
            response = cls.get_session().get(url, timeout=cls.TIMEOUT)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"API Error fetching tournament info {tournament_id}: {str(e)}")
            return None

