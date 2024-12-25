import pygame
import math
import numpy as np
from time import sleep
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)


class RF:

    def __init__(self, origin, unit_x, unit_y):
        self.origin = origin
        self.unit_x = unit_x
        self.unit_y = unit_y


class Origin:
  
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0


class Unit:
    def __init__(self, pixels):
        self.pixels = pixels


def get_X(rframe, x):
    scale_x = rframe.unit_x.pixels
    x0 = rframe.origin.x0
    return int(scale_x * x + x0)


def get_Y(rframe, y):
    scale_y = rframe.unit_y.pixels
    y0 = rframe.origin.y0
    return int(-scale_y * y + y0)


def draw_axes(screen, rframe, x_min, x_max, y_min, y_max, color):
    pygame.draw.line(screen, color, (get_X(rframe, x_min), get_Y(rframe, 0)),
                     (get_X(rframe, x_max), get_Y(rframe, 0)))
    pygame.draw.line(screen, color, (get_X(rframe, 0), get_Y(rframe, y_min)),
                     (get_X(rframe, 0), get_Y(rframe, y_max)))
    draw_text(screen, rframe, 0, 0, "O", color)


def draw_text(screen, rframe, x, y, text, color):
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (get_X(rframe, x), get_Y(rframe, y)))


def draw_polygon(screen, rframe, points, color):
    coords = [(get_X(rframe, x), get_Y(rframe, y)) for x, y in points]
    pygame.draw.polygon(screen, color, coords, 1)


def alloc_matrix(rows, cols):
    return [[0.0 for _ in range(cols)] for _ in range(rows)]


def copy_matrix(A, B):
    rows, cols = len(A), len(A[0])
    for i in range(rows):
        for j in range(cols):
            B[i][j] = A[i][j]


def multiply_matrix(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    assert cols_A == rows_B, "Matrix dimensions do not match for multiplication."

    C = alloc_matrix(rows_A, cols_B)
    for i in range(rows_A):
        for j in range(cols_B):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(cols_A))
    return C


def matrix_rotation_2d(angle):
    cs = math.cos(angle)
    sn = math.sin(angle)
    return [[cs, -sn], [sn, cs]]


# Main Program
def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Matrix Transformation")
    clock = pygame.time.Clock()

    # Reference frame setup
    origin = Origin(60, 450)
    unit_x = Unit(60)
    unit_y = Unit(60)
    rframe = RF(origin, unit_x, unit_y)

    # Drawing parameters
    points = [[2.0, 0.5], [8.0, 0.5], [8.0, 6.5], [2.0, 6.5]]
    transformed_points = alloc_matrix(4, 2)

    # Scaling parameters
    p = 0.95
    q = 1 - p
    n_iterations = 10

    running = True
    while running:
        draw_axes(screen, rframe, 0.0, 8.0, 0.0, 7.0, GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw and transform polygons
        for k in range(n_iterations):
            
            draw_polygon(screen, rframe, points, CYAN)

            # Transform points
            transformed_points[0][0] = p * points[0][0] + q * points[1][0]
            transformed_points[0][1] = p * points[0][1] + q * points[1][1]
            transformed_points[1][0] = p * points[1][0] + q * points[2][0]
            transformed_points[1][1] = p * points[1][1] + q * points[2][1]
            transformed_points[2][0] = p * points[2][0] + q * points[3][0]
            transformed_points[2][1] = p * points[2][1] + q * points[3][1]
            transformed_points[3][0] = p * points[3][0] + q * points[0][0]
            transformed_points[3][1] = p * points[3][1] + q * points[0][1]

            copy_matrix(transformed_points, points)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
