# core/narrative_generation/world_manager.py

from core.world import World, Location

class WorldManager:
    """
    Manages the game world, including locations, their descriptions, and potential interactions.
    """

    def __init__(self, world_data: dict):
        """
        Initializes the WorldManager with world data.

        Args:
            world_data: A dictionary containing data about the game world.
        """
        self.world = self._create_world_from_data(world_data)

    def _create_world_from_data(self, world_data: dict) -> World:
        """
        Creates a World object from the provided data.

        Args:
            world_data: A dictionary containing world data.

        Returns:
            A World object representing the game world.
        """

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
        """
        Retrieves details about a specific location.

        Args:
            location_name: The name of the location.

        Returns:
            A Location object representing the specified location.
        """
        return self.world.locations.get(location_name)

    # Add methods for world manipulation, like moving characters, changing location states, etc.
    # ... 
