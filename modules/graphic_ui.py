import pygame
import time
import sys
from modules.words_list_page import WordsListPage
from modules.games import games





# Init 
pygame.init()
clock = pygame.time.Clock()

#---------------
# CONSTANTS
#---------------

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

# Background
background_main = pygame.image.load("modules/graphic/assets/background_main.png").convert()
background_main = pygame.transform.scale(background_main,(WIDHT, HEIGHT))
background_score = pygame.image.load("modules/graphic/assets/background_score.png").convert_alpha()
background_button = pygame.image.load("modules/graphic/assets/background_button.png").convert_alpha()


# --- BUTTON IMAGES ---
background_button = pygame.image.load("modules/graphic/assets/background_button.png").convert_alpha()
background_button_exit = pygame.image.load("modules/graphic/assets/background_button_exit.png").convert_alpha()
background_button_hover = pygame.image.load("modules/graphic/assets/background_button_hover.png").convert_alpha()

# Button size
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 70

background_button = pygame.transform.scale(background_button, (BUTTON_WIDTH, BUTTON_HEIGHT))
background_button_exit = pygame.transform.scale(background_button_exit, (BUTTON_WIDTH, BUTTON_HEIGHT))
background_button_hover = pygame.transform.scale(background_button_hover, (BUTTON_WIDTH,BUTTON_HEIGHT))

# Arrow Difficulty
arrow_left_png = pygame.image.load("modules/graphic/assets/arrow_left.png").convert_alpha()
arrow_right_png = pygame.image.load("modules/graphic/assets/arrow_right.png").convert_alpha()

arrow_left_png = pygame.transform.scale(arrow_left_png, (60, 60))
arrow_right_png = pygame.transform.scale(arrow_right_png, (60, 60))


#--------------------
#   FUNCTIONS
#--------------------


# Function Buttons Rect
def draw_button_pic(x, y, width, height, image, window):
    rect = pygame.Rect(x, y, width, height)
    image = pygame.transform.scale(image, (width, height))
    window.blit(image, rect)
    return rect

# Text draw
def draw_text(text, size, color, center, window):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window.blit(text_surface, text_rect)

# Function window size
def window_size(size_x, size_y, name):
    window = pygame.display.set_mode((size_x, size_y))
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
    window.blit(background_main, (0, 0))
    draw_text(difficulties[difficulty_index],40,BLACK,(center_x, center_y + 145),window)

    # Arrow rect
    left_arrow_rect = arrow_left_png.get_rect()
    right_arrow_rect = arrow_right_png.get_rect()
    left_arrow_rect.topleft = (center_x - 250, center_y + 120)
    right_arrow_rect.topleft = (center_x + 90, center_y + 120)


    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                time.sleep(0.4)
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Play Button
                if play_button.collidepoint(event.pos):
                    games(difficulty_index, "vicodine")
                    # ajouter stop music

                # Word Button
                elif word_button.collidepoint(event.pos): # En attente de la vrai fonction
                    word_list(screen, clock)
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
                elif exit_button.collidepoint(event.pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    return





        # -- Buttons Play / Diffuculty / Word / Exit --

        # Play
        play_button = pygame.Rect(center_x - 200,center_y,BUTTON_WIDTH,BUTTON_HEIGHT)
        mouse_pos = pygame.mouse.get_pos()
        play_image = (background_button_hover if play_button.collidepoint(mouse_pos)else background_button)
        window.blit(play_image, play_button)
        draw_text("JOUER", 36, WHITE, play_button.center, window) 
        
        # Difficulty rect
        difficulty_button = pygame.Rect((center_x - 200), (center_y + 110), BUTTON_WIDTH, BUTTON_HEIGHT)

        # Difficulty swap
        window.blit(background_button, difficulty_button)
        draw_text(difficulties[difficulty_index],36, difficulty_color[difficulty_index], difficulty_button.center, window)



        # Word
        word_button = pygame.Rect((center_x - 200), (center_y + 220),BUTTON_WIDTH, BUTTON_HEIGHT)
        mouse_pos = pygame.mouse.get_pos()
        word_img = (background_button_hover if word_button.collidepoint(mouse_pos) else background_button)
        window.blit(word_img, word_button)
        draw_text("MOTS", 36, WHITE, word_button.center, window)

        # Arrow blit
        window.blit(arrow_left_png, left_arrow_rect)
        window.blit(arrow_right_png, right_arrow_rect)

        # Quit
        exit_button = pygame.Rect((center_x - 200), (center_y + 330),BUTTON_WIDTH, BUTTON_HEIGHT)
        mouse_pos = pygame.mouse.get_pos()
        exit_img = (background_button_hover if exit_button.collidepoint(mouse_pos) else background_button_exit)
        window.blit(exit_img, exit_button)
        draw_text("QUITTER", 36, RED, exit_button.center, window)

        
        # Score Rectangle
        score = draw_button_pic(40, 40, 300, 100, background_score, window) 
        draw_text("VOTRE SCORE : 0", 28, WHITE, score.center, window)

        clock.tick(60)
        pygame.display.update()





# Fonction en attente
def word_list():
    pass
def game():
    pass



# Call
menu()
pygame.quit()
sys.exit()

