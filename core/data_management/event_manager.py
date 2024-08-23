# core/narrative_generation/event_manager.py

class EventManager:
    """
    Manages game events and their triggers. Allows checking for specific conditions or events that
    may influence the narrative or gameplay.
    """

    def __init__(self):
        """
        Initializes the EventManager with an empty list of events.
        """
        self.events = {}

    def register_event(self, event_name, conditions, effects):
        """
        Registers a new event with specified conditions and effects.

        Args:
            event_name (str): Name of the event.
            conditions (function): A function that checks if the event conditions are met.
            effects (function): A function that defines the effects of the event if it is triggered.
        """
        self.events[event_name] = {
            'conditions': conditions,
            'effects': effects,
            'active': False
        }

    def update_events(self, world_state):
        """
        Updates the status of all registered events based on the current world state.

        Args:
            world_state (dict): The current state of the game world.
        """
        for event_name, event_data in self.events.items():
            if event_data['conditions'](world_state):
                event_data['active'] = True
                event_data['effects'](world_state)
            else:
                event_data['active'] = False

    def check_event(self, event_name, world_state):
        """
        Checks if a specific event is active based on the current world state.

        Args:
            event_name (str): The name of the event to check.
            world_state (dict): The current state of the game world.

        Returns:
            bool: True if the event is active, False otherwise.
        """
        if event_name in self.events:
            return self.events[event_name]['active']
        return False

    def trigger_event_effects(self, event_name, world_state):
        """
        Triggers the effects of a specific event if it is active.

        Args:
            event_name (str): The name of the event to trigger effects for.
            world_state (dict): The current state of the game world.

        Returns:
            None
        """
        if self.check_event(event_name, world_state):
            self.events[event_name]['effects'](world_state)
