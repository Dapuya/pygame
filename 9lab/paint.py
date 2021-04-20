import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 140, 0)
pi = 3.14


screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
pygame.display.set_caption('Paint')
font1 = pygame.font.SysFont('serif', 20)
font2 = pygame.font.SysFont('arial', 15)
font3 = pygame.font.SysFont('arial', 30)

run = True

prev, cur, lx, ly = None, None, None, None


is_pen = False
is_circle = False
is_rect = False
is_eraser = False
click = False
color = (0, 0, 0)



red_color_rect = pygame.Rect(20, 20, 30, 30)
blue_color_rect = pygame.Rect(60, 20, 30, 30)
green_color_rect = pygame.Rect(20, 60, 30, 30)
orange_color_rect = pygame.Rect(60, 60, 30, 30)
pen_rect = pygame.Rect(110, 20, 50, 25)
circle_rect = pygame.Rect(170, 20, 50, 25)
eraser_rect = pygame.Rect(230, 20, 60, 25)
rectangle_rect = pygame.Rect(110, 55, 80, 25)
pen = font2.render("Pen", True, BLACK)
circle = font2.render("Circle", True, BLACK)
rectangle = font2.render("Rectangle", True, BLACK)
eraser = font2.render("Eraser", True, BLACK)
radius = font2.render("Radius :", True, BLACK)
radius1 = font3.render(str(30), True, BLACK)

imagecount = 1


def show_instructions():
    pygame.draw.rect(screen, WHITE, (0, 0, 400, 130))
    pygame.draw.rect(screen, BLACK, (0, 0, 401, 131), 1)
    pygame.draw.rect(screen, RED, red_color_rect)
    pygame.draw.rect(screen, BLUE, blue_color_rect)
    pygame.draw.rect(screen, GREEN, green_color_rect)
    pygame.draw.rect(screen, ORANGE, orange_color_rect)
    pygame.draw.rect(screen, WHITE, pen_rect, 2)
    pygame.draw.rect(screen, WHITE, circle_rect, 2)
    pygame.draw.rect(screen, WHITE, eraser_rect, 2)
    pygame.draw.rect(screen, WHITE, rectangle_rect, 2)

    screen.blit(pen, (115, 25))
    screen.blit(circle, (175, 25))
    screen.blit(rectangle, (115, 60))
    screen.blit(eraser, (235, 25))
    screen.blit(radius, (310, 25))
    screen.blit(radius1, (320, 45))

screen.fill(WHITE)

def draw_circle(color, (x, y)):
    pygame.draw.circle(screen, color, (x, y), 30, 1)


while run:
    mx, my = pygame.mouse.get_pos()
    if pen_rect.collidepoint((mx, my)):
        if click:
            is_pen = True
            is_eraser = False
            is_rect = False
            is_circle = False
    if circle_rect.collidepoint((mx, my)):
        if click:
            is_circle = True
            is_pen = False
            is_eraser = False
            is_rect = False
    if rectangle_rect.collidepoint((mx, my)):
        if click:
            is_rect = True
            is_pen = False
            is_circle = False
            is_eraser = False
    if eraser_rect.collidepoint((mx, my)):
        if click:
            is_eraser = True
            is_pen = False
            is_circle = False
            is_rect = False
    if red_color_rect.collidepoint((mx, my)):
        if click:
            color = RED
    if green_color_rect.collidepoint((mx, my)):
        if click:
            color = GREEN
    if blue_color_rect.collidepoint((mx, my)):
        if click:
            color = BLUE
    if orange_color_rect.collidepoint((mx, my)):
        if click:
            color = ORANGE
    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            lx, ly = pygame.mouse.get_pos()
            if event.button == 1:
                click = True
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
            lx, ly = None, None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if imagecount < 10:
                    imagecount = "0" + str(imagecount)
                pygame.image.save(screen, "image{}.png".format(imagecount))
                imagecount = int(imagecount)
                imagecount += 1

    if is_pen:
        if prev:
            pygame.draw.aaline(screen, color, prev, cur, 1)
            prev = cur

    if is_circle:
        if prev:
            draw_circle(color, prev)

    if is_eraser:
        if prev:
            pygame.draw.circle(screen, WHITE, prev, 20)
            prev = cur

    if is_rect:
        if prev:
            pygame.draw.rect(screen, color, (lx, ly, 150, 50), 2)

    show_instructions()
    pygame.display.update()
    clock.tick(30)

pygame.quit()

