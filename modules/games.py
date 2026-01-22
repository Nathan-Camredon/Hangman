#----------Import----------
import pygame
from modules.games_pages import display_game
from modules.game_logic import letter, games_difficulty, win
import time

def games(difficulty, word):
    """
    Start the game with Pygame loop
    """
    life = games_difficulty(difficulty)
    guessed_letters = []
    guess = ["_"] * len(word)
    
    running = True
    while running:
        # Display the game state
        display_game(guess, life, guessed_letters, difficulty)
        
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return # Exit function
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    return

                # Handle letter input
                if event.unicode.isalpha() and len(event.unicode) == 1:
                    letter_input = event.unicode.lower()
                    guess, life, guessed_letters = letter(letter_input, guess, word, life, guessed_letters, difficulty)
                    
                    # Check Win/Lose condition
                    result = win(guess, word, life)
                    if result is True:
                        display_game(guess, life, guessed_letters, difficulty)
                        time.sleep(2)
                        running = False
                    elif result is False:
                        display_game(guess, life, guessed_letters, difficulty)
                        time.sleep(2)
                        running = False

    return guess
