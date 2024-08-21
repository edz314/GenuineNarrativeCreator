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
            "type":  self._get_event_type(player_action),  # New: Assign an event type
            "description": event_description,
            "consequences": self._generate_consequences(event_type, player, location),  # New: Generate consequences
            # ... add other event data as needed (e.g., "item", "creature")
        }

        return event
        
    def _get_event_type(self, player_action):
        """Determines the type of event based on the player's action."""
        if player_action == "explore":
            return random.choice(["find_item", "encounter_creature", "nothing"])  # Example
        # ... add logic for other player actions 
        return "nothing"

    def _generate_consequences(self, event_type, player, location):
        """Generates consequences based on the event type."""
        consequences = []
        if event_type == "encounter_creature":
            # Example: Reduce player health for creature encounters
            consequences.append({"type": "health_change", "amount": -10})
        elif event_type == "find_item":
            # Example: Add the found item to the player's inventory
            item = random.choice(location.items) if location.items else None
            if item:
                consequences.append({"type": "item_add", "item": item})
                event["item"] = item # Store item name in the event
        # ... add more consequence logic based on other event types
        return consequences
