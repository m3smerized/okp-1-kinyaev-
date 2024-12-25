#  Задание №1.2

import pygame
import numpy as np

# Размеры окна
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
FONT_SIZE = 20


def draw_primitives(screen, center):
    # Окружность
    pygame.draw.circle(screen, RED, (int(center[0]), int(center[1])), 50)
    # Линии
    pygame.draw.line(screen, GREEN, (center[0] - 100, center[1] - 100), (center[0] + 100, center[1] + 100), 3)
    pygame.draw.line(screen, BLUE, (center[0] + 100, center[1] - 100), (center[0] - 100, center[1] + 100), 3)
    # Текст
    font = pygame.font.Font(None, FONT_SIZE)
    text = font.render("Примитивы", True, BLACK)
    screen.blit(text, (center[0] - 30, center[1] + 60))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Transforming Line")
    screen.fill(WHITE)
    center_x = WIDTH / 2
    center_y = HEIGHT / 2
    center = np.array([center_x, center_y])

    draw_primitives(screen, center)

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
