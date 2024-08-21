# tests/test_event_generator.py

import unittest
from core.narrative_generation.event_generator import EventGenerator
from core.character import Character
from core.world import Location

class TestEventGenerator(unittest.TestCase):

    def setUp(self):
        """
        Sets up a sample player character and location for event generation tests.
        """
        self.player = Character(name="Test Player", health=100, inventory=[])
        self.location = Location(
            name="Forest", 
            description="A dense forest with towering trees.", 
            connections=[], 
            creatures=["wolf", "goblin"], 
            items=["healing potion"]
        )
        self.event_generator = EventGenerator()

    def test_generate_event(self):
        """
        Tests that the generate_event method returns a valid event dictionary.
        """
        event = self.event_generator.generate_event("explore", self.player, self.location)

        # Assert that the event dictionary has the expected keys
        self.assertIn("description", event)
        self.assertIn("consequences", event)

        # Assert that the description is a string
        self.assertIsInstance(event["description"], str)

        # Assert that consequences is a list (even if empty for now)
        self.assertIsInstance(event["consequences"], list)

    def test_event_description_content(self):
        """
        Tests that the generated event description contains relevant context.
        """
        event = self.event_generator.generate_event("explore", self.player, self.location)
        description = event["description"]

        # Check if player name and location name are in the description
        self.assertIn(self.player.name, description)
        self.assertIn(self.location.name, description)

        # Check if a creature or item from the location is present (randomly chosen)
        self.assertTrue(
            any(creature in description for creature in self.location.creatures) or
            any(item in description for item in self.location.items)
        )

if __name__ == "__main__":
    unittest.main()
