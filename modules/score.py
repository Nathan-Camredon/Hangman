import json
import os
import pygame

def calculate_points(difficulty):
    """
    Returns points based on difficulty level.
    """
    if difficulty == 0: # Easy
        return 10
    elif difficulty == 1: # Normal
        return 20
    elif difficulty == 2: # Hard
        return 30
    elif difficulty == 3: # God ale
        return 50
    return 0

def ask_username():
    """
    Opens a Pygame loop to ask for the username.
    """
    pygame.init()
    
    # Get current screen size or use default
    info = pygame.display.Info()
    W, H = info.current_w, info.current_h
    screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
    
    font = pygame.font.Font(None, 74)
    input_box = pygame.Rect(W//2 - 200, H//2 - 32, 400, 64)
    color_active = pygame.Color('lightskyblue3')
    color_inactive = pygame.Color('gray15')
    color = color_active
    active = True
    text = ''
    done = False
    
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    # Limit length if needed
                    if len(text) < 15:
                        text += event.unicode

        screen.fill((30, 30, 30))
        
        # Render instruction text
        instruction_surface = font.render("Entrez votre pseudo :", True, (255, 255, 255))
        screen.blit(instruction_surface, (W//2 - instruction_surface.get_width()//2, H//2 - 100))

        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
    
    return text

def save_score(username, difficulty):
    """
    Saves the score to data/score.json.
    """
    if not username:
        return

    points = calculate_points(difficulty)
    file_path = os.path.join("data", "score.json")

    # Load existing scores
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                scores = json.load(f)
        except json.JSONDecodeError:
            scores = {}
    else:
        scores = {}

    # Update score
    if username in scores:
        scores[username] += points
    else:
        scores[username] = points

    # Save scores
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=4, ensure_ascii=False)
