class NarrativeStructuring:
    """
    Handles the structuring of the narrative, determining how elements such as setup, conflict, and resolution
    are arranged based on the current game state, player actions, and probabilistic factors.
    """

    def __init__(self, lore):
        """
        Initializes the NarrativeStructuring component.

        Args:
            lore (Lore): Instance of the Lore class for accessing world and character information.
        """
        self.lore = lore

    def create_structure(self, player_action, characters, world_state):
        """
        Creates a narrative structure based on player action, characters involved, and the current state of the world.

        Args:
            player_action (str): The action performed by the player.
            characters (list): A list of characters involved in the narrative.
            world_state (dict): The current state of the game world.

        Returns:
            dict: A dictionary representing the structured narrative elements.
        """
        narrative_structure = {
            "setup": self._create_setup(player_action, characters, world_state),
            "conflict": self._create_conflict(player_action, characters, world_state),
            "resolution": self._create_resolution(player_action, characters, world_state)
        }

        return narrative_structure

    def _create_setup(self, player_action, characters, world_state):
        """
        Creates the setup part of the narrative based on the input parameters.

        Args:
            player_action (str): The action performed by the player.
            characters (list): A list of characters involved in the narrative.
            world_state (dict): The current state of the game world.

        Returns:
            str: The narrative setup description.
        """
        # Use lore to enhance the setup
        character_name = characters[0].name
        backstory = self.lore.get_character_backstory(character_name).get('backstory', 'a mysterious past')
        world_rules = ', '.join(self.lore.get_world_rules().values())

        return f"At the beginning of this scenario, {character_name}, known for {backstory}, navigates a world where {world_rules} set the stage."

    def _create_conflict(self, player_action, characters, world_state):
        """
        Creates the conflict part of the narrative based on the input parameters.

        Args:
            player_action (str): The action performed by the player.
            characters (list): A list of characters involved in the narrative.
            world_state (dict): The current state of the game world.

        Returns:
            str: The narrative conflict description.
        """
        # Example: Introduce conflict considering lore-based motivations
        character_name = characters[0].name
        motivation = self.lore.get_character_backstory(character_name).get('motivations', ['personal gain'])[0]

        return f"The action taken by the player brings {character_name} into direct conflict with another, driven by their motivation for {motivation}."

    def _create_resolution(self, player_action, characters, world_state):
        """
        Creates the resolution part of the narrative based on the input parameters.

        Args:
            player_action (str): The action performed by the player.
            characters (list): A list of characters involved in the narrative.
            world_state (dict): The current state of the game world.

        Returns:
            str: The narrative resolution description.
        """
        # Example: Use world rules and past events to craft a resolution
        character_name = characters[0].name
        resolution_event = world_state.get('resolution_conditions', 'an unexpected turn')
        world_rules = ', '.join(self.lore.get_world_rules().values())

        return f"The conflict resolves as {character_name} encounters {resolution_event}, all under the shadow of the world’s rules: {world_rules}."
