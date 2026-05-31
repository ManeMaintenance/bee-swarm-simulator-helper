"""Player inventory and hive management."""

from typing import List, Dict


class PlayerData:
    """Tracks player's bees and collected pollen."""

    def __init__(self, player_name: str):
        self.player_name = player_name
        self.bees: List[Dict[str, str]] = []
        self.pollen_count: int = 0

    def add_bee(self, bee_name: str, rarity: str = "common") -> None:
        """Add a bee to the player's hive."""
        self.bees.append({"name": bee_name, "rarity": rarity})

    def collect_pollen(self, amount: int) -> int:
        """Add pollen to the player's total and return new total."""
        self.pollen_count += amount
        return self.pollen_count

    def get_hive_summary(self) -> str:
        """Return a simple summary of the hive."""
        if not self.bees:
            return f"{self.player_name} has no bees yet."
        bee_list = ", ".join([b["name"] for b in self.bees])
        return f"{self.player_name}'s hive: {bee_list}"