import pygame
from narrative.generation.narrative_generator import NarrativeGenerator
from narrative.generation.narrative_structuring import NarrativeStructuring
from narrative.generation.character_manager import CharacterManager
from core.data_management.world_manager import WorldManager
from core.utils.data_loading import load_game_data
from core.integration.game_integration.pygame_integration import PygameIntegration  # Assuming Pygame integration
from core.utils.logging import setup_logging
from narrative.generation.action_executor import ActionExecutor


def handle_events():
    """Handles Pygame events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False  # Signal to exit the game
        # Handle more events here (e.g., key presses, mouse clicks)
    return True


def process_player_input(pygame_integration, logger):
    """Processes player input."""
    player_input = pygame_integration.handle_input()
    if player_input:
        logger.debug("Player Input: %s", player_input)
    return player_input


def initialize_game():
    """Initializes the game components."""
    # Setup Logging
    logger = setup_logging()
    logger.info("Starting Genuine Narrative Game")

    try:
        # Load Game Data
        game_data = load_game_data("data/world_data.yaml")  # Update path if needed
    except FileNotFoundError as e:
        logger.error("Failed to load game data: %s", e)
        raise

    # Initialize Core Modules
    narrative_structuring = NarrativeStructuring()
    character_manager = CharacterManager(game_data["characters"])
    world_manager = WorldManager(game_data["world"])
    narrative_generator = NarrativeGenerator(narrative_structuring, character_manager, world_manager)

    # Initialize Pygame Integration (or other integrations)
    pygame_integration = PygameIntegration()

    return logger, narrative_generator, pygame_integration


def main():
    logger, narrative_generator, pygame_integration = initialize_game()

    # Game Initialization
    current_location = "forest"  # Starting location
    player_action = ""

    # Main Game Loop
    running = True
    while running:
        # Handle Events
        running = handle_events()

        if not running:
            break  # Exit the loop if the quit event was triggered

        # Process Player Input
        player_action = process_player_input(pygame_integration, logger)

        # Generate Narrative
        if player_action:
            try:
                narrative_text = narrative_generator.generate_narrative(player_action, current_location)
                logger.info("Narrative Generated: %s", narrative_text)
                pygame_integration.display_narrative(narrative_text)
            except Exception as e:
                logger.error("Failed to generate narrative: %s", e)

        # Refresh the game display (Add any display update logic here)
        pygame.display.update()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")

