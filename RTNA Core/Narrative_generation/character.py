# core/character.py

class Character:
    """
    Represents a character in the game, including the player and NPCs.
    """

    def __init__(self, name: str, health: int, inventory: list = None):
        """Initializes a Character object."""
        self.name = name
        self.health = health
        self.inventory = inventory or []  # Initialize inventory as an empty list if not provided
        self.location = None  # Add location attribute to track character's current location
        # Add other stats as needed (strength, intelligence, etc.)

    def __str__(self):
        """Returns a string representation of the character."""
        return f"{self.name} (Health: {self.health}, Inventory: {self.inventory})"

    def change_stat(self, stat_name: str, amount: int):
        """Changes a character stat by the given amount."""
        if hasattr(self, stat_name):
            setattr(self, stat_name, getattr(self, stat_name) + amount)

    def is_alive(self) -> bool:
        """Checks if the character is alive."""
        return self.health > 0
