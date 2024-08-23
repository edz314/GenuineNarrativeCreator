# narrative/generation/Narrative_structuring.py

class NarrativeStructuring:
    """
    Handles the structuring of the narrative, determining how elements such as setup, conflict, and resolution
    are arranged based on the current game state, player actions, and probabilistic factors.
    """

    def __init__(self, lore, map_manager, event_manager):
        """
        Initializes the NarrativeStructuring component.

        Args:
            lore (Lore): Instance of the Lore class for accessing world and character information.
            map_manager (MapManager): Instance of the MapManager for accessing and generating maps.
            event_manager (EventManager): Instance of an EventManager for managing game events and conditions.
        """
        self.lore = lore
        self.map_manager = map_manager
        self.event_manager = event_manager

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
            "resolution": self._create_resolution(player_action, characters, world_state),
            "branching_paths": self._determine_branching_paths(player_action, characters, world_state),
            "event_triggers": self._check_event_triggers(world_state)
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
        character_name = characters[0].name
        backstory = self.lore.get_character_backstory(character_name).get('backstory', 'a mysterious past')
        world_rules = ', '.join(self.lore.get_world_rules().values())
        current_location = player_action.get('location', 'an unknown place')

        return f"At the beginning of this scenario, {character_name}, known for {backstory}, navigates {current_location} where {world_rules} set the stage."

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
        character_name = characters[0].name
        motivation = self.lore.get_character_backstory(character_name).get('motivations', ['personal gain'])[0]
        opposing_force = self._identify_opposing_force(player_action, characters, world_state)

        return f"The action taken by {character_name} brings them into conflict with {opposing_force}, driven by their motivation for {motivation}."

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
        character_name = characters[0].name
        resolution_event = world_state.get('resolution_conditions', 'an unexpected turn')
        world_rules = ', '.join(self.lore.get_world_rules().values())

        return f"The conflict resolves as {character_name} encounters {resolution_event}, all under the shadow of the world’s rules: {world_rules}."

    def _determine_branching_paths(self, player_action, characters, world_state):
        """
        Determines possible branching paths in the narrative based on player actions and current state.

        Args:
            player_action (str): The action performed by the player.
            characters (list): A list of characters involved in the narrative.
            world_state (dict): The current state of the game world.

        Returns:
            list: Possible narrative paths that can be taken next.
        """
        # Example logic for branching paths
        if player_action.get('type') == 'explore':
            return ['discover_ancient_ruin', 'find_hidden_treasure']
        elif player_action.get('type') == 'combat':
            return ['defeat_enemy', 'retreat_and_regroup']
        else:
            return ['continue_journey', 'seek_allies']

    def _check_event_triggers(self, world_state):
        """
        Checks for specific conditions or events in the game world that may affect the narrative.

        Args:
            world_state (dict): The current state of the game world.

        Returns:
            list: A list of event triggers and their effects on the narrative.
        """
        triggers = []
        if self.event_manager.check_event('natural_disaster', world_state):
            triggers.append('natural_disaster')
        if self.event_manager.check_event('festival', world_state):
            triggers.append('festival')
        return triggers

    def _identify_opposing_force(self, player_action, characters, world_state):
        """
        Identifies the opposing force in a conflict based on the current context.

        Args:
            player_action (str): The action performed by the player.
            characters (list): A list of characters involved in the narrative.
            world_state (dict): The current state of the game world.

        Returns:
            str: The name or description of the opposing force.
        """
        # Example logic for identifying opposing forces
        if 'enemy' in player_action:
            return player_action['enemy']
        else:
            return 'an unknown adversary'

