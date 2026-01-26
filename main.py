# Files main.py
from modules.graphic_ui import menu
import pygame


def main():
    while True:
        difficulty = menu()
        if difficulty is None:
            break
    pygame.quit()

if __name__ == "__main__":
    main()