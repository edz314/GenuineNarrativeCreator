class NarrativeGenerator:
    """
    Generates narrative based on player actions and the current state of the game world.
    """

    def __init__(self, narrative_structuring, character_manager, world_manager):
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

            # Generate a narrative structure (e.g., setup, conflict, resolution)
            narrative_structure = self.narrative_structuring.create_structure(player_action, characters, world_state)

            # Populate the structure with specific details
            narrative_text = self._compose_narrative(narrative_structure, characters, world_state)

            return narrative_text

        except ValueError as ve:
            # Handle invalid inputs
            raise ve

        except Exception as e:
            # Handle any unexpected errors during narrative generation
            raise RuntimeError(f"Failed to generate narrative: {str(e)}")

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

    def _compose_narrative(self, narrative_structure, characters, world_state):
        """
        Composes the narrative text based on the provided structure, characters, and world state.

        Args:
            narrative_structure (dict): The structure of the narrative (e.g., setup, conflict, resolution).
            characters (list): The list of characters involved in the narrative.
            world_state (dict): The current state of the world/environment.

        Returns:
            str: The composed narrative text.
        """
        narrative_text = ""

        # Example of structuring the narrative based on setup, conflict, and resolution
        setup = narrative_structure.get('setup', '')
        conflict = narrative_structure.get('conflict', '')
        resolution = narrative_structure.get('resolution', '')

        # Combine these elements into a cohesive narrative
        narrative_text += f"{setup}\n"
        if conflict:
            narrative_text += f"{conflict}\n"
        if resolution:
            narrative_text += f"{resolution}\n"

        # Add character-specific dialogue or actions
        for character in characters:
            dialogue = character.get_dialogue()
            narrative_text += f"{character.name}: {dialogue}\n"

        # Integrate world state elements if necessary
        if 'weather' in world_state:
            narrative_text += f"The weather is {world_state['weather']}.\n"

        # Final narrative adjustments
        return narrative_text.strip()

    def update_character_manager(self, new_character_manager):
        """
        Updates the CharacterManager used by the NarrativeGenerator.

        Args:
            new_character_manager (CharacterManager): The new CharacterManager instance.
        """
        self.character_manager = new_character_manager

    def update_world_manager(self, new_world_manager):
        """
        Updates the WorldManager used by the NarrativeGenerator.

        Args:
            new_world_manager (WorldManager): The new WorldManager instance.
        """
        self.world_manager = new_world_manager

    def update_narrative_structuring(self, new_narrative_structuring):
        """
        Updates the NarrativeStructuring used by the NarrativeGenerator.

        Args:
            new_narrative_structuring (NarrativeStructuring): The new NarrativeStructuring instance.
        """
        self.narrative_structuring = new_narrative_structuring
