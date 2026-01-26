#----------Import----------
import pygame
from modules.games_pages import display_game
from modules.game_logic import letter, games_difficulty, win
from modules.score import ask_username, save_score
import time

<<<<<<< Updated upstream:modules/games.py
def games(difficulty, word):
=======
def game(difficulty, word, username):
>>>>>>> Stashed changes:modules/game.py
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
                    
<<<<<<< Updated upstream:modules/games.py
                    # Check Win/Lose condition
                    result = win(guess, word, life)
=======
                    # Check if the game is over (Win or Lose)
                    result = win(guess, word, life, username, difficulty)
>>>>>>> Stashed changes:modules/game.py
                    if result is True:
                        display_game(guess, life, guessed_letters, difficulty)
                        
                        # Handle Score
                        current_username = ask_username()
                        save_score(current_username, difficulty)
                        
                        time.sleep(2)
                        running = False
                    elif result is False:
                        display_game(guess, life, guessed_letters, difficulty)
                        time.sleep(2)
                        running = False

    return guess

def score():
    