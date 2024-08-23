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
            event_manager (EventManager): Instance of the EventManager for managing game events and conditions.
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
        # Update events based on the current world state
        self.event_manager.update_events(world_state)
        
        # Determine active events that may influence the narrative
        active_events = self._get_active_events(world_state)

        narrative_structure = {
            "setup": self._create_setup(player_action, characters, world_state, active_events),
            "conflict": self._create_conflict(player_action, characters, world_state, active_events),
            "resolution": self._create_resolution(player_action, characters, world_state, active_events),
            "branching_paths": self._determine_branching_paths(player_action, characters, world_state, active_events),
            "event_triggers": self._check_event_triggers(world_state)
        }

        return narrative_structure

    def _create_setup(self, player_action, characters, world_state, active_events):
        """
        Creates the setup part of the narrative based on the input parameters.

        Args:
            player_action (str): The action performed by the player.
            characters (list): A list of characters involved in the narrative.
            world_state (dict): The current state of the game world.
            active_events (list): List of active events that might affect the setup.

        Returns:
            str: The narrative setup description.
        """
        character_name = characters[0].name
        backstory = self.lore.get_character_backstory(character_name).get('backstory', 'a mysterious past')
        world_rules = ', '.join(self.lore.get_world_rules().values())
        current_location = player_action.get('location', 'an unknown place')

        # Incorporate active events into the setup narrative
        event_descriptions = self._describe_active_events(active_events)
        setup_narrative = f"At the beginning of this scenario, {character_name}, known for {backstory}, navigates {current_location} where {world_rules} set the stage. {event_descriptions}"

        return setup_narrative

    def _create_conflict(self, player_action, characters, world_state, active_events):
        """
        Creates the conflict part of the narrative based on the input parameters.

        Args:
            player_action (str): The action performed by the player.
            characters (list): A list of characters involved in the narrative.
            world_state (dict): The current state of the game world.
            active_events (list): List of active events that might affect the conflict.

        Returns:
            str: The narrative conflict description.
        """
        character_name = characters[0].name
        motivation = self.lore.get_character_backstory(character_name).get('motivations', ['personal gain'])[0]
        opposing_force = self._identify_opposing_force(player_action, characters, world_state)

        # Modify conflict based on active events
        if 'natural_disaster' in active_events:
            conflict_narrative = f"The action taken by {character_name} is interrupted by a raging storm, forcing them into a conflict with {opposing_force}, all while trying to survive the disaster."
        else:
            conflict_narrative = f"The action taken by {character_name} brings them into conflict with {opposing_force}, driven by their motivation for {motivation}."

        return conflict_narrative

    def _create_resolution(self, player_action, characters, world_state, active_events):
        """
        Creates the resolution part of the narrative based on the input parameters.

        Args:
            player_action (str): The action performed by the player.
            characters (list): A list of characters involved in the narrative.
            world_state (dict): The current state of the game world.
            active_events (list): List of active events that might affect the resolution.

        Returns:
            str: The narrative resolution description.
        """
        character_name = characters[0].name
        resolution_event = world_state.get('resolution_conditions', 'an unexpected turn')
        world_rules = ', '.join(self.lore.get_world_rules().values())

        # Adjust resolution based on active events
        if 'natural_disaster' in active_events:
            resolution_narrative = f"As {character_name} fights to overcome {resolution_event}, they must also contend with the devastation left by the storm. The world’s rules seem more fragile than ever."
        else:
            resolution_narrative = f"The conflict resolves as {character_name} encounters {resolution_event}, all under the shadow of the world’s rules: {world_rules}."

        return resolution_narrative

    def _determine_branching_paths(self, player_action, characters, world_state, active_events):
        """
        Determines possible branching paths in the narrative based on player actions and current state.

        Args:
            player_action (str): The action performed by the player.
            characters (list): A list of characters involved in the narrative.
            world_state (dict): The current state of the game world.
            active_events (list): List of active events that might affect the narrative paths.

        Returns:
            list: Possible narrative paths that can be taken next.
        """
        if 'natural_disaster' in active_events:
            return ['find_shelter', 'help_survivors', 'escape_area']
        elif player_action.get('type') == 'explore':
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

    def _get_active_events(self, world_state):
        """
        Retrieves a list of currently active events from the EventManager.

        Args:
            world_state (dict): The current state of the game world.

        Returns:
            list: A list of active events.
        """
        active_events = []
        for event_name in self.event_manager.events:
            if self.event_manager.check_event(event_name, world_state):
                active_events.append(event_name)
        return active_events

    def _describe_active_events(self, active_events):
        """
        Generates a description of the active events to be included in the narrative.

        Args:
            active_events (list): List of active events that are currently affecting the game world.

        Returns:
            str: A textual description of the active events.
        """
        descriptions = {
            'natural_disaster': "A storm rages on the horizon, threatening the lands.",
            'festival': "The sounds of a distant festival fill the air, bringing a sense of joy and celebration."
        }
        return " ".join(descriptions[event] for event in active_events if event in descriptions)
