import pygame
from file_manager import load_words, save_words

class DeleteWordPage:
    def __init__(self, screen, word, on_back):
        self.screen = screen
        self.word = word
        self.on_back = on_back
        self.font = pygame.font.SysFont("arial", 32)

        self.yes_button = pygame.Rect(100, 300, 150, 50)
        self.no_button = pygame.Rect(300, 300, 150, 50)

    def draw(self):
        self.screen.fill((20, 20, 20))

        msg = self.font.render(f"Supprimer '{self.word}' ?", True, (255, 255, 255))
        self.screen.blit(msg, (100, 200))

        pygame.draw.rect(self.screen, (180, 50, 50), self.yes_button)
        pygame.draw.rect(self.screen, (50, 180, 50), self.no_button)

        self.screen.blit(self.font.render("Oui", True, (255, 255, 255)), (140, 310))
        self.screen.blit(self.font.render("Non", True, (255, 255, 255)), (340, 310))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.yes_button.collidepoint(event.pos):
                words = load_words()
                words = [w for w in words if w != self.word]
                save_words(words)
                self.on_back()

            elif self.no_button.collidepoint(event.pos):
                self.on_back()