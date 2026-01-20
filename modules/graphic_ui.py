import pygame
import sys # Pour pouvoir arrêter complétement le programme

# ─────────────────────────────
# INITIALISATION
# ─────────────────────────────

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Jeu du Pendu")

WIDTH, HEIGHT = screen.get_size()

clock = pygame.time.Clock() # Limite la frqc Hz d'image par seconde

# ─────────────────────────────
# CONSTANTES
# ─────────────────────────────

MENU = "menu"
GAME = "game"
DIFFICULTY = "difficulty"
LIST_WORD = "list_word"

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (50, 100, 200)
RED = (180, 50, 50)
GREEN = (0, 255, 78)

# ─────────────────────────────
# UI - BOUTONS & RECTANGLES
# ─────────────────────────────

button_width = 300
button_height = 70

# Score (menu)
score_rect = pygame.Rect(100, 100, 500, 300)

# Quit (commun à toutes les pages)
quit_rect = pygame.Rect(WIDTH - 270, 20, 250, 80)

# Boutons centraux (menu)
buttons = []
center_x = WIDTH // 2
center_y = HEIGHT // 3

for i in range(3):
    rect = pygame.Rect(
        center_x - button_width // 2,
        center_y + i * (button_height + 50),
        button_width,
        button_height
    )
    buttons.append(rect)

# Arrows difficulty button
arrow_size = 80
left_arrow = pygame.Rect(WIDTH //2 - 250, HEIGHT //2 - 40, arrow_size, arrow_size)
right_arrow = pygame.Rect(WIDTH //2 + 170, HEIGHT // 2 - 40, arrow_size, arrow_size)

difficulty_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 40, 300, 80)



# ─────────────────────────────
# ÉTAT DU JEU
# ─────────────────────────────

current_page = MENU
running = True

# ─────────────────────────────
# GESTION DES ÉVÉNEMENTS
# ─────────────────────────────

def handle_events():
    global running, current_page

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if current_page == MENU:
                    running = False
                else:
                    current_page = MENU

        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(event.pos)


def handle_mouse_click(mouse_pos):
    global running, current_page

    # Bouton quitter (partout)
    if quit_rect.collidepoint(mouse_pos):
        running = False
        return

    # MENU
    if current_page == MENU:
        if buttons[0].collidepoint(mouse_pos):
            current_page = GAME

        elif buttons[1].collidepoint(mouse_pos):
            current_page = DIFFICULTY

        elif buttons[2].collidepoint(mouse_pos):
            current_page = LIST_WORD

    # DIFFICULTY
    elif current_page == DIFFICULTY:
        current_page = GAME

    # LIST_WORD
    elif current_page == LIST_WORD:
        current_page = MENU

    # GAME
    elif current_page == GAME:
        pass  # logique du jeu plus tard


# ─────────────────────────────
# AFFICHAGE
# ─────────────────────────────

def draw():
    screen.fill(BLACK)

    if current_page == MENU:
        draw_menu()

    elif current_page == DIFFICULTY:
        draw_difficulty()

    elif current_page == LIST_WORD:
        draw_list_word()

    elif current_page == GAME:
        draw_game()

    pygame.display.update()


def draw_menu():
    pygame.draw.rect(screen, BLUE, score_rect)
    pygame.draw.rect(screen, RED, quit_rect)

    for rect in buttons:
        pygame.draw.rect(screen, GREEN, rect)


def draw_difficulty():
    pygame.draw.rect(screen, RED, quit_rect)
    pygame.draw.rect(screen, GRAY, pygame.Rect(300, 300, 600, 300))


def draw_list_word():
    pygame.draw.rect(screen, RED, quit_rect)
    pygame.draw.rect(screen, GRAY, pygame.Rect(400, 200, 500, 400))


def draw_game():
    screen.fill((30, 60, 120))
    pygame.draw.rect(screen, RED, quit_rect)


# ─────────────────────────────
# BOUCLE PRINCIPALE
# ─────────────────────────────

while running:
    handle_events()
    draw()
    clock.tick(60)

pygame.quit()
sys.exit()
