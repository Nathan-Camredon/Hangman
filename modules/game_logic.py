
import random

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
        if difficulty == 3:
            if russian(life):
                life = 0

    return guess, life, guessed_letters
            
def games_difficulty(difficulty):
    """
    Set the difficulty (lives based on level)
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

def win(guess, word, life):
    """
    Verify if the player won or lost
    """
    if "".join(guess) == word: 
        return True
    if life == 0:
        return False
    return None


def russian(life):
    """
    Russian Roulette mechanic for Difficulty 3.
    Probability to die increases with mistakes.
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