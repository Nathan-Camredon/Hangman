# Files graphic_ui.py


import pygame
import time
from modules.words_list_page import words_list_page
from modules.words_list import words_selector





# Init
pygame.init()
clock = pygame.time.Clock()


#---------------
# CONSTANTS
#---------------


# Window Size
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
#Center Window
center_x = WIDTH // 2
center_y = HEIGHT // 2


# Soundtrack
pygame.mixer.music.load("modules/graphic/assets/soundtrack.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


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
    "EASY",
    "MEDIUM",
    "HARD",
    "G0D LIK3"]


difficulty_color = [
    (0, 200, 0),     # easy = green
    (240, 220, 0),   # medium = yellow
    (200, 50, 50),   # hard = purple
    (150, 0, 200),   # god_like = red
]


# Background
background_main = pygame.image.load("modules/graphic/assets/background_main.png").convert()
background_main = pygame.transform.scale(background_main,(WIDTH, HEIGHT))
background_score = pygame.image.load("modules/graphic/assets/background_score.png").convert_alpha()
background_button = pygame.image.load("modules/graphic/assets/background_button.png").convert_alpha()
popup_img = pygame.image.load("modules/graphic/assets/background_score.png").convert_alpha()
popup_rect = popup_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))


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


# Function Buttons Rectangle
def draw_button_pic(x, y, width, height, image, window):
    """Draw Button size, position and screen"""
    rect = pygame.Rect(x, y, width, height)
    image = pygame.transform.scale(image, (width, height))
    window.blit(image, rect)
    return rect

# Function Text draw
def draw_text(text, size, color, center, window):
    """Draw text with color size and screen"""
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window.blit(text_surface, text_rect)

# Function window size
def window_size(size_x, size_y, name):
    """Window Size"""
    window = pygame.display.set_mode((size_x, size_y))
    pygame.display.set_caption(name)
    return window

# Function end game
def end_game_screen(result, word):
    """Function for end game, win or lose with text and pop up, back to menu after 3s"""
    font_title = pygame.font.SysFont("Arial", 60, bold=True)
    font_word = pygame.font.SysFont("Arial", 40)

    if result == "WIN":
        title_text = "Win !"
        color = GREEN
    else:
        title_text = "Ho no... Lose"
        color = RED

    title_surface = font_title.render(title_text, True, color)
    word_surface = font_word.render(f"The word was : {word}", True, WHITE)

    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < 3000: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        
        screen.blit(background_main, (0, 0)) 


        screen.blit(popup_img, popup_rect)


        screen.blit(
            title_surface,
            title_surface.get_rect(center=(popup_rect.centerx, popup_rect.centery - 40))
        )
        screen.blit(
            word_surface,
            word_surface.get_rect(center=(popup_rect.centerx, popup_rect.centery + 30))
        )

        pygame.display.flip()

# Menu
def menu():
    """Game loop craft Buttons / Arrows / Mouse pos and 
    Play, difficulty, words & quit button"""
    from modules.game import game

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
        screen.blit(background_main, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                time.sleep(0.4)
                return None

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Play Button
                if play_button.collidepoint(event.pos):
                    word = words_selector(difficulty_index)
                    game(difficulty_index, word)
                    

                # Word Button
                elif word_button.collidepoint(event.pos):
                    words_list_page()
                    
                # Left Arrow
                elif left_arrow_rect.collidepoint(event.pos):
                    difficulty_index -= 1
                    if difficulty_index < 0:
                        difficulty_index = len(difficulties) - 1

                # Right Arrow
                elif right_arrow_rect.collidepoint(event.pos):
                    difficulty_index += 1
                    if difficulty_index >= len(difficulties):
                        difficulty_index = 0
                        


                # Exit
                elif exit_button.collidepoint(event.pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    return None





        # -- Buttons Play / Diffuculty / Word / Exit --

        # Play
        play_button = pygame.Rect(center_x - 200,center_y,BUTTON_WIDTH,BUTTON_HEIGHT)
        mouse_pos = pygame.mouse.get_pos()
        play_image = (background_button_hover if play_button.collidepoint(mouse_pos)else background_button)
        window.blit(play_image, play_button)
        draw_text("PLAY", 36, WHITE, play_button.center, window) 
        
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
        draw_text("WORDS", 36, WHITE, word_button.center, window)

        # Arrow blit
        window.blit(arrow_left_png, left_arrow_rect)
        window.blit(arrow_right_png, right_arrow_rect)

        # Quit
        exit_button = pygame.Rect((center_x - 200), (center_y + 330),BUTTON_WIDTH, BUTTON_HEIGHT)
        mouse_pos = pygame.mouse.get_pos()
        exit_img = (background_button_hover if exit_button.collidepoint(mouse_pos) else background_button_exit)
        window.blit(exit_img, exit_button)
        draw_text("QUIT", 36, RED, exit_button.center, window)

        
        # Score Rectangle
        score = draw_button_pic(40, 40, 300, 100, background_score, window) 
        draw_text(f"Your Score : ", 28, WHITE, score.center, window)

        clock.tick(60)
        pygame.display.update()