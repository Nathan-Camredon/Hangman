# Files main.py
from modules.game import game
from modules.graphic_ui import menu
import pygame
from modules.score import ask_username


def main():
    username = ask_username()
    while True:

        difficulty = menu(username)
        if difficulty is None:
            break
    pygame.quit()
if __name__ == "__main__":
    main()