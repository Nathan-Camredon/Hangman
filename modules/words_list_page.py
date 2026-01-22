import pygame
from . import words_list
def word_list(screen, clock):
    screen.fill((0,0,0))
    window = screen
    running = True
   
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            words = [w.strip() for w in f.readlines()]
    except FileNotFoundError:
        words = ["Erreur : fichier words.txt introuvable"]

    font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 35)

    back_button = pygame.Rect(50, 50, 200, 70)

    scroll_offset = 0
    scroll_speed = 40

    while running:
        window.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False

            if event.type == pygame.MOUSEWHEEL:
                scroll_offset += event.y * scroll_speed

        pygame.draw.rect(window,(0,0,0), back_button)
        window.blit(font.render("Retour", True, (255,255,255)), (70, 65))

        y = 150 + scroll_offset
        for word in words:
            text = small_font.render(word, True, (255,255,255))
            window.blit(text, (100, y))
            y += 40

        pygame.display.update()
        clock.tick(60)