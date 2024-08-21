# core/narrative_generation/narrative_structuring.py

from core.character import Character
from core.world import Location

class NarrativeStructuring:
    """
    Structures the narrative, incorporating events and dialogue.
    """

    def structure_narrative(self, player_action: str, player: Character, location: Location,
                          event: dict = None, dialogue: str = None) -> dict:
        """
        Creates a structured narrative from the given information.
        """
        narrative = {
            "introduction": "",
            "events": [],
            "dialogue": "",
            "conclusion": ""
        }

        # 1. Introduction:
        narrative["introduction"] = self._generate_introduction(player_action, player, location)

        # 2. Events:
        if event:
            narrative["events"].append(event["description"]) 

        # 3. Dialogue:
        if dialogue:
            narrative["dialogue"] = dialogue

        # 4. Conclusion (Placeholder - customize based on game logic):
        narrative["conclusion"] = self._generate_conclusion(player, location)

        return narrative

    def _generate_introduction(self, player_action: str, player: Character, location: Location) -> str:
        """Generates the introduction to the narrative."""
        return f"{player.name} decides to {player_action} in the {location.name}."

    def _generate_conclusion(self, player: Character, location: Location) -> str:
        """Generates the conclusion to the narrative."""
        # Placeholder - add more complex logic based on game state and events
        return f"{player.name} continues their journey in the {location.name}." 
