# core/dialogue.py

class DialogueManager:
    def __init__(self):
        self.dialogue_data = {
            # Example dialogue data (add more as needed)
            "find_item": {
                "healing potion": "You find a healing potion. It might be useful later.",
                "rusty sword": "You discover a rusty sword. It doesn't look very sharp."
            },
            "encounter_creature": {
                "wolf": "A menacing wolf growls at you.",
                "goblin": "A mischievous goblin eyes you suspiciously."
            }
        }

    def get_dialogue(self, event: dict, player: Character, location: Location) -> str:
        """Returns dialogue based on the event, if available."""
        event_type = event.get("type") 
        if event_type:
            if event_type == "find_item":
                item_name = event.get("item")
                return self.dialogue_data["find_item"].get(item_name, "")
            elif event_type == "encounter_creature":
                creature_name = event.get("creature")
                return self.dialogue_data["encounter_creature"].get(creature_name, "")
        return ""
