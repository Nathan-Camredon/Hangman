from modules.games import games
from modules.games import games_difficulty
from modules.games_pages import games_pages
def main():
    while True: 
        difficulty = 0
        word = "test"
        games_difficulty(difficulty)
        guess = games(difficulty, word)
        games_pages(guess)
if __name__ == "__main__":
    main()