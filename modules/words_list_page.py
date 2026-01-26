# Fichier words_list_page.py
import pygame

from modules.delete_word_page import delete_word_page_loop
from modules.add_word_page import add_word_page_loop
from modules.file_manager import save_words, load_words

pygame.init()
clock = pygame.time.Clock()

# --- Fenêtre ---
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

center_x = WIDTH // 2
center_y = HEIGHT // 2

# --- Couleurs ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (180, 50, 50)
BLUE = (50, 100, 200)

# --- Police ---
font = pygame.font.SysFont("arial", 28)

# --- Données ---
words = load_words()
selected_word = None

# --- Scroll (4 colonnes x 19 lignes) ---
COLS = 4
ROWS = 19
scroll_offset = 0

def compute_max_scroll():
    global words
    total_rows = (len(words) + COLS - 1) // COLS
    return max(0, total_rows - ROWS)

max_scroll = compute_max_scroll()

# --- Boutons ---
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 70

back_button = pygame.Rect(center_x + 600, center_y - 300, BUTTON_WIDTH, BUTTON_HEIGHT)
add_button = pygame.Rect(center_x + 600, center_y - 200, BUTTON_WIDTH, BUTTON_HEIGHT)
delete_button = pygame.Rect(center_x + 600, center_y - 100, BUTTON_WIDTH, BUTTON_HEIGHT)

# --- Background ---
background_word = pygame.image.load("modules/graphic/assets/background_word.png").convert()
background_word = pygame.transform.scale(background_word, (WIDTH, HEIGHT))


# ---------- Dessin texte ----------
def draw_text(text, size, color, center, window):
    f = pygame.font.SysFont(None, size)
    text_surface = f.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window.blit(text_surface, text_rect)


# ---------- Dessin des mots ----------
def draw_words(screen, words, selected_word, scroll_offset, font):
    x_start = 350
    y_start = 260
    col_spacing = 250
    line_spacing = 30

    first_row = scroll_offset
    first_index = first_row * COLS

    for row in range(ROWS):
        for col in range(COLS):
            index = first_index + row * COLS + col
            if index >= len(words):
                return

            word = words[index]
            color = (255, 255, 0) if word == selected_word else (255, 255, 255)
            text = font.render(word, True, color)

            x = x_start + col * col_spacing
            y = y_start + row * line_spacing

            screen.blit(text, (x, y))


# ---------- Sélection d'un mot ----------
def select_word(pos, words, scroll_offset):
    global selected_word

    x, y = pos

    x_start = 350
    y_start = 260
    col_spacing = 250
    line_spacing = 30

    col = (x - x_start) // col_spacing
    row = (y - y_start) // line_spacing

    if col < 0 or col >= COLS or row < 0 or row >= ROWS:
        return None

    first_row = scroll_offset
    first_index = first_row * COLS

    index = first_index + row * COLS + col

    if 0 <= index < len(words):
        selected_word = words[index]
        return selected_word

    return None


# ---------- Boutons ----------
def draw_buttons():
    background_button = pygame.image.load("modules/graphic/assets/background_button.png").convert_alpha()
    background_button_hover = pygame.image.load("modules/graphic/assets/background_button_hover.png").convert_alpha()

    background_button = pygame.transform.scale(background_button, (BUTTON_WIDTH, BUTTON_HEIGHT))
    background_button_hover = pygame.transform.scale(background_button_hover, (BUTTON_WIDTH, BUTTON_HEIGHT))

    mouse_pos = pygame.mouse.get_pos()

    # Retour
    return_image = background_button_hover if back_button.collidepoint(mouse_pos) else background_button
    screen.blit(return_image, back_button)
    draw_text("Retour", 36, BLUE, back_button.center, screen)

    # Add
    add_image = background_button_hover if add_button.collidepoint(mouse_pos) else background_button
    screen.blit(add_image, add_button)
    draw_text("Add", 36, BLUE, add_button.center, screen)

    # Delete
    delete_image = background_button_hover if delete_button.collidepoint(mouse_pos) else background_button
    screen.blit(delete_image, delete_button)
    draw_text("Delete", 36, BLUE, delete_button.center, screen)


# ---------- Page principale ----------
def words_list_page():
    global scroll_offset, selected_word, words, max_scroll

    running = True
    result = None

    # recalcul au cas où la liste a changé avant d'arriver ici
    max_scroll = compute_max_scroll()

    while running:
        screen.blit(background_word, (0, 0))

        draw_words(screen, words, selected_word, scroll_offset, font)
        draw_buttons()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Scroll
                if event.button == 4:  # molette haut
                    scroll_offset = max(0, scroll_offset - 1)
                elif event.button == 5:  # molette bas
                    scroll_offset = min(max_scroll, scroll_offset + 1)

                # Bouton retour
                if back_button.collidepoint(event.pos):
                    return "menu"

                # Bouton add
                elif add_button.collidepoint(event.pos):
                    result = add_word_page_loop(screen)
                    if isinstance(result, tuple) and result[0] == "confirm":
                        new_word = result[1]
                        words.append(new_word)
                        save_words(words)
                        max_scroll = compute_max_scroll()
                        result = None

                # Bouton delete
                elif delete_button.collidepoint(event.pos):
                    if selected_word:
                        result = delete_word_page_loop(screen, selected_word)
                        if result == "confirm":
                            words.remove(selected_word)
                            save_words(words)
                            selected_word = None
                            max_scroll = compute_max_scroll()
                            result = None

                # Sélection d'un mot
                selected_word = select_word(event.pos, words, scroll_offset)

        clock.tick(60)
