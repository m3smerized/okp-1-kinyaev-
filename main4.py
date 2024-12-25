# Задание №1.4

import pygame
import numpy as np

# Размеры окна
WIDTH = 1200
HEIGHT = 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
FONT_SIZE = 20

T = np.array([[1, 2], [3, 1]])
L = np.array([[0, 100], [200, 300]], dtype=float)


def get_line_from_user():
    while True:
        try:
            x1 = float(input("Введите x1 для отрезка: "))
            y1 = float(input("Введите y1 для отрезка: "))
            x2 = float(input("Введите x2 для отрезка: "))
            y2 = float(input("Введите y2 для отрезка: "))
            return np.array([[x1, y1], [x2, y2]])  # Матрица координат отрезка
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")


def transform_line(line_matrix, transformation_matrix):
    transformed_matrix = np.dot(line_matrix, transformation_matrix)
    return transformed_matrix


def draw_line(screen, center, color, start_point, end_point, width=3):
    x1, y1 = int(start_point[0] + center[0]), int(center[1] - start_point[1])
    x2, y2 = int(end_point[0] + center[0]), int(center[1] - end_point[1])
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), width)


def draw_text(screen, text, x, y, color=BLACK):
    font = pygame.font.Font(None, FONT_SIZE)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def get_midpoint(line_matrix):
    start_point = line_matrix[0]
    end_point = line_matrix[1]
    return (start_point + end_point) / 2


def draw_circle(screen, center, color, pos, radius):
    x, y = int(pos[0] + center[0]), int(center[1] - pos[1])
    pygame.draw.circle(screen, color, (x, y), radius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Line Transformation")
    screen.fill(WHITE)

    # смещаем центр чтобы оба отрезка поместились на экране
    center_x = 100
    center_y = 700
    center = np.array([center_x, center_y])

    transformed_L = transform_line(L, T)  # Преобразование отрезка
    midpoint_L = get_midpoint(L) # Нахождение середины исходного отрезка
    midpoint_transformed_L = get_midpoint(transformed_L) # Нахождение середины преобразованного отрезка

    draw_line(screen, center, YELLOW, L[0], L[1]) # Отрисовка оригинального отрезка
    draw_line(screen, center, BLUE, transformed_L[0], transformed_L[1]) # Отрисовка преобразованного отрезка
    draw_line(screen, center, GREEN, midpoint_L, midpoint_transformed_L, 2) # Соединяющая линия

    draw_circle(screen, center, RED, midpoint_L, 6) # Круг середины исходного отрезка
    draw_circle(screen, center, RED, midpoint_transformed_L, 6) # Круг середины преобразованного отрезка

    text1 = f"Исходный отрезок: ({L[0][0]:.2f}, {L[0][1]:.2f}) - ({L[1][0]:.2f}, {L[1][1]:.2f})"
    text2 = f"Преобразованный отрезок: ({transformed_L[0][0]:.2f}, {transformed_L[0][1]:.2f}) - ({transformed_L[1][0]:.2f}, {transformed_L[1][1]:.2f})"

    draw_text(screen, text1, 10, 10)
    draw_text(screen, text2, 10, 40)

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
