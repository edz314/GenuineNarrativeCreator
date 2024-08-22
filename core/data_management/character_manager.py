# character_manager.py

class CharacterManager:
    def __init__(self, characters_data):
        """
        Initialize the CharacterManager with character data.
        
        Args:
            characters_data (dict): A dictionary containing character data.
        """
        self.characters = self._initialize_characters(characters_data)

    def _initialize_characters(self, characters_data):
        """
        Initialize characters from the provided data.
        
        Args:
            characters_data (dict): Raw character data to initialize the characters.
        
        Returns:
            dict: A dictionary of character objects.
        """
        characters = {}
        for character_name, character_info in characters_data.items():
            characters[character_name] = Character(character_name, character_info)
        return characters

    def get_character(self, character_name):
        """
        Retrieve a character by name.
        
        Args:
            character_name (str): The name of the character to retrieve.
        
        Returns:
            Character: The character object corresponding to the name.
        """
        return self.characters.get(character_name)

    def update_character(self, character_name, new_info):
        """
        Update the information for a character.
        
        Args:
            character_name (str): The name of the character to update.
            new_info (dict): New data to update the character with.
        """
        if character_name in self.characters:
            self.characters[character_name].update_info(new_info)

# Example Character class
class Character:
    def __init__(self, name, info):
        """
        Initialize a Character with a name and additional info.
        
        Args:
            name (str): The character's name.
            info (dict): Additional information about the character.
        """
        self.name = name
        self.info = info

    def update_info(self, new_info):
        """
        Update the character's information.
        
        Args:
            new_info (dict): New information to update the character with.
        """
        self.info.update(new_info)
