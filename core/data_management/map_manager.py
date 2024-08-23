# map_manager.py

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
