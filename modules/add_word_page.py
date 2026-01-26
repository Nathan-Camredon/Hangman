import pygame
pygame.init()
clock = pygame.time.Clock()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
center_x = WIDTH // 2
center_y = HEIGHT // 2
mouse_pos = pygame.mouse.get_pos()
background_word = pygame.image.load("modules/graphic/assets/background_word.png").convert()
background_word = pygame.transform.scale(background_word,(WIDTH, HEIGHT))
WHITE = (255,255,255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (180, 50, 50)
BLUE = (50, 100, 200)

FONT = pygame.font.SysFont("Arial", 32)
SMALL_FONT = pygame.font.SysFont("Arial", 24)


typed_word = ""

BUTTON_WIDTH = 300
BUTTON_HEIGHT = 70
back_button = pygame.Rect(40, 40, 300, 70)
confirm_button = pygame.Rect(center_x - 150, center_y + 100, 300, 60)
background_button = pygame.image.load("modules/graphic/assets/background_button.png").convert_alpha()
background_button_hover = pygame.image.load("modules/graphic/assets/background_button_hover.png").convert_alpha()

background_button = pygame.transform.scale(background_button, (BUTTON_WIDTH, BUTTON_HEIGHT))
background_button_hover = pygame.transform.scale(background_button_hover, (BUTTON_WIDTH, BUTTON_HEIGHT))

def draw_text(text, size, color, center, window):
    f = pygame.font.SysFont(None, size)
    text_surface = f.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window.blit(text_surface, text_rect)

def draw_add_word_page(screen):
    screen.blit(background_word, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    title = FONT.render("Add a word ?", True, BLACK)
    screen.blit(title, (center_x - title.get_width() // 2, 400))

    pygame.draw.rect(screen, GRAY, (center_x - 200, center_y - 40, 400, 60))
    text = FONT.render(typed_word, True, BLACK)
    screen.blit(text, (center_x - 190, center_y - 30))

    # Button Back
    return_image = background_button_hover if back_button.collidepoint(mouse_pos) else background_button
    screen.blit(return_image, back_button)
    draw_text("Retour", 36, BLUE, back_button.center, screen)

    # Button Confirm
    pygame.draw.rect(screen, RED, confirm_button)
    screen.blit(SMALL_FONT.render("Confirm", True, WHITE),
                (confirm_button.x + 60, confirm_button.y + 15))

    pygame.display.update()
    clock.tick(60)

def handle_add_word_event(event):
    global typed_word

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            typed_word = typed_word[:-1]
        elif event.key == pygame.K_RETURN:
            if typed_word.strip():
                return ("confirm", typed_word.strip())
        else:
            if len(typed_word) < 20:
                typed_word += event.unicode

    if event.type == pygame.MOUSEBUTTONDOWN:
        if back_button.collidepoint(event.pos):
            typed_word = ""
            return "back"

        if confirm_button.collidepoint(event.pos):
            if typed_word.strip():
                return ("confirm", typed_word.strip())

    return None

def add_word_page_loop(screen):
    running = True
    while running:
        draw_add_word_page(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "back"

            result = handle_add_word_event(event)
            if result is not None:
                return result

        clock.tick(60)
