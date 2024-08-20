import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

SNAKE_SIZE = 20
snake_pos = [WIDTH // 2, HEIGHT // 2]
snake_speed = 20
direction = 'RIGHT'

def main():
    global direction

    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
        
        if direction == 'UP':
            snake_pos[1] -= snake_speed
        elif direction == 'DOWN':
            snake_pos[1] += snake_speed
        elif direction == 'LEFT':
            snake_pos[0] -= snake_speed
        elif direction == 'RIGHT':
            snake_pos[0] += snake_speed

        WINDOW.fill(BLACK)
        pygame.draw.rect(WINDOW, GREEN, pygame.Rect(snake_pos[0], snake_pos[1], SNAKE_SIZE, SNAKE_SIZE))
        
        pygame.display.flip()
        
        clock.tick(10)

if __name__ == "__main__":
    main()

