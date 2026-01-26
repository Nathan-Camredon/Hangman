# Fichier wods_list_page.py
import pygame
from modules.words_list import load_words
from modules.delete_word_page import draw_delete_word_page, handle_delete_word_event
from modules.add_word_page import draw_add_word_page, handle_add_word_event
  
clock = pygame.time.Clock()

#window size function
def window_size(size_x, size_y, name):
    window = pygame.display.set_mode((size_x, size_y))
    pygame.display.set_caption(name)
    return window

# Window Size
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.NOFRAME)
WIDHT, HEIGHT = screen.get_size()

center_x = WIDHT // 2
center_y = HEIGHT // 2

# Constant
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (180, 50, 50)
BLUE = (50, 100, 200)

# Scroll
words = load_words()
scroll_offset = 0
max_scroll = max(0, len(words) * 30 - 400)

# Boutons
back_button = pygame.Rect(750, 20, 120, 40)
add_button = pygame.Rect(50, 500, 150, 50)
delete_button = pygame.Rect(250, 500, 150, 50)

# Background
background_words = pygame.image.load("modules/graphic/assets/background_words.png").convert()
background_words = pygame.transform.scale(background_words,(WIDHT, HEIGHT))


font = pygame.font.SysFont("arial", 28)
words = load_words()
selected_word = None

def split_columns(items, col_size=20):
    return [items[i:i + col_size] for i in range(0, len(items), col_size)]

def draw_words(screen, words, selected_word, scroll_offset, font):
    columns = split_columns(words, col_size=20)
    x_start = 50
    y_start = 80 - scroll_offset
    col_spacing = 250
    line_spacing = 30

    for col_index, col in enumerate(columns):
        x = x_start + col_index * col_spacing
        y = y_start

        for word in col:
            color = (255, 255, 0) if word == selected_word else (255, 255, 255)
            text = font.render(word, True, color)
            screen.blit(text, (x, y))
            y += line_spacing

# Text draw
def draw_text(text, size, color, center, window):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window.blit(text_surface, text_rect)

def draw_buttons():
    # --- BUTTON IMAGES ---
    background_button = pygame.image.load("modules/graphic/assets/background_button.png").convert_alpha()
    background_button_hover = pygame.image.load("modules/graphic/assets/background_button_hover.png").convert_alpha()

    # Button size
    BUTTON_WIDTH = 300
    BUTTON_HEIGHT = 70

    #background button and hover
    background_button = pygame.transform.scale(background_button, (BUTTON_WIDTH, BUTTON_HEIGHT))
    background_button_hover = pygame.transform.scale(background_button_hover, (BUTTON_WIDTH,BUTTON_HEIGHT))

    # Return Button
    return_button = pygame.Rect((center_x + 500), (center_y -500),BUTTON_WIDTH, BUTTON_HEIGHT)
    mouse_pos = pygame.mouse.get_pos()
    return_image = (background_button_hover if return_button.collidepoint(mouse_pos)else background_button)
    screen.blit(return_image, return_button)
    draw_text("Retour", 36, BLUE, return_button.center, screen)

    #Add Button
    add_button = pygame.Rect((center_x + 500), (center_y -400),BUTTON_WIDTH, BUTTON_HEIGHT)
    mouse_pos = pygame.mouse.get_pos()
    return_image = (background_button_hover if add_button.collidepoint(mouse_pos)else background_button)
    screen.blit(return_image, add_button)
    draw_text("Add", 36, BLUE, add_button.center, screen)
    
    #Delete Button    
    delete_button_button = pygame.Rect((center_x + 500), (center_y -300),BUTTON_WIDTH, BUTTON_HEIGHT)
    mouse_pos = pygame.mouse.get_pos()
    return_image = (background_button_hover if delete_button_button.collidepoint(mouse_pos)else background_button)
    screen.blit(return_image, delete_button_button)
    draw_text("Delete", 36, BLUE, delete_button_button.center, screen)

def draw():
    screen.fill((30, 30, 30))
    draw_words()
    draw_buttons()

def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Scroll
        if event.button == 4:
            scroll_offset = max(0, scroll_offset - 20)
        elif event.button == 5:
            scroll_offset = min(max_scroll, scroll_offset + 20)

        # Boutons
        if back_button.collidepoint(event.pos):
            pass
            #on_back()

        elif add_button.collidepoint(event.pos):
            draw_add_word_page(screen)

        elif delete_button.collidepoint(event.pos):
            if selected_word:
                draw_delete_word_page(screen, selected_word)

        # Sélection d’un mot
        select_word(event.pos, words, scroll_offset)

def select_word(pos, words, scroll_offset):
    x, y = pos
    y += scroll_offset

    col_width = 250
    line_height = 30
    col_index = (x - 50) // col_width

    if col_index < 0:
        return

    word_index = (y - 80) // line_height
    global_index = col_index * 20 + word_index

    if 0 <= global_index < len(words):
        selected_word = words[global_index]
        return selected_word
    
def words_list_page():
    global scroll_offset, selected_word

    running = True

    while running:
        screen.blit(background_words, (0, 0))

        draw_words(screen, words, selected_word, scroll_offset, font)
        draw_buttons()   # utilise screen, donc OK

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scroll_offset = max(0, scroll_offset - 20)
                elif event.button == 5:
                    scroll_offset = min(max_scroll, scroll_offset + 20)

                if back_button.collidepoint(event.pos):
                    return "menu"
                elif add_button.collidepoint(event.pos):
                    pass

                elif delete_button.collidepoint(event.pos):
                    pass

                select_word(event.pos, scroll_offset)

        clock.tick(60)