import pygame
from modules.file_manager import load_words, save_words

class WordsListPage:
    def __init__(self, screen, on_back, on_add, on_delete):
        self.screen = screen
        self.on_back = on_back
        self.on_add = on_add
        self.on_delete = on_delete

        self.font = pygame.font.SysFont("arial", 28)

        self.words = load_words()
        self.selected_word = None

        # Scroll
        self.scroll_offset = 0
        self.max_scroll = max(0, len(self.words) * 30 - 400)

        # Boutons
        self.back_button = pygame.Rect(750, 20, 120, 40)
        self.add_button = pygame.Rect(50, 500, 150, 50)
        self.delete_button = pygame.Rect(250, 500, 150, 50)

    def split_columns(self, items, col_size=20):
        return [items[i:i + col_size] for i in range(0, len(items), col_size)]

    def draw_words(self):
        columns = self.split_columns(self.words, col_size=20)

        x_start = 50
        y_start = 80 - self.scroll_offset
        col_spacing = 250
        line_spacing = 30

        for col_index, col in enumerate(columns):
            x = x_start + col_index * col_spacing
            y = y_start

            for word in col:
                color = (255, 255, 0) if word == self.selected_word else (255, 255, 255)
                text = self.font.render(word, True, color)
                self.screen.blit(text, (x, y))
                y += line_spacing

    def draw_buttons(self):
        pygame.draw.rect(self.screen, (180, 50, 50), self.back_button)
        pygame.draw.rect(self.screen, (50, 180, 50), self.add_button)
        pygame.draw.rect(self.screen, (50, 50, 180), self.delete_button)

        self.screen.blit(self.font.render("Retour", True, (255, 255, 255)), (self.back_button.x + 20, self.back_button.y + 5))
        self.screen.blit(self.font.render("Ajouter", True, (255, 255, 255)), (self.add_button.x + 20, self.add_button.y + 10))
        self.screen.blit(self.font.render("Supprimer", True, (255, 255, 255)), (self.delete_button.x + 10, self.delete_button.y + 10))

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.draw_words()
        self.draw_buttons()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Scroll
            if event.button == 4:
                self.scroll_offset = max(0, self.scroll_offset - 20)
            elif event.button == 5:
                self.scroll_offset = min(self.max_scroll, self.scroll_offset + 20)

            # Boutons
            if self.back_button.collidepoint(event.pos):
                self.on_back()

            elif self.add_button.collidepoint(event.pos):
                self.on_add()

            elif self.delete_button.collidepoint(event.pos):
                if self.selected_word:
                    self.on_delete(self.selected_word)

            # Sélection d’un mot
            self.select_word(event.pos)

    def select_word(self, pos):
        x, y = pos
        y += self.scroll_offset

        col_width = 250
        line_height = 30
        col_index = (x - 50) // col_width

        if col_index < 0:
            return

        word_index = (y - 80) // line_height
        global_index = col_index * 20 + word_index

        if 0 <= global_index < len(self.words):
            self.selected_word = self.words[global_index]