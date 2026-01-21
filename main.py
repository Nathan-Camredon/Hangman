from modules.games import games
from modules.games import games_difficulty

def main():
    while True: 
        difficulty = 0
        word = "vicodine"
        games_difficulty(difficulty)
        games(difficulty, word)
if __name__ == "__main__":
    main()
