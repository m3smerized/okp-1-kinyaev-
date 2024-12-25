# Задание №1.8

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

# Матрица отражения относительно y = x
T = np.array([[0, 1], [1, 0]])

# Координаты треугольника
L = np.array([[8, 1], [7, 3], [6, 2]], dtype=float)


def transform_triangle(triangle_matrix, transformation_matrix):
    transformed_matrix = np.dot(triangle_matrix, transformation_matrix)
    return transformed_matrix

def draw_triangle(screen, center, color, triangle_matrix):
    points = [(int(p[0] + center[0]), int(center[1] - p[1])) for p in triangle_matrix]
    pygame.draw.polygon(screen, color, points, 3)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Triangle Reflection")
    screen.fill(WHITE)

    center_x = WIDTH / 2
    center_y = HEIGHT / 2
    center = np.array([center_x, center_y])

    # Масштабирование и смещение
    scale_factor = 100
    offset_x = -100  # Смещение по оси X
    offset_y = -100  # Смещение по оси Y

    scaled_L = L * scale_factor
    scaled_L[:, 0] += offset_x
    scaled_L[:, 1] += offset_y

    transformed_L = transform_triangle(scaled_L, T)

    transformed_L[:, 0] += offset_x
    transformed_L[:, 1] += offset_y


    # Отображение треугольника
    draw_triangle(screen, center, YELLOW, scaled_L)
    draw_triangle(screen, center, BLUE, transformed_L)

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