import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zaza")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Game clock
clock = pygame.time.Clock()
FPS = 60

# Player attributes
player_size = 50
player_x = WIDTH // 2 
player_y = HEIGHT - player_size - 10  # Stay on the ground
player_speed = 7

# Blocks (obstacles)
block_width = 50
block_height = 50
block_speed = 5
blocks = []

# Score
score = 0
font = pygame.font.Font(None, 36)

def create_block(): #function
    """Create a new falling block."""
    x = random.randint(0, WIDTH - block_width)
    y = -block_height  # Start off-screen
    return [x, y]

def draw_text(text, x, y):
    """Draw text on the screen."""
    label = font.render(text, True, BLACK)
    screen.blit(label, (x, y))

def main():
    global player_x, score

    # Initialize blocks as an empty list
    blocks = []
    running = True
    block_timer = 0

    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys for left/right movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Move left
            player_x -= player_speed
        if keys[pygame.K_d]:  # Move right
            player_x += player_speed

        # Prevent the player from moving out of bounds
        player_x = max(0, min(WIDTH - player_size, player_x))

        # Create blocks at regular intervals
        block_timer += 1
        if block_timer > 30:  # New block every half second (30 frames)
            blocks.append(create_block())
            block_timer = 0

        # Update blocks' positions
        for block in blocks:
            block[1] += block_speed

        # Remove blocks that are off-screen
        blocks = [block for block in blocks if block[1] < HEIGHT]

        # Check for collisions
        for block in blocks:
            if (
                player_x < block[0] + block_width
                and player_x + player_size > block[0]
                and player_y < block[1] + block_height
                and player_y + player_size > block[1]
            ):
                print("Game Over! Your score:", score)
                running = False

        # Update score
        score += 1

        # Draw player
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

        # Draw blocks 
        for block in blocks:
            pygame.draw.rect(screen, RED, (block[0], block[1], block_width, block_height))

        # Draw score
        draw_text(f"Score: {score}", 10, 10)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
