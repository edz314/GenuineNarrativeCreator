# core/narrative_generation/event_generator.py

from core.data_management.character_manager import Character
from core.data_management.world_manager import Location

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
            A dictionary representing the generated event, including a description, type, and potential consequences.
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

        event_type = self._get_event_type(player_action)

        # Create an event dictionary with a type and potential additional data
        event = {
            "type": event_type,
            "description": event_description,
            "consequences": self._generate_consequences(event_type, player, location),  
        }

        return event

    def _get_event_type(self, player_action):
        """Determines the type of event based on the player's action."""
        if player_action == "explore":
            return random.choice(["find_item", "encounter_creature", "move_location", "trigger_event", "nothing"])  
        # ... add logic for other player actions 
        return "nothing"

    def _generate_consequences(self, event_type, player, location):
        """Generates consequences based on the event type."""
        consequences = []
        if event_type == "encounter_creature":
            consequences.append({"type": "health_change", "amount": -10})
        elif event_type == "find_item":
            item = random.choice(location.items) if location.items else None
            if item:
                consequences.append({"type": "item_add", "item": item})
                event["item"] = item # Store item name in the event
        elif event_type == "move_location": 
            new_location = random.choice(location.connections) if location.connections else None
            if new_location:
                consequences.append({"type": "move_location", "location": new_location})
                event["new_location"] = new_location # Store the new location
        elif event_type == "trigger_event":
            new_event_type = random.choice(["find_item", "encounter_creature", "nothing"])
            consequences.append({"type": "trigger_event", "event_type": new_event_type})
        elif event_type == "change_character_stat":
            consequences.append({"type": "change_character_stat", "stat": "strength", "amount": 5})
        # ... add more consequence logic based on other event types
        return consequences 
