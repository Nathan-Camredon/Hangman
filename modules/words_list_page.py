import pygame
from modules.words_list import load_words, filter_words_by_length, add_word, delete_word

def word_list():
    window = screen
    #running = True

    # Charger les mots depuis words.txt
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            words = [w.strip() for w in f.readlines()]
    except FileNotFoundError:
        words = ["Erreur : fichier words.txt introuvable"]

    font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 35)

    # Bouton retour
    back_button = pygame.Rect(50, 50, 200, 70)

    # Gestion du scroll
    scroll_offset = 0
    scroll_speed = 40

    while running:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False

            # Scroll avec molette
            if event.type == pygame.MOUSEWHEEL:
                scroll_offset += event.y * scroll_speed

        # Bouton retour
        pygame.draw.rect(window, RED, back_button)
        window.blit(font.render("Retour", True, (255,255,255)), (70, 65))

        # Affichage des mots
        y = 150 + scroll_offset
        for word in words:
            text = small_font.render(word, True, (255,255,255))
            window.blit(text, (100, y))
            y += 40

        pygame.display.update()
        clock.tick(60)