import pygame
import time


# Init 
pygame.init()
clock = pygame.time.Clock()


# Window Size
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.NOFRAME)
WIDHT, HEIGHT = screen.get_size()

center_x = WIDHT // 2
center_y = HEIGHT // 2

# Constant
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (50, 100, 200)
RED = (180, 50, 50)
GREEN = (0, 255, 78)
YELLOW = (255, 255, 0, 255)



# Function to display the game state
def display_game(guess):
    """
    Render the game state to the screen.
    Includes the guessed word.
    """
    window = screen
    # Use global font setup if possible, or init here. 
    # Better to init font once outside, but keeping local for now as per minimal change strategy unless performance hit.
    font = pygame.font.SysFont("Arial", 40)

    window.fill(WHITE)
    
    # Render the guessed word
    for index, letter in enumerate(guess):
        text = font.render(f"{letter}", True, BLACK)
        # Position text: centered horizontally, spaced vertically
        # center_x - (half total width) + (offset for current letter)
        text_rect = text.get_rect(center=(center_x - (len(guess) * 50) // 2 + index * 50, center_y))
        window.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)