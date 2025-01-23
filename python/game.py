import pygame
import sys
import random

# Initialiseer pygame
pygame.init()

# Scherminstellingen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodge Game")

# Kleuren
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Lettertype
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)

# Tekst
title_text = font.render("Welkom bij Mijn Game", True, black)
button_text = button_font.render("Start", True, white)

# Knop instellingen
button_width = 200
button_height = 100
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 2

# Speler instellingen
player_size = 50
player_x = screen_width // 2
player_y = screen_height - player_size - 10
player_speed = 10

# Obstakel instellingen
obstacle_size = 50
obstacle_x = random.randint(0, screen_width - obstacle_size)
obstacle_y = -obstacle_size
obstacle_speed = 8
max_speed = 20

# Klok
clock = pygame.time.Clock()

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    game_loop()

        screen.fill(white)
        screen.blit(title_text, ((screen_width - title_text.get_width()) // 2, 100))
        pygame.draw.rect(screen, blue, (button_x, button_y, button_width, button_height))
        screen.blit(button_text, (button_x + (button_width - button_text.get_width()) // 2, button_y + (button_height - button_text.get_height()) // 2))

        pygame.display.flip()

def game_loop():
    global player_x, obstacle_x, obstacle_y, obstacle_speed

    running = True
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Toetsen input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_d] and player_x < screen_width - player_size:
            player_x += player_speed

        # Obstakel beweging
        obstacle_y += obstacle_speed
        if obstacle_y > screen_height:
            obstacle_y = -obstacle_size
            obstacle_x = random.randint(0, screen_width - obstacle_size)
            score += 1
            if obstacle_speed < max_speed:
                obstacle_speed += 2

        # Botsdetectie
        if obstacle_y + obstacle_size > player_y:
            if player_x < obstacle_x < player_x + player_size or player_x < obstacle_x + obstacle_size < player_x + player_size:
                running = False

        # Scherm updaten
        screen.fill(white)
        pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, red, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))

        # Score weergeven
        score_text = pygame.font.Font(None, 36).render(f"Score: {score}", True, black)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    game_over()

def game_over():
    screen.fill(white)
    text = font.render("Game Over", True, red)
    screen.blit(text, ((screen_width - text.get_width()) // 2, (screen_height - text.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    main_menu()

if __name__ == "__main__":
    main_menu()
