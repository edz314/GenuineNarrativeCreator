# tests/test_narrative_generator.py

import unittest
from core.narrative_generator import NarrativeGenerator
from core.narrative_structuring import NarrativeStructuring
from core.character_manager import CharacterManager
from core.world_manager import WorldManager

class TestNarrativeGenerator(unittest.TestCase):

    def setUp(self):
        """
        Sets up the necessary objects for testing the NarrativeGenerator.
        """
        self.character_data = {
            "player": {
                "name": "Test Player",
                "health": 100,
                "inventory": ["sword", "shield"]
            }
        }
        self.world_data = {
            "world": {
                "locations": {
                    "forest": {
                        "description": "A dense forest with towering trees.",
                        "connections": ["cave"],
                        "creatures": ["wolf", "goblin"],
                        "items": ["healing potion"]
                    },
                    "cave": {
                        "description": "A dark and damp cave.",
                        "connections": ["forest"],
                        "creatures": ["bat", "spider"]
                    }
                }
            }
        }
        self.narrative_structuring = NarrativeStructuring()
        self.character_manager = CharacterManager(self.character_data)
        self.world_manager = WorldManager(self.world_data)
        self.narrative_generator = NarrativeGenerator(self.narrative_structuring, self.character_manager, self.world_manager)

    def test_generate_narrative(self):
        """
        Tests the generate_narrative method with different player actions and locations.
        """
        # Test case 1: Explore the forest
        narrative = self.narrative_generator.generate_narrative("explore", "forest")
        self.assertIn("Test Player decides to explore in forest", narrative)
        self.assertIn("A dense forest with towering trees.", narrative)

        # Test case 2: Enter the cave
        narrative = self.narrative_generator.generate_narrative("enter", "cave")
        self.assertIn("Test Player decides to enter in cave", narrative)
        self.assertIn("A dark and damp cave.", narrative)

    def test_generate_narrative_invalid_location(self):
        """
        Tests handling of invalid location names.
        """
        narrative = self.narrative_generator.generate_narrative("explore", "invalid_location")
        # You might want to assert a specific error message or behavior here.
        # For example:
        # self.assertIn("Error: Location 'invalid_location' not found.", narrative)

if __name__ == '__main__':
    unittest.main()
