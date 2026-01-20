import pygame
import time


# Init 
pygame.init()
clock = pygame.time.Clock()


# Window Size
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDHT, HEIGHT = screen.get_size()

center_x = WIDHT // 2
center_y = HEIGHT // 2

# Constant
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (50, 100, 200)
RED = (180, 50, 50)
GREEN = (0, 255, 78)
YELLOW = (255, 255, 0, 255)



def games_pages(guess):
    window = screen
    # Font setup
    font = pygame.font.SysFont("Arial", 40)

    running = True
    while running:
        window.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            text = font.render(f"{guess}", True, BLACK)
            # Position text: centered horizontally, spaced vertically
            text_rect = text.get_rect(center=(center_x, center_y - 100 + index * 50))
            window.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

