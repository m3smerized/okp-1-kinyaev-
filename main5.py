# Задание №1.5

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
T = np.array([[1, 2], [3, 1]])
# Координаты параллельных отрезков
L = np.array([[50, 100], [250, 200], [50, 200], [250, 300]], dtype=float)


def transform_line(line_matrix, transformation_matrix):
    transformed_matrix = np.dot(line_matrix.reshape(2, 2), transformation_matrix)
    return transformed_matrix.reshape(2, 2)


def calculate_slope(line_matrix):
    x1, y1 = line_matrix[0]
    x2, y2 = line_matrix[1]
    if x2 - x1 == 0:
        return float('inf')  # Infinite slope for vertical line
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
    pygame.display.set_caption("Parallel Line Transformation")
    screen.fill(WHITE)

    # Смещаем центр чтобы оба отрезка поместились на экран
    center_x = 100
    center_y = 700
    center = np.array([center_x, center_y])

    # Преобразование отрезков
    transformed_L1 = transform_line(L[:2], T)  # Преобразование первого отрезка
    transformed_L2 = transform_line(L[2:], T)  # Преобразование второго отрезка

    # Расчет наклонов
    slope_L1 = calculate_slope(L[:2])
    slope_L2 = calculate_slope(L[2:])
    slope_transformed_L1 = calculate_slope(transformed_L1)
    slope_transformed_L2 = calculate_slope(transformed_L2)

    # Отображение отрезков
    draw_line(screen, center, YELLOW, L[0], L[1])  # Исходный L1
    draw_line(screen, center, YELLOW, L[2], L[3])  # Исходный L2

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
