import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SNAKE_SIZE = 20
snake_pos = [WIDTH // 2, HEIGHT // 2]
snake_body = [[WIDTH // 2, HEIGHT // 2]]
snake_speed = 20
direction = 'RIGHT'
change_to = direction
food_pos = [random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
            random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
score = 0
high_score = 0
obstacles = [[random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
              random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE] for _ in range(5)]
paused = False
speed_increment = 1.1
level = 1

# New feature constants
FOOD_COLORS = [RED, BLUE, YELLOW, WHITE, GREEN]
current_food_color = random.choice(FOOD_COLORS)

def game_over():
    global high_score
    if score > high_score:
        high_score = score
    font = pygame.font.SysFont(None, 55)
    text = font.render(f'Game Over! Score: {score}', True, RED)
    high_score_text = font.render(f'High Score: {high_score}', True, YELLOW)
    WINDOW.fill(BLACK)
    WINDOW.blit(text, (WIDTH // 6, HEIGHT // 3))
    WINDOW.blit(high_score_text, (WIDTH // 6, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    main()

def pause_game():
    global paused
    paused = not paused

def main():
    global direction, change_to, snake_pos, snake_body, food_pos, score, obstacles, paused, snake_speed, level, current_food_color

    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_game()
                if not paused:
                    if event.key == pygame.K_UP and direction != 'DOWN':
                        change_to = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        change_to = 'DOWN'
                    elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                        change_to = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        change_to = 'RIGHT'
        
        if paused:
            font = pygame.font.SysFont(None, 55)
            paused_text = font.render('Paused', True, YELLOW)
            WINDOW.blit(paused_text, (WIDTH // 2 - 80, HEIGHT // 3))
            pygame.display.flip()
            continue
        
        direction = change_to

        if direction == 'UP':
            snake_pos[1] -= snake_speed
        elif direction == 'DOWN':
            snake_pos[1] += snake_speed
        elif direction == 'LEFT':
            snake_pos[0] -= snake_speed
        elif direction == 'RIGHT':
            snake_pos[0] += snake_speed

        if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
            game_over()
        
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 1
            current_food_color = random.choice(FOOD_COLORS)  # Change food color
            if score % 5 == 0:  # Increase level every 5 points
                level += 1
                snake_speed *= speed_increment
            food_pos = [random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                        random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
            obstacles.append([random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                              random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE])
        else:
            snake_body.pop()

        if snake_pos in snake_body[1:]:
            game_over()
        if snake_pos in obstacles:
            game_over()

        if level % 2 == 0:
            WINDOW.fill(BLUE)  # Change background color
        else:
            WINDOW.fill(BLACK)
        
        pygame.draw.rect(WINDOW, GREEN, pygame.Rect(snake_pos[0], snake_pos[1], SNAKE_SIZE, SNAKE_SIZE))
        for segment in snake_body[1:]:
            pygame.draw.rect(WINDOW, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
        pygame.draw.rect(WINDOW, current_food_color, pygame.Rect(food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))
        for obs in obstacles:
            pygame.draw.rect(WINDOW, BLUE, pygame.Rect(obs[0], obs[1], SNAKE_SIZE, SNAKE_SIZE))
        
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        level_text = font.render(f'Level: {level}', True, WHITE)
        high_score_text = font.render(f'High Score: {high_score}', True, WHITE)
        WINDOW.blit(score_text, (10, 10))
        WINDOW.blit(level_text, (10, 40))
        WINDOW.blit(high_score_text, (10, 70))
        
        pygame.display.flip()
        
        clock.tick(10 + level)  # Increase game speed with level

if __name__ == "__main__":
    main()
