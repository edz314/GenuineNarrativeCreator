# core/data_management/character_manager.py

class Character:
    """
    Represents a character in the game, with attributes and methods for interaction and state management.
    """
    
    def __init__(self, name, traits, location=None):
        """
        Initializes a Character with a name, traits, and optional starting location.
        
        Args:
            name (str): The name of the character.
            traits (dict): A dictionary of character traits (e.g., 'brave', 'cunning').
            location (Location, optional): The starting location of the character.
        """
        self.name = name
        self.traits = traits
        self.location = location
        self.health = 100  # Default health value
        self.mood = 'neutral'  # Default mood state
        self.relationships = {}  # Track relationships with other characters

    def interact_with(self, other_character):
        """
        Defines how this character interacts with another character.
        
        Args:
            other_character (Character): The other character to interact with.
        """
        # Example interaction logic
        if self.traits.get('friendly'):
            print(f"{self.name} greets {other_character.name} warmly.")
        else:
            print(f"{self.name} is suspicious of {other_character.name}.")

    def update_state(self, event_name):
        """
        Updates the character's state based on a specific event.
        
        Args:
            event_name (str): The name of the event affecting the character.
        """
        # Example: Adjust character's mood based on event
        if event_name == 'natural_disaster':
            self.mood = 'anxious'
            print(f"{self.name} feels anxious due to the natural disaster.")
        elif event_name == 'festival':
            self.mood = 'joyful'
            print(f"{self.name} is joyful because of the festival.")

    def update_health(self, amount):
        """
        Updates the character's health.
        
        Args:
            amount (int): The amount to adjust health by (can be positive or negative).
        """
        self.health += amount
        if self.health > 100:
            self.health = 100
        elif self.health <= 0:
            self.health = 0
            print(f"{self.name} has perished.")

    def change_location(self, new_location):
        """
        Changes the character's current location.
        
        Args:
            new_location (Location): The new location where the character will be.
        """
        self.location = new_location
        print(f"{self.name} has moved to {new_location.name}.")

    def adjust_relationship(self, other_character_name, change):
        """
        Adjusts the relationship value with another character.
        
        Args:
            other_character_name (str): The name of the other character.
            change (int): The amount to adjust the relationship value by.
        """
        if other_character_name not in self.relationships:
            self.relationships[other_character_name] = 0
        self.relationships[other_character_name] += change

        # Print updated relationship status for debugging
        print(f"{self.name}'s relationship with {other_character_name} is now {self.relationships[other_character_name]}.")

    def __repr__(self):
        return f"<Character(name={self.name}, health={self.health}, mood={self.mood}, location={self.location})>"

# Example usage of the Character class with events

# Instantiate the EventManager
event_manager = EventManager()

# Create characters
alice = Character(name="Alice", traits={"friendly": True})
bob = Character(name="Bob", traits={"hostile": True})

# Characters interacting
alice.interact_with(bob)  # Alice greets Bob warmly.
bob.interact_with(alice)  # Bob is suspicious of Alice.

# Update character states based on events
alice.update_state('festival')
bob.update_state('natural_disaster')

# Update character health
alice.update_health(-20)  # Alice loses 20 health points.
bob.update_health(-50)    # Bob loses 50 health points.

# Adjust relationships
alice.adjust_relationship("Bob", 10)  # Alice's relationship with Bob improves.
bob.adjust_relationship("Alice", -5)  # Bob's relationship with Alice worsens.

# Change locations (assuming locations are defined elsewhere)
# alice.change_location(some_location)
# bob.change_location(another_location)
