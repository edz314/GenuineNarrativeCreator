# core/game_integration/pygame_integration.py

import pygame

class PygameIntegration:
    """
    Handles the integration of the narrative game with the Pygame library for display and input.
    """

    def __init__(self, screen_width=800, screen_height=600, font_size=24):
        """
        Initializes Pygame and sets up the display and font.

        Args:
            screen_width: The width of the game window.
            screen_height: The height of the game window.
            font_size: The font size for displaying text.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Genuine Narrative Game")
        self.font = pygame.font.Font(None, font_size)

    def display_text(self, text: str, color=(255, 255, 255), y_position=10):
        """
        Displays text on the Pygame screen.

        Args:
            text: The text to display.
            color: The color of the text (RGB tuple).
            y_position: The vertical position of the text on the screen.
        """
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, y_position)  # Position text with a margin
        self.screen.blit(text_surface, text_rect)

    def clear_screen(self):
        """
        Clears the Pygame screen with a black background.
        """
        self.screen.fill((0, 0, 0))

    def update_display(self):
        """
        Updates the Pygame display.
        """
        pygame.display.flip()

    def handle_input(self) -> str:
        """
        Handles player input events in Pygame.

        Returns:
            The player's input as a string (e.g., a command or choice).
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # Example: Press Enter to confirm input
                    # Get player input from a text input box (not implemented here)
                    player_input = "get_input_from_text_box()" 
                    return player_input

        return "" # Return empty string if no input is received

    # Add more methods for handling specific Pygame interactions (e.g., button clicks, mouse events)
    # ... 
