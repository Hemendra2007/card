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

SNAKE_SIZE = 20
snake_pos = [WIDTH // 2, HEIGHT // 2]
snake_body = [[WIDTH // 2, HEIGHT // 2]]
snake_speed = 20
direction = 'RIGHT'
change_to = direction
food_pos = [random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
            random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
score = 0
obstacles = [[random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
              random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE] for _ in range(5)]
paused = False
speed_increment = 1.1

def game_over():
    font = pygame.font.SysFont(None, 55)
    text = font.render(f'Game Over! Score: {score}', True, RED)
    WINDOW.fill(BLACK)
    WINDOW.blit(text, (WIDTH // 6, HEIGHT // 3))
    pygame.display.flip()
    pygame.time.wait(2000)
    main()

def pause_game():
    global paused
    paused = not paused

def main():
    global direction, change_to, snake_pos, snake_body, food_pos, score, obstacles, paused, snake_speed

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
        
        WINDOW.fill(BLACK)
        pygame.draw.rect(WINDOW, GREEN, pygame.Rect(snake_pos[0], snake_pos[1], SNAKE_SIZE, SNAKE_SIZE))
        for segment in snake_body[1:]:
            pygame.draw.rect(WINDOW, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
        pygame.draw.rect(WINDOW, RED, pygame.Rect(food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))
        for obs in obstacles:
            pygame.draw.rect(WINDOW, BLUE, pygame.Rect(obs[0], obs[1], SNAKE_SIZE, SNAKE_SIZE))
        
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        WINDOW.blit(score_text, (10, 10))
        
        pygame.display.flip()
        
        clock.tick(10)

if __name__ == "__main__":
    main()
