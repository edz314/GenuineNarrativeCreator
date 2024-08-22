# core/narrative_generation/world_manager.py

from core.world import World, Location

class WorldManager:
    """
    Manages the game world, including locations, their descriptions, and potential interactions.
    """

    def __init__(self, world_data: dict):
        """Initializes the WorldManager with world data."""
        self.world = self._create_world_from_data(world_data)

    def _create_world_from_data(self, world_data: dict) -> World:
        """Creates a World object from the provided data."""
        locations = {}
        for location_name, location_data in world_data["locations"].items():
            locations[location_name] = Location(
                name=location_name,
                description=location_data["description"],
                connections=location_data.get("connections", []),
                creatures=location_data.get("creatures", []),
                items=location_data.get("items", [])
            )
        return World(locations)

    def get_location_details(self, location_name: str) -> Location:
        """Retrieves details about a specific location."""
        return self.world.locations.get(location_name)

    def move_player(self, player: Character, new_location_name: str):
        """Moves the player to a new location."""
        new_location = self.get_location_details(new_location_name)
        if new_location:
            player.location = new_location  # Assuming Character class has a 'location' attribute
            print(f"{player.name} has moved to {new_location.name}.") # Placeholder for narrative 
        else:
            print(f"Error: Location '{new_location_name}' not found.")

    # Add other world manipulation methods as needed 
    # ...
