# core/utils/data_loading.py

import yaml

def load_game_data(file_path: str) -> dict:
    """
    Loads game data from a YAML file.

    Args:
        file_path: The path to the YAML file containing the game data.

    Returns:
        A dictionary containing the loaded game data.
    """

    try:
        with open(file_path, 'r') as file:
            game_data = yaml.safe_load(file)
        return game_data
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return {}  # Return an empty dictionary if file not found
    except yaml.YAMLError as e:
        print(f"Error loading YAML file: {e}")
        return {} 
