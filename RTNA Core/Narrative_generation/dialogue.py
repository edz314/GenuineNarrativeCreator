# core/narrative_generation/dialogue.py

import random
from core.character import Character
from core.world import Location

class DialogueManager:
    """
    Manages and generates dialogue for the game.
    """

    def __init__(self):
        """
        Initializes the dialogue manager with sample dialogue data.
        """
        self.dialogue_data = {
            "find_item": {
                "healing potion": [
                    "You carefully pick up the healing potion. It could come in handy.",
                    "A healing potion! This might save your life later."
                ],
                "rusty sword": [
                    "You find a rusty sword. It's better than nothing, but you hope to find something sharper.",
                    "The sword is covered in rust, but you might be able to clean it up."
                ],
                "default": [
                    "You discover something interesting.",
                    "You find something lying on the ground."
                ]
            },
            "encounter_creature": {
                "wolf": [
                    "The wolf snarls at you, baring its teeth.",
                    "A large wolf blocks your path, its eyes glowing in the dim light."
                ],
                "goblin": [
                    "The goblin sneers at you and brandishes a crude dagger.",
                    "A small, green-skinned goblin jumps out from behind a tree!"
                ],
                "default": [
                    "A creature appears before you.",
                    "Something stirs in the shadows."
                ]
            }
        }

    def get_dialogue(self, event: dict, player: Character, location: Location) -> str:
        """
        Returns dialogue based on the event, if available.

        Args:
            event: The current event dictionary.
            player: The player character object.
            location: The current location object.

        Returns:
            A string containing the dialogue, or an empty string if no dialogue is found.
        """
        event_type = event.get("type")
        if event_type:
            if event_type == "find_item":
                item_name = event.get("item")
                dialogue_lines = self.dialogue_data["find_item"].get(item_name) or self.dialogue_data["find_item"]["default"]
                return random.choice(dialogue_lines)
            elif event_type == "encounter_creature":
                creature_name = event.get("creature")
                dialogue_lines = self.dialogue_data["encounter_creature"].get(creature_name) or self.dialogue_data["encounter_creature"]["default"]
                return random.choice(dialogue_lines)
        return ""
