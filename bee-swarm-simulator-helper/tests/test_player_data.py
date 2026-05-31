"""Tests for PlayerData class."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.player_data import PlayerData


def test_add_bee():
    player = PlayerData("TestBot")
    player.add_bee("Rascal Bee", "rare")
    assert len(player.bees) == 1
    assert player.bees[0]["name"] == "Rascal Bee"


def test_collect_pollen():
    player = PlayerData("TestBot")
    total = player.collect_pollen(150)
    assert total == 150
    total = player.collect_pollen(50)
    assert total == 200


def test_hive_summary_empty():
    player = PlayerData("EmptyHive")
    assert "no bees yet" in player.get_hive_summary()


def test_hive_summary_with_bees():
    player = PlayerData("BeeMaster")
    player.add_bee("Honey Bee")
    player.add_bee("Fire Bee")
    summary = player.get_hive_summary()
    assert "Honey Bee" in summary
    assert "Fire Bee" in summary