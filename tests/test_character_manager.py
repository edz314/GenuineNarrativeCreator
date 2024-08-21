# tests/test_character_manager.py

import unittest
from core.character_manager import CharacterManager
from core.character import Character

class TestCharacterManager(unittest.TestCase):

    def setUp(self):
        """
        Sets up test data for CharacterManager tests.
        """
        self.character_data = {
            "player": {
                "name": "Test Player",
                "health": 100,
                "inventory": ["sword", "shield"]
            },
            "npc1": {
                "name": "Friendly NPC",
                "health": 50,
                "dialogue": ["Hello there!"]
            }
        }
        self.character_manager = CharacterManager(self.character_data)

    def test_get_character(self):
        """
        Tests getting a character by name.
        """
        player = self.character_manager.get_character("player")
        self.assertIsInstance(player, Character)
        self.assertEqual(player.name, "Test Player")

        npc = self.character_manager.get_character("npc1")
        self.assertIsInstance(npc, Character)
        self.assertEqual(npc.name, "Friendly NPC")

    def test_get_player(self):
        """
        Tests getting the player character.
        """
        player = self.character_manager.get_player()
        self.assertIsInstance(player, Character)
        self.assertEqual(player.name, "Test Player")

    def test_update_character_health(self):
        """
        Tests updating a character's health.
        """
        player = self.character_manager.get_character("player")
        self.assertEqual(player.health, 100)

        self.character_manager.update_character_health("player", -20)
        self.assertEqual(player.health, 80)

    def test_add_item_to_inventory(self):
        """
        Tests adding an item to a character's inventory.
        """
        player = self.character_manager.get_character("player")
        self.assertEqual(player.inventory, ["sword", "shield"])

        self.character_manager.add_item_to_inventory("player", "potion")
        self.assertEqual(player.inventory, ["sword", "shield", "potion"])

if __name__ == '__main__':
    unittest.main()
