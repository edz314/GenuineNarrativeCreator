# main.py

import pygame
from core.narrative_generator import NarrativeGenerator
from core.narrative_structuring import NarrativeStructuring
from core.character_manager import CharacterManager
from core.world_manager import WorldManager
from utils.data_loading import load_game_data
from core.game_integration.pygame_integration import PygameIntegration # Assuming Pygame integration
from utils.logging import setup_logging
from core.action_executor import ActionExecutor

def main():
    # 1. Setup Logging
    logger = setup_logging() 
    logger.info("Starting Genuine Narrative Game")

    # 2. Load Game Data 
    game_data = load_game_data("data/world_data.yaml") # Update path if needed

    # 3. Initialize Core Modules
    narrative_structuring = NarrativeStructuring()
    character_manager = CharacterManager(game_data["characters"])
    world_manager = WorldManager(game_data["world"])
    narrative_generator = NarrativeGenerator(narrative_structuring, character_manager, world_manager)

    # 4. Initialize Pygame Integration (or other integrations)
    pygame_integration = PygameIntegration()

    # 5. Game Initialization
    current_location = "forest"  # Starting location
    player_action = ""

    # 6. Main Game Loop
    running = True
    while running:
        # 6.1. Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # ... Add other event handling (key presses, etc.)

        # 6.2. Get Player Input (replace with your Pygame input logic)
        player_input = pygame_integration.handle_input()
        if player_input:
            player_action = player_input
            logger.debug("Player Input: %s", player_action)

        # 6.3. Generate Narrative
        if player_action:
            narrative_text = narrative_generator.generate_narrative(player_action, current_location)
            logger.debug("Generated Narrative: %s", narrative_text)

            # 6.4. Display Narrative
            pygame_integration.clear_screen()
            pygame_integration.display_text(narrative_text)
            pygame_integration.update_display()

            # 6.5. Process Player Action (Update game state based on action)
            # ... (Update current_location, character stats, etc. based on player_action) 
            player_action = "" # Reset player action

            # 6.6 Initialize EscalationManager
            escalation_manager = EscalationManager(human_operator_available=True)  
        
            # 6.7 Initialize NarrativeGenerator (pass escalation_manager)
            narrative_generator = NarrativeGenerator(narrative_structuring, character_manager, world_manager, escalation_manager)
            
            # 6.8 Initialize ActionExecutor
            action_executor = ActionExecutor(character_manager, world_manager, narrative_generator)
                
        # Get available actions (you need to implement this logic based on game state)
        available_actions = get_available_actions(player, current_location)  

        # Select an action for the player
        selected_action = player.select_action(available_actions, game_state)

        # Execute the selected action
        action_executor.execute_action(player, selected_action, game_state)
        
        )
    
    # 7. Game Cleanup 
    pygame.quit()
    logger.info("Exiting Game")

if __name__ == "__main__":
    main()
