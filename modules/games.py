#----------Import----------
import random
import pygame
from modules.games_pages import display_game

#----------Function----------
def letter(A, guess, word, life, guessed_letters, difficulty):
    """
    Verify if the letter is in the word
    """
    # Check if letter already guessed
    if A in guessed_letters:
        if difficulty == 0:
            return guess, life, guessed_letters
        life -= 1
        return guess, life, guessed_letters

    guessed_letters.append(A)
    # Check if letter is in the word
    if A in word:
        for i in range(len(word)):
            if A == word[i]:
                guess[i] = A
    else:
        life -= 1

    return guess, life, guessed_letters
            
def games_difficulty(difficulty):
    """
    Set the difficulty (lives based on level)
    """
    guess = [] # Unused local var, can be removed, but keeping structure for now
    if difficulty == 0:
        life = 7
    if difficulty == 1:
        life = 7
    if difficulty == 2:
        life = 6
    if difficulty == 3:
        life = 1
    return life

def win(guess, word, life):
    """
    Verify if the player won or lost
    """
    if "".join(guess) == word: 
        return True
    if life == 0:
        return False
    return None

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
        display_game(guess)
        
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
                        print("You win!")
                        #"Win" screen or wait before closing
                        running = False
                    elif result is False:
                        print("You lose!")
                        #"Lose" screen
                        running = False

    return guess

if __name__ == "__main__":
    # Ensure games_pages init is called if running standalone (usually handled by main)
    # But games_pages has init at top level, so it should be fine.
    games(0, "test")
