"""API client for Bee Swarm Simulator data."""

import requests
from typing import Optional

BASE_URL = "https://api.beeswarmsimulator.example/v1"


class BeeAPI:
    """Minimal client to fetch bee data."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def get_bee_stats(self, bee_name: str) -> dict:
        """Return stats for a given bee type."""
        resp = self.session.get(f"{BASE_URL}/bees/{bee_name.lower()}")
        resp.raise_for_status()
        return resp.json()

    def get_top_pollen_fields(self, limit: int = 5) -> list:
        """Return top pollen fields by efficiency."""
        resp = self.session.get(f"{BASE_URL}/fields/top", params={"limit": limit})
        resp.raise_for_status()
        return resp.json().get("fields", [])