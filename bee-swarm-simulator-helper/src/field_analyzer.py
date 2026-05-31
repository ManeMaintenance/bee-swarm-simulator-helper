"""Analyze pollen fields for optimal farming."""

from .bee_api import BeeAPI


class FieldAnalyzer:
    """Compare pollen fields based on bee strengths."""

    def __init__(self, api: BeeAPI):
        self.api = api

    def recommend_field(self, bee_name: str) -> str:
        """Return the best field for a given bee type."""
        try:
            stats = self.api.get_bee_stats(bee_name)
            preferred_field = stats.get("preferred_field", "Sunflower Field")
            return preferred_field
        except Exception:
            return "Sunflower Field"

    def top_fields(self, count: int = 3) -> list:
        """Return top pollen fields from API."""
        try:
            fields = self.api.get_top_pollen_fields(limit=count)
            return [f["name"] for f in fields]
        except Exception:
            return ["Sunflower Field", "Clover Field", "Mushroom Field"]