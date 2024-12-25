# Практическое задание №1.1

import pygame
import numpy as np

# Размеры окна
WIDTH = 600
HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FONT_SIZE = 20


def get_point_from_user():
    while True:
        try:
            x = float(input("Введите координату x: "))
            y = float(input("Введите координату y: "))
            return np.array([x, y])
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")


def transform_point(point, transform_matrix):
    transformed_point = np.dot(transform_matrix, point)
    return transformed_point  # Возвращаем только x и y


def draw_points(screen, point1, point2, center):
    x1, y1 = int(point1[0] + center[0]), int(center[1] - point1[1])
    x2, y2 = int(point2[0] + center[0]), int(center[1] - point2[1])

    pygame.draw.circle(screen, RED, (x1, y1), 5)  # Исходная точка
    pygame.draw.circle(screen, GREEN, (x2, y2), 5)  # Преобразованная точка

    pygame.display.update()


def draw_text(screen, text, x, y, color=BLACK, font_size=FONT_SIZE):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Transformation Visualization")
    screen.fill(WHITE)

    center_x = WIDTH / 2
    center_y = HEIGHT / 2
    center = np.array([center_x, center_y])

    point = get_point_from_user()  # Получаем координаты точки от пользователя
    T = np.array([[1, 3], [4, 1]])  # Матрица трансформации
    transformed_point = transform_point(point, T)  # Выполняем трансформацию

    draw_points(screen, point[:2], transformed_point, center)  # Визуализация

    text1 = f"Исходные координаты: ({point[0]:.2f}, {point[1]:.2f})"
    text2 = f"Преобразованные координаты: ({transformed_point[0]:.2f}, {transformed_point[1]:.2f})"
    draw_text(screen, text1, 10, 10)
    draw_text(screen, text2, 10, 40)
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()  # Перерисовываем экран для обновления
    pygame.quit()


if __name__ == "__main__":
    main()
