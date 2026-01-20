#----------Import----------
import random


#----------Function----------
def letter(A, guess, word, life, letter, difficulty):
    if difficulty == 0:
        if A in letter and A in guess:
            return guess, life
    if A in letter:
        life -= 1
        return guess, life
    for i in range (len(word)):
        if A == word[i]:
            guess[i] = A
    return guess, life
            

def games_difficulty(difficulty):
    guess = []
    if difficulty == 0:
        life = 7

    if difficulty == 1:
        life = 6

    if difficulty == 2:
        life = 5
    return life


def games():
    pass