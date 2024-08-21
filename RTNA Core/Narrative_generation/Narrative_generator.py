# core/narrative_generation/narrative_generator.py

from core.narrative_structuring import NarrativeStructuring
from core.character_manager import CharacterManager
from core.world_manager import WorldManager
from core.narrative_generation.event_generator import EventGenerator
from core.dialogue import DialogueManager  # New import for dialogue

class NarrativeGenerator:
    """
    Generates narrative text, handles events and dialogue.
    """

    def __init__(self, narrative_structuring: NarrativeStructuring, 
                 character_manager: CharacterManager, 
                 world_manager: WorldManager):
        """Initializes NarrativeGenerator."""
        self.narrative_structuring = narrative_structuring
        self.character_manager = character_manager
        self.world_manager = world_manager
        self.event_generator = EventGenerator() 
        self.dialogue_manager = DialogueManager() # Initialize DialogueManager

    def generate_narrative(self, player_action: str, current_location: str) -> str:
        """Generates narrative text based on player action and location."""
        player = self.character_manager.get_player()
        location_details = self.world_manager.get_location_details(current_location)

        # 1. Generate Event:
        event = self.event_generator.generate_event(player_action, player, location_details)

        # 2. Apply Event Consequences:
        self._apply_event_consequences(event, player, current_location)

        # 3. Generate Dialogue (if applicable)
        dialogue = self.dialogue_manager.get_dialogue(event, player, location_details)

        # 4. Structure Narrative (include event and dialogue):
        structured_narrative = self.narrative_structuring.structure_narrative(
            player_action, player, location_details, event, dialogue
        )

        # 5. Generate Text from Structure:
        narrative_text = self._generate_text_from_structure(structured_narrative)
        return narrative_text

    def _apply_event_consequences(self, event: dict, player: Character, current_location: str):
        """Applies the consequences of an event."""
        for consequence in event["consequences"]:
            if consequence["type"] == "health_change":
                self.character_manager.update_character_health(player.name, consequence["amount"])
            elif consequence["type"] == "item_add":
                self.character_manager.add_item_to_inventory(player.name, consequence["item"])
            # ... add other consequence types as needed

    def _generate_text_from_structure(self, structured_narrative: dict) -> str:
        """Generates text from the structured narrative."""
        # ... implement your text generation logic here ...
        pass  
