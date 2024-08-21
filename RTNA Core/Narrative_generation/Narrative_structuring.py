# core/narrative_generation/narrative_structuring.py

from core.character import Character
from core.world import Location

class NarrativeStructuring:
    """
    Structures the narrative, incorporating events, dialogue, and more dynamic elements.
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
        narrative["introduction"] = self._generate_introduction(player_action, player, location, event)

        # 2. Events:
        if event:
            narrative["events"].append(event["description"])

        # 3. Dialogue:
        if dialogue:
            narrative["dialogue"] = dialogue

        # 4. Conclusion:
        narrative["conclusion"] = self._generate_conclusion(player, location, event)

        return narrative

    def _generate_introduction(self, player_action: str, player: Character, location: Location, event: dict) -> str:
        """Generates the introduction to the narrative, considering the event."""
        introduction = f"{player.name} decides to {player_action} in the {location.name}. "
        if event:
            if event["type"] == "encounter_creature":
                creature = event.get("creature", "a creature")  # Get creature from event data
                introduction += f"Suddenly, {creature} appears!"
            elif event["type"] == "find_item":
                item = event.get("item", "something")
                introduction += f"{player.name} spots {item} on the ground."
        return introduction

    def _generate_conclusion(self, player: Character, location: Location, event: dict) -> str:
        """Generates the conclusion, considering the event and potential location change."""
        conclusion = ""
        if event:
            if event["type"] == "move_location":
                new_location = event.get("new_location", location.name)
                conclusion += f"{player.name} arrives at {new_location}." 
            elif event["type"] == "health_change":
                health_change = event.get("amount", 0)
                if health_change < 0:
                    conclusion += f"{player.name} feels a bit weaker."
                elif health_change > 0:
                    conclusion += f"{player.name} feels invigorated."
        if not conclusion: 
            conclusion = f"{player.name} continues exploring the {location.name}."
        return conclusion
