import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
pygame.display.set_caption('Paint')


run = True

prev, curr = None, None

pen = pygame.image.load('pen.png')
is_pen = False
circle = pygame.image.load('circle.png')
is_circle = False
rectangle = pygame.image.load('rectangle.png')
is_rectangle = False
eraser = pygame.image.load('eraser.png')
is_eraser = True



screen.fill(white)

while run:
    screen.blit(pen, (20, 20))
    screen.blit(eraser, (62, 20))
    screen.blit(circle, (104, 20))
    screen.blit(rectangle, (146, 20))
    pygame.draw.rect(screen, red, (190, 20, 15, 15))
    pygame.draw.rect(screen, green, (215, 20, 15, 15))
    pygame.draw.rect(screen, blue, (240, 20, 15, 15))
    pygame.draw.rect(screen, black, (0, 0, 270, 65), 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if pen.get_rect().collidepoint(x, y):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    prev = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    cur = pygame.mouse.get_pos()
                    if prev:
                        pygame.draw.line(screen, red, prev, cur, 1)
                        prev = cur
                if event.type == pygame.MOUSEBUTTONUP:
                    prev = None
        if event.type == pygame.MOUSEMOTION:
            pass
        if event.type == pygame.MOUSEBUTTONUP:
            pass



    pygame.display.flip()
    clock.tick(30)

pygame.quit()

