# Fichier game_logic.py
import random
from modules.score import save_score
#----------Function----------
def letter(A, guess, word, life, guessed_letters, difficulty):
    """
    Processes a letter guess in the Hangman game.

    Args:
        A (str): The letter guessed by the player.
        guess (list): The current state of the guessed word (letters and underscores).
        word (str): The target secret word.
        life (int): The current remaining lives.
        guessed_letters (list): List of already guessed letters.
        difficulty (int): The current game difficulty level.

    Returns:
        tuple: Updated (guess, life, guessed_letters).
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
        if difficulty == 3:
            if russian(life):
                life = 0

    return guess, life, guessed_letters
            
def game_difficulty(difficulty):
    """
    Determines the total lives based on the difficulty level.

    Args:
        difficulty (int): The difficulty level (0=Easy, 1=Normal, 2=Hard, 3=God Like).

    Returns:
        int: The number of lives.
    """
    if difficulty == 0:
        life = 7
    if difficulty == 1:
        life = 7
    if difficulty == 2:
        life = 6
    if difficulty == 3:
        life = 6
    return life

def win(guess, word, life, username, difficulty):
    """
    Checks the current game status.

    Args:
        guess (list): The current guessed word state.
        word (str): The secret word.
        life (int): Remaining lives.

    Returns:
        bool or None: True if won, False if lost, None if game continues.
    """
    if "".join(guess) == word: 
        save_score(username, difficulty)
        return True
    if life == 0:
        return False
    return None


def russian(life):
    """
    Implements the 'Russian Roulette' mechanic for Difficulty 3.
    
    The probability to instantly lose all lives increases as the player makes mistakes.

    Args:
        life (int): Current lives remaining.

    Returns:
        bool: True if the player unluckily dies, False otherwise.
    """

    max_lives = 6
    if life >= max_lives:
        return False
        
    threshold = max_lives - life
    # Roll a 6-sided die
    roll = random.randint(1, 6)
    
    if roll <= threshold:
        return True
    return False