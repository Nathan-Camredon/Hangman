#----------Import----------
import random
try:
    from modules.enter import letter_press
except ImportError:
    from enter import letter_press

#----------Function----------
def letter(A, guess, word, life, guessed_letters, difficulty):
    if A in guessed_letters:
        if difficulty == 0 and A in guess:
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
    guess = []
    if difficulty == 0:
        life = 7
    if difficulty == 1:
        life = 6
    if difficulty == 2:
        life = 5
    return life


def games(difficulty, word):
    life = games_difficulty(difficulty)
    guessed_letters = []
    guess = ["_"] * len(word)
    while True:
        a = letter_press()
        guess, life, guessed_letters = letter(a, guess, word, life, guessed_letters, difficulty)
        print(life, guessed_letters, guess)
    

if __name__ == "__main__":
    games(1, "caca")