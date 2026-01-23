# Fichier games_pages.py

import pygame
from modules.game_logic import games_difficulty


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
RED = (180, 50, 50)


# Background 
background_game = pygame.image.load("modules/graphic/assets/background_game.png").convert()
background_game = pygame.transform.scale(background_game, (WIDHT, HEIGHT))


# Load Character Assets
# Using a dictionary to map number of mistakes (7 - life) to the image name part

# Difficulty 0 (Character 1 - Basic Stickman)
char1_imgs = {}
try:
    char1_imgs[1] = pygame.image.load("modules/graphic/assets/character 1/Head 1.png")
    char1_imgs[2] = pygame.image.load("modules/graphic/assets/character 1/body 1.png")
    char1_imgs[3] = pygame.image.load("modules/graphic/assets/character 1/armL 1.png")
    char1_imgs[4] = pygame.image.load("modules/graphic/assets/character 1/armR 1.png")
    char1_imgs[5] = pygame.image.load("modules/graphic/assets/character 1/footL 1.png")
    char1_imgs[6] = pygame.image.load("modules/graphic/assets/character 1/footR 1.png")
    char1_imgs[7] = pygame.image.load("modules/graphic/assets/character 1/weapon 1.png")  
    # Scaling if necessary
except FileNotFoundError:
    print("Error loading Character 1 assets")

# Difficulty 1 & 2 (Character 2 - Advanced Character)
char2_imgs = {}
try:
    char2_imgs[1] = pygame.image.load("modules/graphic/assets/character 2/head 2.png")
    char2_imgs[2] = pygame.image.load("modules/graphic/assets/character 2/body 2.png")
    char2_imgs[3] = pygame.image.load("modules/graphic/assets/character 2/armL 2.png")
    char2_imgs[4] = pygame.image.load("modules/graphic/assets/character 2/armR 2.png")
    char2_imgs[5] = pygame.image.load("modules/graphic/assets/character 2/footL 2.png")
    char2_imgs[6] = pygame.image.load("modules/graphic/assets/character 2/footR 2.png")
    char2_imgs[7] = pygame.image.load("modules/graphic/assets/character 2/weapon 2.png")
except FileNotFoundError:
    print("Error loading Character 2 assets")


# Function to display the game state
def display_game(guess, life, guessed_letters, difficulty):
    """
    Renders the current game state to the screen.

    Draws the background, the hangman character based on remaining lives,
    the list of used letters, and the current state of the secret word.

    Args:
        guess (list): The list of characters representing the current guess state (letters or underscores).
        life (int): The number of lives remaining.
        guessed_letters (list): A list of all letters guessed so far.
        difficulty (int): The selected difficulty level, used to choose the character assets.
    """
    window = screen
    # Use global font setup if possible, or init here. 
    # Better to init font once outside, but keeping local for now as per minimal change strategy unless performance hit.
    font = pygame.font.SysFont("Arial", 40)
    small_font = pygame.font.SysFont("Arial", 25)

    window.blit(background_game, (0,0))
    
    # --- Draw Character ---
    max_lives = games_difficulty(difficulty)
    mistakes = max_lives - life
    
    imgs_to_use = char1_imgs if difficulty == 0 else char2_imgs
    
    # Position for character 
    char_x = center_x - 300
    char_y = center_y - 150
    
    # Blit all parts up to current mistakes
    for i in range(1, mistakes + 1):
        if i in imgs_to_use:
            rect = imgs_to_use[i].get_rect(center=(char_x, char_y)) 
            window.blit(imgs_to_use[i], rect)


    # --- Draw Guessed Letters ---
    guessed_str = " ".join(guessed_letters)
    guessed_text = small_font.render(f"Letters: {guessed_str}", True, BLACK)
    window.blit(guessed_text, (20, 20))
    
    # --- Draw Lives ---
    life_text = small_font.render(f"Lives: {life}", True, RED)
    window.blit(life_text, (WIDHT - 150, 20))

    # Render the guessed word
    for index, letter in enumerate(guess):
        text = font.render(f"{letter}", True, BLACK)
        # Position text: centered horizontally, spaced vertically
        text_rect = text.get_rect(center=((center_x - 55) - (len(guess) * 50) // 2 + index * 50, (center_y + 180)))
        window.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)