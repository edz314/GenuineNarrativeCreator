# core/character.py

class Character:
    # ... (existing attributes and methods) ...

    def __init__(self, name: str, health: int, inventory: list = None):
        # ... (existing initialization) ...
        self.motivations = {}  # Dictionary to store motivations

    def add_motivation(self, motivation_name: str, urgency: int = 1):
        """Adds a motivation to the character."""
        self.motivations[motivation_name] = urgency

    def select_action(self, available_actions: list, game_state: dict) -> str:
        """
        Selects an action based on the character's motivations and the game state.

        Args:
            available_actions: A list of actions available to the character in the current situation.
            game_state: A dictionary representing the current state of the game.

        Returns:
            The selected action as a string.
        """
        # 1. Prioritize Motivations:
        sorted_motivations = sorted(self.motivations.items(), key=lambda item: item[1], reverse=True)

        # 2. Evaluate Actions for Each Motivation:
        for motivation, urgency in sorted_motivations:
            for action in available_actions:
                # 2.1. Check Action Feasibility (placeholder):
                if self._is_action_feasible(action, motivation, game_state):
                    # 2.2. Consider Potential Consequences (placeholder):
                    if self._are_consequences_acceptable(action, motivation, game_state):
                        return action

        # 3. Default Action (if no suitable action is found):
        return "wait"  # Or another default action

    def _is_action_feasible(self, action: str, motivation: str, game_state: dict) -> bool:
        """
        Checks if the action is feasible for the given motivation and game state.

        (You need to implement the logic based on your game's rules)
        """
        # Example:
        if action == "move_to_location" and motivation == "find_food":
            # Check if the target location has food
            return True 
        return False

    def _are_consequences_acceptable(self, action: str, motivation: str, game_state: dict) -> bool:
        """
        Checks if the potential consequences of the action are acceptable.

        (You need to implement the logic based on your game's rules)
        """
        # Example:
        if action == "attack_creature" and motivation == "protect_self":
            # Check if the player is strong enough to attack the creature
            return True
        return False
