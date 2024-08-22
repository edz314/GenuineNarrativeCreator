# core/action_executor.py

class ActionExecutor:
    """
    Executes character actions and updates the game state.
    """

    def __init__(self, character_manager, world_manager, narrative_generator):
        """Initializes the ActionExecutor."""
        self.character_manager = character_manager
        self.world_manager = world_manager
        self.narrative_generator = narrative_generator

    def execute_action(self, character: Character, action: str, game_state: dict):
        """
        Executes the given action for the character.

        Args:
            character: The character performing the action.
            action: The action to be performed.
            game_state: A dictionary representing the current state of the game.
        """
        if action == "move_to_location":
            target_location = game_state.get("target_location")  # Get target location from game state
            if target_location:
                self.world_manager.move_player(character, target_location)  
                # Add narrative for the move
                print(self.narrative_generator.generate_narrative(action, target_location))
        elif action == "attack_creature":
            # Implement attack logic here (update health, etc.)
            print(f"{character.name} attacks the creature!")  # Placeholder
        # ... Add logic for other action types ...
