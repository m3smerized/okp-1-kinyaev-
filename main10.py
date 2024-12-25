import pygame
import math
import numpy as np

# Размеры окна
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def pascal_snail(a, b, angle, center):
    r = b + 2 * a * math.cos(angle)
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return int(x + center[0]), int(center[1] - y)


def draw_pascal_snail(screen, center, a, b, color, steps=360 * 5, step_size=0.02):
    points = []
    for i in range(steps):
        angle = i * step_size
        point = pascal_snail(a, b, angle, center)
        points.append(point)
    if len(points) > 1:
        pygame.draw.lines(screen, color, False, points, 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pascal Snail")
    screen.fill(WHITE)

    center_x = WIDTH / 2
    center_y = HEIGHT / 2
    center = (center_x, center_y)

    a = 50
    b = 20

    draw_pascal_snail(screen, center, a, b, GREEN)

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
