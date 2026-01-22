import pygame
from file_manager import load_words, save_words

class AddWordPage:
    def __init__(self, screen, on_back):
        self.screen = screen
        self.on_back = on_back
        self.font = pygame.font.SysFont("arial", 32)
        self.input_text = ""

        self.input_box = pygame.Rect(100, 200, 400, 50)
        self.validate_button = pygame.Rect(100, 300, 200, 50)

    def draw(self):
        self.screen.fill((20, 20, 20))

        pygame.draw.rect(self.screen, (255, 255, 255), self.input_box, 2)
        text = self.font.render(self.input_text, True, (255, 255, 255))
        self.screen.blit(text, (self.input_box.x + 10, self.input_box.y + 10))

        pygame.draw.rect(self.screen, (50, 180, 50), self.validate_button)
        self.screen.blit(self.font.render("Ajouter", True, (255, 255, 255)), (120, 310))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.save_word()
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.validate_button.collidepoint(event.pos):
                self.save_word()

    def save_word(self):
        if self.input_text.strip():
            words = load_words()
            words.append(self.input_text.strip())
            save_words(words)
        self.on_back()