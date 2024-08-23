# map_manager.py

import random

class MapSchema:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.terrain = [[None for _ in range(width)] for _ in range(height)]
        self.landmarks = []
        self.dynamic_elements = []
        self.metadata = {}

    def add_terrain(self, x, y, terrain_type, properties):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.terrain[y][x] = {
                'type': terrain_type,
                'properties': properties
            }
        else:
            raise ValueError("Coordinates out of bounds.")

    def add_landmark(self, x, y, name, description, importance_level):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.landmarks.append({
                'x': x,
                'y': y,
                'name': name,
                'description': description,
                'importance_level': importance_level
            })
        else:
            raise ValueError("Coordinates out of bounds.")

    def add_dynamic_element(self, x, y, element_type, properties):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.dynamic_elements.append({
                'x': x,
                'y': y,
                'type': element_type,
                'properties': properties
            })
        else:
            raise ValueError("Coordinates out of bounds.")

    def set_metadata(self, key, value):
        self.metadata[key] = value

    def get_metadata(self, key):
        return self.metadata.get(key)

    def __repr__(self):
        return f"<MapSchema name={self.name}, width={self.width}, height={self.height}>"

# Procedural map generation function
def generate_map(name, width, height, narrative_context):
    """
    Generates a map based on the narrative context and player actions.
    
    Args:
        name (str): Name of the map.
        width (int): Width of the map.
        height (int): Height of the map.
        narrative_context (dict): Information about the current narrative phase, player actions, etc.
    
    Returns:
        MapSchema: A dynamically generated map object.
    """
    # Initialize the map schema
    map_schema = MapSchema(name, width, height)
    
    # Define some basic terrain types and their properties
    terrain_types = ['forest', 'mountain', 'water', 'plain']
    terrain_properties = {
        'forest': {'movement_cost': 2, 'visibility': 0.7},
        'mountain': {'movement_cost': 3, 'visibility': 0.4},
        'water': {'movement_cost': 0, 'visibility': 0.9},  # Water is impassable
        'plain': {'movement_cost': 1, 'visibility': 1.0}
    }
    
    # Generate the terrain layout
    for y in range(height):
        for x in range(width):
            terrain_choice = random.choice(terrain_types)
            map_schema.add_terrain(x, y, terrain_choice, terrain_properties[terrain_choice])
    
    # Add landmarks based on narrative context
    if narrative_context.get('phase') == 'exploration':
        for _ in range(3):  # Add 3 landmarks
            x, y = random.randint(0, width-1), random.randint(0, height-1)
            map_schema.add_landmark(x, y, 'Ancient Ruins', 'Mysterious ruins from an ancient civilization', 'high')
    
    # Add dynamic elements based on player actions
    if narrative_context.get('recent_action') == 'combat':
        for _ in range(2):  # Add 2 combat-related dynamic elements
            x, y = random.randint(0, width-1), random.randint(0, height-1)
            map_schema.add_dynamic_element(x, y, 'Enemy Camp', {'enemy_type': 'goblins', 'strength': 5})
    
    # Set some metadata
    map_schema.set_metadata('created_by', 'Map Generator v1.0')
    
    return map_schema
