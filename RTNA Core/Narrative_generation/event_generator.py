# core/narrative_generation/event_generator.py

import random
from core.character import Character
from core.world import Location

class EventGenerator:
    """
    Generates dynamic events based on player actions, character information, and world context.
    """

    def generate_event(self, player_action: str, player: Character, location: Location) -> dict:
        """
        Generates a dynamic event based on the given context.

        Args:
            player_action: The action performed by the player.
            player: The player character object.
            location: The current location object.

        Returns:
            A dictionary representing the generated event, including a description and potential consequences.
        """

        # Define a list of possible event templates.
        event_templates = [
            "{player} stumbles upon a hidden path leading deeper into {location}.",
            "A {creature} suddenly appears, blocking {player}'s path!",
            "{player} finds a {item} lying on the ground.",
            "The ground begins to shake, and a deep rumble echoes through {location}."
        ]

        # Choose a random event template.
        event_template = random.choice(event_templates)

        # Fill in the template with context-specific details.
        event_description = event_template.format(
            player=player.name,
            location=location.name,
            creature=random.choice(location.creatures) if location.creatures else "mysterious figure",
            item=random.choice(["rusty sword", "healing potion", "ancient map"])
        )

        # Create an event dictionary.
        event = {
            "description": event_description,
            "consequences": []  # Add potential consequences based on event type
        }

        return event
