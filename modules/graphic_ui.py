import pygame
import time
from modules import words_list_page
from modules.games import games

# Init 
pygame.init()
clock = pygame.time.Clock()
# Window Size
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDHT, HEIGHT = screen.get_size()
#Center Window
center_x = WIDHT // 2
center_y = HEIGHT // 2

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (50, 100, 200)
LIGHT_BLUE = (0, 123, 255, 255)
RED = (180, 30, 30)
LIGHT_RED = (255, 0, 46, 255)
GREEN = (0, 255, 78)
DARK_GREEN = (0, 185, 78, 255)
YELLOW = (255, 255, 0, 255)


# Difficulty
difficulties = [
    "Facile",
    "Normal",
    "Difficile",
    "G0d lik3"]

difficulty_color = [
    (0, 200, 0),     # easy = green
    (240, 220, 0),   # medium = yellow
    (200, 50, 50),   # hard = purple
    (150, 0, 200),   # god_like = red
]


# Arrow Difficulty
arrow_left_png = pygame.image.load("modules/graphic/assets/arrow_left.png").convert_alpha()
arrow_right_png = pygame.image.load("modules/graphic/assets/arrow_right.png").convert_alpha()

arrow_left_png = pygame.transform.scale(arrow_left_png, (60, 60))
arrow_right_png = pygame.transform.scale(arrow_right_png, (60, 60))

# Function Buttons Rect
def draw_button(x, y, width, height, color, window):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(window, color, rect)
    return rect

# Text draw
def draw_text(text, size, color, center, window):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window.blit(text_surface, text_rect)

def draw_text_center(text, size, color, rect, window, bold=False):
    font = pygame.font.SysFont(None, size, bold=bold)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    window.blit(text_surface, text_rect)

# Function window size
def window_size(size_x, size_y, name):
    window = pygame.display.set_mode((size_x, size_y))
    window.fill(GRAY)
    pygame.display.set_caption(name)
    return window

# Song
def song(name):
    pass # En attente d'une musique

# Menu
def menu():

    # Variables
    window = screen
    running = True
    difficulty_index = 0

    draw_text(difficulties[difficulty_index],40,BLACK,(center_x, center_y + 145),window)

    # Arrow rect
    left_arrow_rect = arrow_left_png.get_rect()
    right_arrow_rect = arrow_right_png.get_rect()
    left_arrow_rect.topleft = (center_x - 250, center_y + 120)
    right_arrow_rect.topleft = (center_x + 190, center_y + 120)

    while running:
        window.fill(GRAY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                time.sleep(0.4)
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Play Button
                if play_button.collidepoint(event.pos):
                    games(1, "vicodine")
                    # ajouter stop music

                # Word Button
                elif word_button.collidepoint(event.pos): # En attente de la vrai fonction
                    words_list_page.word_list(screen, clock)
                    # ajouter stop music

                # Left Arrow
                elif left_arrow_rect.collidepoint(event.pos):
                    difficulty_index -= 1
                    if difficulty_index < 0:
                        difficulty_index = len(difficulties) - 1 # Gestion d'erreur ( a effaer repere flo)
                

                # Right Arrow
                elif right_arrow_rect.collidepoint(event.pos):
                    difficulty_index += 1
                    if difficulty_index >= len(difficulties):
                        difficulty_index = 0
                        # Gestion d'erreur ( a effacer repère flo)

                # Exit
                if exit_button.collidepoint(event.pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    running = False
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    # ajouter stop music







        # -- Buttons Play / Diffuculty / Word / Exit --

        # Play
        play_button = draw_button((center_x - 150), center_y, 300, 70, BLUE, window)

        mouse_pos = pygame.mouse.get_pos()
        play_color = LIGHT_BLUE if play_button.collidepoint(mouse_pos) else BLUE
        exit_button = draw_button((center_x - 150), center_y, 300, 70, play_color, window)
        draw_text("JOUER", 36, BLACK, play_button.center, window)
        
        # Difficulty rect
        difficulty_button = draw_button((center_x - 150), (center_y + 110), 300, 70, difficulty_color[difficulty_index], window)

        # Difficulty swap
        font = pygame.font.SysFont(None, 40)
        text = font.render(difficulties[difficulty_index], True, BLACK)
        window.blit(text, (center_x - 50, center_y + 130))


        # Word
        word_button = draw_button((center_x - 150), (center_y + 220), 300, 70, GREEN, window)
        mouse_pos = pygame.mouse.get_pos()
        word_color = GREEN if word_button.collidepoint(mouse_pos) else DARK_GREEN
        word_button = draw_button((center_x - 150), (center_y + 220), 300, 70, word_color, window)
        draw_text("MOTS", 36, BLACK, word_button.center, window)

        # Arrow blit
        window.blit(arrow_left_png, left_arrow_rect)
        window.blit(arrow_right_png, right_arrow_rect)

        # Quit
        exit_button = draw_button(center_x + 650, 10, 300, 70, RED, window)

        mouse_pos = pygame.mouse.get_pos()
        exit_color = LIGHT_RED if exit_button.collidepoint(mouse_pos) else RED
        exit_button = draw_button(center_x + 650, 10, 300, 70, exit_color, window)
        draw_text("QUITTER", 36, BLACK, exit_button.center, window)

        
        # Score Rectangle
        score = draw_button(40, 40, 300, 200, YELLOW, window)
        draw_text("VOTRE SCORE : 0",36,BLACK,(score.centerx, score.top + 25),window)

        clock.tick(60)
        pygame.display.update()



menu()