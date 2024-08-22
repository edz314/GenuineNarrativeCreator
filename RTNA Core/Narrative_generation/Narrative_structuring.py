class NarrativeStructuring:
    """
    Handles the structuring of narratives, defining the flow of events and how they are presented.
    """

    def __init__(self):
        """
        Initializes the NarrativeStructuring object.
        """
        self.default_structure = {
            'setup': "The scene is set.",
            'conflict': "A challenge arises.",
            'resolution': "The situation is resolved."
        }

    def create_structure(self, player_action, characters, world_state):
        """
        Creates a narrative structure based on player action, characters, and world state.

        Args:
            player_action (str): The action performed by the player.
            characters (list): The list of characters involved in the narrative.
            world_state (dict): The current state of the world/environment.

        Returns:
            dict: A structured narrative dict with elements like setup, conflict, and resolution.
        """
        structure = {}

        # Determine the setup based on the world state and player action
        structure['setup'] = self._generate_setup(player_action, world_state)

        # Create a conflict based on the player action and characters
        structure['conflict'] = self._generate_conflict(player_action, characters, world_state)

        # Determine the resolution based on the outcome or potential outcomes of the action
        structure['resolution'] = self._generate_resolution(player_action, characters, world_state)

        return structure

    def _generate_setup(self, player_action, world_state):
        """
        Generates the setup portion of the narrative based on the world state and player action.

        Args:
            player_action (str): The action performed by the player.
            world_state (dict): The current state of the world/environment.

        Returns:
            str: The setup text.
        """
        # Example logic: The setup could depend on the time of day or the current location
        location = world_state.get('location', 'an unknown place')
        time_of_day = world_state.get('time_of_day', 'daytime')

        setup_text = f"The player finds themselves in {location} during {time_of_day}."
        return setup_text

    def _generate_conflict(self, player_action, characters, world_state):
        """
        Generates the conflict portion of the narrative based on the player action and characters.

        Args:
            player_action (str): The action performed by the player.
            characters (list): The list of characters involved in the narrative.
            world_state (dict): The current state of the world/environment.

        Returns:
            str: The conflict text.
        """
        # Example logic: Conflict could arise based on an interaction with a character or a challenge in the environment
        if characters:
            main_character = characters[0].name  # Assuming the first character is the primary one
            conflict_text = f"{main_character} opposes the player's decision to {player_action}."
        else:
            conflict_text = f"The player's action to {player_action} causes a disturbance in the environment."

        return conflict_text

    def _generate_resolution(self, player_action, characters, world_state):
        """
        Generates the resolution portion of the narrative based on the player action and characters.

        Args:
            player_action (str): The action performed by the player.
            characters (list): The list of characters involved in the narrative.
            world_state (dict): The current state of the world/environment.

        Returns:
            str: The resolution text.
        """
        # Example logic: The resolution could depend on the success or failure of the player's action
        success_chance = world_state.get('success_chance', 0.5)  # Default success chance is 50%
        resolution = "successfully" if success_chance > 0.5 else "unsuccessfully"

        if characters:
            main_character = characters[0].name  # Assuming the first character is the primary one
            resolution_text = f"{main_character} helps the player to {resolution} complete the action."
        else:
            resolution_text = f"The player {resolution} completes the action."

        return resolution_text

    def update_default_structure(self, new_structure):
        """
        Updates the default narrative structure used as a fallback.

        Args:
            new_structure (dict): A dictionary containing the new default structure.
        """
        if isinstance(new_structure, dict):
            self.default_structure.update(new_structure)
        else:
            raise ValueError("New structure must be a dictionary.")

    def apply_custom_structure(self, custom_structure, player_action, characters, world_state):
        """
        Applies a custom narrative structure instead of the default one.

        Args:
            custom_structure (dict): The custom narrative structure to apply.
            player_action (str): The action performed by the player.
            characters (list): The list of characters involved in the narrative.
            world_state (dict): The current state of the world/environment.

        Returns:
            dict: A structured narrative dict based on the custom structure.
        """
        structure = {}

        for key, value in custom_structure.items():
            if callable(value):
                structure[key] = value(player_action, characters, world_state)
            else:
                structure[key] = value

        return structure

    def reset_structure(self):
        """
        Resets the narrative structure to its default state.
        """
        self.default_structure = {
            'setup': "The scene is set.",
            'conflict': "A challenge arises.",
            'resolution': "The situation is resolved."
        }
