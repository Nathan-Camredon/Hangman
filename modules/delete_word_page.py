import pygame
pygame.init()
clock = pygame.time.Clock()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
center_x = WIDTH // 2
center_y = HEIGHT // 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (180, 50, 50)

FONT = pygame.font.SysFont("Arial", 32)
SMALL_FONT = pygame.font.SysFont("Arial", 24)

# Boutons
cancel_button = pygame.Rect(center_x - 300, center_y + 80, 250, 60)
confirm_button = pygame.Rect(center_x + 50, center_y + 80, 250, 60)


def draw_delete_word_page(screen, word):
    screen.fill(WHITE)

    title = FONT.render("Supprimer ce mot ?", True, BLACK)
    screen.blit(title, (center_x - title.get_width() // 2, 40))

    word_text = FONT.render(word, True, RED)
    screen.blit(word_text, (center_x - word_text.get_width() // 2, center_y - 40))

    # Bouton annuler
    pygame.draw.rect(screen, GRAY, cancel_button)
    screen.blit(SMALL_FONT.render("Annuler", True, BLACK),
                (cancel_button.x + 60, cancel_button.y + 15))

    # Bouton confirmer
    pygame.draw.rect(screen, RED, confirm_button)
    screen.blit(SMALL_FONT.render("Supprimer", True, WHITE),
                (confirm_button.x + 50, confirm_button.y + 15))

    pygame.display.update()
    clock.tick(60)


def handle_delete_word_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:

        if cancel_button.collidepoint(event.pos):
            return "cancel"

        if confirm_button.collidepoint(event.pos):
            return "confirm"

    return None