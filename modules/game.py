# Fichier game.py

#----------Import----------
import pygame
from modules.game_pages import display_game
from modules.game_logic import letter, game_difficulty, win
from modules.score import save_score
from modules.graphic_ui import end_game_screen
import time


def game(difficulty, word, username):
    """
    Start the game with Pygame loop
    """
    life = game_difficulty(difficulty)
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
                return "QUIT"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "MENU"

                # Handle letter input
                if event.unicode.isalpha() and len(event.unicode) == 1:
                    letter_input = event.unicode.lower()
                    guess, life, guessed_letters = letter(letter_input, guess, word, life, guessed_letters, difficulty)
                    

                    # Check if the game is over (Win or Lose)
                    result = win(guess, word, life, username, difficulty)
                    if result is True:
                        save_score(username, difficulty)
                        display_game(guess, life, guessed_letters, difficulty)
                        pygame.display.flip()
                        end_game_screen("WIN", word)
                        return "WIN"
                    elif result is False:
                        display_game(guess, life, guessed_letters, difficulty)
                        end_game_screen("LOSE", word)
                        return "LOSE"

    return guess
