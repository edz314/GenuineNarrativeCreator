# core/narrative_generator.py

from core.narrative_structuring import NarrativeStructuring
from core.character_manager import CharacterManager
from core.world_manager import WorldManager

class NarrativeGenerator:
    """
    Generates narrative text based on game state, player actions, and character information.
    """

    def __init__(self, narrative_structuring: NarrativeStructuring, 
                 character_manager: CharacterManager, 
                 world_manager: WorldManager):
        """
        Initializes the NarrativeGenerator.

        Args:
            narrative_structuring: An object responsible for structuring the narrative.
            character_manager: An object for managing characters.
            world_manager: An object for managing the game world.
        """
        self.narrative_structuring = narrative_structuring
        self.character_manager = character_manager
        self.world_manager = world_manager

    def generate_narrative(self, player_action: str, current_location: str):
        """
        Generates narrative text based on the given player action and location.

        Args:
            player_action: The action performed by the player.
            current_location: The player's current location.

        Returns:
            A string containing the generated narrative text.
        """
        
        # Example: Fetching relevant data from other modules
        player = self.character_manager.get_player()
        location_details = self.world_manager.get_location_details(current_location)

        # Placeholder for generating the structured narrative 
        # based on player_action, player, and location_details
        structured_narrative = self.narrative_structuring.structure_narrative(player_action, player, location_details) 

        # Generate narrative text from the structured narrative.
        narrative_text = self._generate_text_from_structure(structured_narrative)

        return narrative_text

    def _generate_text_from_structure(self, structured_narrative: dict):
        """
        Generates narrative text from the structured narrative.

        Args:
            structured_narrative: A structured representation of the narrative.

        Returns:
            A string containing the generated narrative text.
        """

        # Implement your text generation logic here.
        # Example using a simple template:
        narrative_text = f"{structured_narrative['introduction']}\n"
        for event in structured_narrative['events']:
            narrative_text += f"- {event['description']}\n"
        narrative_text += f"{structured_narrative['conclusion']}"

        return narrative_text
