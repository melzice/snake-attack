import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Fixed screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Screensaver")
pygame.mouse.set_visible(False)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
block_size = 20
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], block_size, block_size])

def game_loop():
    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = block_size
    y_change = 0

    snake = []
    snake_length = 1  # Start with 1 block

    food_x = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -block_size
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = block_size

        x += x_change
        y += y_change

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            running = False  # hit wall

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, block_size, block_size])

        snake.append([x, y])
        if len(snake) > snake_length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == [x, y]:  # hit self
                running = False

        draw_snake(snake)
        pygame.display.update()

        # Check if food is eaten
        if x == food_x and y == food_y:
            snake_length += 1  # Grow snake
            food_x = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size

        clock.tick(10)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()

