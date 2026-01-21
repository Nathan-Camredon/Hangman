#----------Import----------
import random
try:
    from modules.enter import letter_press
except ImportError:
    from enter import letter_press

#----------Function----------
def letter(A, guess, word, life, guessed_letters, difficulty):
    """
    Verify if the letter is in the word
    """
    if A in guessed_letters:
        if difficulty == 0:
            return guess, life, guessed_letters
        life -= 1
        return guess, life, guessed_letters

    guessed_letters.append(A)
    if A in word:
        for i in range(len(word)):
            if A == word[i]:
                guess[i] = A
    else:
        life -= 1

    return guess, life, guessed_letters
            
def games_difficulty(difficulty):
    """
    Set the difficulty
    """
    guess = []
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
    Verify if the player win
    """
    if "".join(guess) == word:  #"".join(guess) -> guess = ["g", "u", "s", "s"] 
        return True
    if life == 0:
        return False
    return None

def games(difficulty, word):
    """
    Start the game
    """
    life = games_difficulty(difficulty)
    guessed_letters = []
    guess = ["_"] * len(word)
    while True:
        a = letter_press()
        guess, life, guessed_letters = letter(a, guess, word, life, guessed_letters, difficulty)
        if win(guess, word, life) == True:
            print("You win!")
            break
        if win(guess, word, life) == False:
            print("You lose!")
            break
    return guess

if __name__ == "__main__":
    games(0, "test")
