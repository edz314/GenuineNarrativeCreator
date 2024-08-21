# tests/test_world_manager.py

import unittest
from core.world_manager import WorldManager
from core.world import Location

class TestWorldManager(unittest.TestCase):

    def setUp(self):
        """
        Sets up test data for the WorldManager.
        """
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
        self.world_manager = WorldManager(self.world_data)

    def test_create_world_from_data(self):
        """
        Tests the creation of the world from data.
        """
        world = self.world_manager.world
        self.assertIsNotNone(world)
        self.assertEqual(len(world.locations), 2)  # Check if two locations were created

    def test_get_location_details(self):
        """
        Tests getting details of a specific location.
        """
        forest = self.world_manager.get_location_details("forest")
        self.assertIsInstance(forest, Location)
        self.assertEqual(forest.name, "forest")
        self.assertEqual(forest.description, "A dense forest with towering trees.")
        self.assertEqual(forest.connections, ["cave"])
        self.assertEqual(forest.creatures, ["wolf", "goblin"])
        self.assertEqual(forest.items, ["healing potion"])

    def test_get_location_details_invalid(self):
        """
        Tests getting details of an invalid location.
        """
        invalid_location = self.world_manager.get_location_details("invalid_location")
        self.assertIsNone(invalid_location)

if __name__ == '__main__':
    unittest.main()

