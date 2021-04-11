import pygame
import math

class Point:
    # constructed using a normal tupple
    def __init__(self, point_t = (0,0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)

def draw_dashed_line(surf, color, start_pos, end_pos, width=3, dash_length=10):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement.__div__(length)
    for index in range(0, int(length/dash_length), 2):
        start = origin + (slope *    index    * dash_length)
        end = origin + (slope * (index + 1) * dash_length)
        pygame.draw.line(surf, color, start.get(), end.get(), width)


pygame.init()

screen = pygame.display.set_mode((980, 590))

pygame.display.set_caption('SinCos')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
pi = 3.14159

vertical = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
horizontal = ['-3pi', '-2.5pi', '-2pi', '-1.5pi', '-pi', '-0.5pi', '  0', ' 0.5pi', ' pi', ' 1.5pi', ' 2pi', ' 2.5pi', ' 3pi']
font = pygame.font.SysFont('arial', 15)
cnt_for_vertical = len(vertical)
cnt_for_horizontal = len(horizontal)

l1, l2, l3, l4 = '2', '_', 'sin x', 'cos x'

common_counter = 0
from math import sin
run = True
while run:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # frame
    pygame.draw.line(screen, black, (50, 20), (930, 20), 2)
    pygame.draw.line(screen, black, (50, 540), (930, 540), 2)
    pygame.draw.line(screen, black, (50, 20), (50, 540), 2)
    pygame.draw.line(screen, black, (930, 20), (930, 540), 2)

    # x & y axes
    pygame.draw.line(screen, black, (50, 280), (930, 280), 2)
    pygame.draw.line(screen, black, (490, 20), (490, 540), 2)

    # grid
    for i in range(40, 530, 60):
        pygame.draw.line(screen, black, (50, i), (930, i), 1)
    for i in range(70, 930, 140):
        pygame.draw.line(screen, black, (i, 20), (i, 540), 1)

    # vertical divisions:
    #  left side divisions
    for i in range(40, 530, 30):
        pygame.draw.line(screen, black, (50, i), (60, i), 1)
    for i in range(40, 530, 15):
        pygame.draw.line(screen, black, (50, i), (55, i), 1)
    #  right side divisions
    for i in range(40, 530, 30):
        pygame.draw.line(screen, black, (920, i), (930, i), 1)
    for i in range(40, 530, 15):
        pygame.draw.line(screen, black, (925, i), (930, i), 1)

    # horizontal divisions
    #  upper divisions
    for i in range(140, 910, 140):
        pygame.draw.line(screen, black, (i, 20), (i, 35), 1)
    for i in range(105, 910, 70):
        pygame.draw.line(screen, black, (i, 20), (i, 30), 1)
    for i in range(87, 910, 35):
        pygame.draw.line(screen, black, (i, 20), (i, 25), 1)
    # lower divisions
    for i in range(140, 910, 140):
        pygame.draw.line(screen, black, (i, 525), (i, 540), 1)
    for i in range(105, 910, 70):
        pygame.draw.line(screen, black, (i, 530), (i, 540), 1)
    for i in range(87, 910, 35):
        pygame.draw.line(screen, black, (i, 535), (i, 540), 1)

    for i in range(33, 541, 60):
        vertical_text = font.render(vertical[common_counter], True, black)
        screen.blit(vertical_text, (10, i))
        common_counter += 1
        if common_counter == cnt_for_vertical:
            break
    common_counter = 0

    for i in range(60, 930, 70):
        horizontal_text = font.render(horizontal[common_counter], True, black)
        screen.blit(horizontal_text, (i, 550))
        common_counter += 1
        if common_counter == cnt_for_horizontal:
            break
    common_counter = 0

    # graph
    # cos
    for x in range(70, 910):
        if x % 4 == 2:
            pygame.draw.aaline(screen, blue, (x, int(280 + (240 * sin(3.5 * ((float(x) / 980) * 2 * pi))))),
                               (x + 1, int(280 + (240 * sin(3.5 * ((float(x + 1) / 980) * 2 * pi))))), 3)
        if x % 4 == 0:
            pygame.draw.aaline(screen, white, (x, int(280 + (240 * sin(3.5 * ((float(x) / 980) * 2 * pi))))),
                               (x + 1, int(280 + (240 * sin(3.5 * ((float(x + 1) / 980) * 2 * pi))))), 3)

        # pygame.draw.aaline(screen, blue, (x, int(280 + (240 * sin(3.5 * ((float(x) / 980) * 2 * pi))))),
        #                    (x + 1, int(280 + (240 * sin(3.5 * ((float(x + 1) / 980) * 2 * pi))))), 3)
        pygame.draw.aaline(screen, red, (x, int(280 + (240 * sin(3.5 * ((float(x) / 980) * 2 * pi) - pi / 2)))),
                           (x + 1, int(280 + (240 * sin(3.5 * ((float(x + 1) / 980) * 2 * pi) - pi / 2)))), 3)


    pygame.display.flip()
