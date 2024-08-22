from core.narrative_structuring import NarrativeStructuring
from core.character_manager import CharacterManager
from core.world_manager import WorldManager
from RTNA_Core.Narrative_generation.PromptManager import PromptManager
from data.lore import Lore

class NarrativeGenerator:
    """
    Generates narrative based on player actions and the current state of the game world.
    Integrates with the Prompt Manager, LLM, and Lore to maintain narrative consistency.
    """

    def __init__(self, narrative_structuring: NarrativeStructuring, character_manager: CharacterManager, world_manager: WorldManager):
        """
        Initializes the NarrativeGenerator with required managers and structuring tools.

        Args:
            narrative_structuring (NarrativeStructuring): Handles the structure of the narrative.
            character_manager (CharacterManager): Manages characters in the narrative.
            world_manager (WorldManager): Manages the game world state and environment.
        """
        self.narrative_structuring = narrative_structuring
        self.character_manager = character_manager
        self.world_manager = world_manager
        self.lore = Lore()  # Initialize the Lore class to access world and character information
        self.prompt_manager = PromptManager(narrative_structuring, self.get_context_manager())

    def get_context_manager(self):
        """
        Returns the context manager, which handles narrative context such as past interactions,
        character developments, and ongoing story arcs. This method can be expanded to provide
        more complex context management in the future.

        Returns:
            dict: A dictionary representing the current context of the narrative.
        """
        # For now, return a simple context. This can be expanded to use a full ContextManager class.
        return {
            "previous_actions": [],
            "current_emotions": {}
        }

    def generate_narrative(self, player_action, current_location):
        """
        Generates the narrative text based on player action and current location.

        Args:
            player_action (str): The action performed by the player.
            current_location (str): The current location of the player in the game world.

        Returns:
            str: The generated narrative text.
        """
        try:
            self._validate_input(player_action, current_location)

            # Retrieve the relevant data based on player action and location
            characters = self.character_manager.get_characters_in_location(current_location)
            world_state = self.world_manager.get_world_state(current_location)

            # Retrieve relevant lore information for consistency
            world_rules = self.lore.get_world_rules()
            character_backstories = {
                character.name: self.lore.get_character_backstory(character.name)
                for character in characters
            }

            # Generate a narrative structure (e.g., setup, conflict, resolution)
            narrative_structure = self.narrative_structuring.create_structure(player_action, characters, world_state)

            # Use the PromptManager to create a prompt for the LLM or narrative engine
            main_character = self.character_manager.get_main_character()
            current_state = {
                "location": current_location,
                "action_description": player_action,
                "characters": characters,
                "world_state": world_state,
                "world_rules": world_rules,
                "character_backstories": character_backstories
            }
            prompt = self.prompt_manager.create_prompt("action", main_character, current_state)

            # Use the generated prompt in the narrative process (e.g., sending it to an LLM)
            narrative_text = self._generate_narrative_from_prompt(prompt)

            return narrative_text

        except ValueError as ve:
            # Handle invalid inputs
            raise ve

        except Exception as e:
            # Handle any unexpected errors during narrative generation
            raise RuntimeError(f"Failed to generate narrative: {str(e)}")

    def _generate_narrative_from_prompt(self, prompt):
        """
        Generates narrative text based on the given prompt.

        Args:
            prompt (str): The prompt generated by the PromptManager.

        Returns:
            str: The narrative text generated from the prompt.
        """
        # Here you would typically integrate with a language model or narrative engine.
        # For now, this is a placeholder implementation.
        return f"Generated narrative: {prompt}"

    def _validate_input(self, player_action, current_location):
        """
        Validates the inputs to the narrative generator.

        Args:
            player_action (str): The action performed by the player.
            current_location (str): The current location of the player in the game world.

        Raises:
            ValueError: If any input is invalid.
        """
        if not player_action or not isinstance(player_action, str):
            raise ValueError("Invalid player action. It must be a non-empty string.")
        if not current_location or not isinstance(current_location, str):
            raise ValueError("Invalid current location. It must be a non-empty string.")
