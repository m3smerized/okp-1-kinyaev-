# Задание №1.6

import pygame
import numpy as np

# Размеры окна
WIDTH = 1000
HEIGHT = 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Матрица преобразования
T = np.array([[1, 2], [1, -3]])
# Координаты пересекающихся отрезков
L = np.array([[-1 / 2, 3 / 2], [3, -2], [-1, -1], [3, 5 / 3]], dtype=float)


def transform_line(line_matrix, transformation_matrix):
    transformed_matrix = np.dot(line_matrix.reshape(2, 2), transformation_matrix)
    return transformed_matrix.reshape(2, 2)


def calculate_slope(line_matrix):
    x1, y1 = line_matrix[0]
    x2, y2 = line_matrix[1]
    if x2 - x1 == 0:
        return float('inf')
    return (y2 - y1) / (x2 - x1)


def draw_line(screen, center, color, start_point, end_point, width=3):
    x1, y1 = int(start_point[0] + center[0]), int(center[1] - start_point[1])
    x2, y2 = int(end_point[0] + center[0]), int(center[1] - end_point[1])
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), width)


def draw_text(screen, text, x, y, color=BLACK, font_size=20):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Intersecting Line Transformation")
    screen.fill(WHITE)

    center_x = WIDTH / 2
    center_y = HEIGHT / 2
    center = np.array([center_x, center_y])

    # Масштабирование отрезков и смещение
    scale_factor = 100
    offset_x = 0  # Смещение по оси X
    offset_y = 0  # Смещение по оси Y
    scaled_L = L * scale_factor
    scaled_L[:, 0] += offset_x
    scaled_L[:, 1] += offset_y

    # Преобразование отрезков
    transformed_L1 = transform_line(scaled_L[:2], T)
    transformed_L2 = transform_line(scaled_L[2:], T)

    # Расчет наклонов
    slope_L1 = calculate_slope(scaled_L[:2])
    slope_L2 = calculate_slope(scaled_L[2:])
    slope_transformed_L1 = calculate_slope(transformed_L1)
    slope_transformed_L2 = calculate_slope(transformed_L2)

    # Отображение отрезков
    draw_line(screen, center, YELLOW, scaled_L[0], scaled_L[1])  # Исходный L1
    draw_line(screen, center, YELLOW, scaled_L[2], scaled_L[3])  # Исходный L2
    draw_line(screen, center, BLUE, transformed_L1[0], transformed_L1[1])  # Преобразованный L1
    draw_line(screen, center, BLUE, transformed_L2[0], transformed_L2[1])  # Преобразованный L2

    # Вывод наклонов
    draw_text(screen, f"Исходный наклон L1: {slope_L1:.2f}", 10, 10)
    draw_text(screen, f"Исходный наклон L2: {slope_L2:.2f}", 10, 40)
    draw_text(screen, f"Преобразованный наклон L1: {slope_transformed_L1:.2f}", 10, 70)
    draw_text(screen, f"Преобразованный наклон L2: {slope_transformed_L2:.2f}", 10, 100)

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
