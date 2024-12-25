#  Задание №1.3

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


def draw_line(screen, center, color, start_point, end_point):
    x1, y1 = int(start_point[0] + center[0]), int(center[1] - start_point[1])
    x2, y2 = int(end_point[0] + center[0]), int(center[1] - end_point[1])
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), 3)


def draw_text(screen, text, x, y, color=BLACK):
    font = pygame.font.Font(None, FONT_SIZE)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Transforming Line")
    screen.fill(WHITE)
    center_x = WIDTH / 2
    center_y = HEIGHT / 2
    center = np.array([center_x, center_y])

    # Получение координат отрезка от пользователя
    line_matrix = get_line_from_user()
    transformed_line_matrix = transform_line(line_matrix, np.array([[1, 3], [4, 1]]))  # Выполняем преобразование отрезка

    screen.fill(WHITE)
    draw_line(screen, center, YELLOW, line_matrix[0], line_matrix[1])  # Отрисовка оригинального отрезка
    draw_line(screen, center, MAGENTA, transformed_line_matrix[0],
              transformed_line_matrix[1])  # Отрисовка преобразованного отрезка

    # Вывод текста на экран
    text1 = f"Исходный отрезок: ({line_matrix[0][0]:.2f}, {line_matrix[0][1]:.2f}) - ({line_matrix[1][0]:.2f}, {line_matrix[1][1]:.2f})"
    text2 = f"Преобразованный отрезок: ({transformed_line_matrix[0][0]:.2f}, {transformed_line_matrix[0][1]:.2f}) - ({transformed_line_matrix[1][0]:.2f}, {transformed_line_matrix[1][1]:.2f})"
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
