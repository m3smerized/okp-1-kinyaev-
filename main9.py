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

# Матрица масштабирования
T = np.array([[2, 0], [0, 2]])

# Координаты треугольника
L = np.array([[5, 1], [5, 2], [3, 2]], dtype=float)


def transform_triangle(triangle_matrix, transformation_matrix):
    transformed_matrix = np.dot(triangle_matrix, transformation_matrix)
    return transformed_matrix

def draw_triangle(screen, center, color, triangle_matrix):
    points = [(int(p[0] + center[0]), int(center[1] - p[1])) for p in triangle_matrix]
    pygame.draw.polygon(screen, color, points, 3)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Triangle Scaling")
    screen.fill(WHITE)

    center_x = WIDTH / 2
    center_y = HEIGHT / 2
    center = np.array([center_x, center_y])

    # Масштабирование и смещение для исходного треугольника
    scale_factor = 50
    offset_x = -150  # Смещение по оси X
    offset_y = -150  # Смещение по оси Y


    scaled_L = L * scale_factor
    scaled_L[:, 0] += offset_x
    scaled_L[:, 1] += offset_y


    # Масштабирование
    transformed_L = transform_triangle(L, T)

    # Масштабирование и смещение для масштабированного треугольника
    scaled_transformed_L = transformed_L * scale_factor
    scaled_transformed_L[:, 0] += offset_x
    scaled_transformed_L[:, 1] += offset_y

    # Отображение треугольников
    draw_triangle(screen, center, RED, scaled_L)
    draw_triangle(screen, center, BLUE, scaled_transformed_L)

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