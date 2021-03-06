import pygame
import time
import random

pygame.init()

FPS = 30
clock = pygame.time.Clock()
WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
font1 = pygame.font.SysFont('arial', 25)
font2 = pygame.font.SysFont('arial', 45)
font_for_levels = pygame.font.SysFont('arial', 20)


class Snake:
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.elements = [[100, 200], [120, 200], [140, 200]]
        self.dx = 5
        self.dy = 0
        self.is_add = True
        self.score = 0
        self.level = 1
        self.block = 5
        self.is_level_2 = False
        self.is_level_3 = False
        self.color = (0, 0, 0)

    def draw(self):
        for elem in self.elements:
            pygame.draw.circle(screen, self.color, elem, self.radius)

    def add_snake(self):
        if not self.is_add:
            self.size += 1
            self.score += 1
            self.elements.append([0, 0])
            self.is_add = True

    def move(self):
        if not self.is_add:
            self.add_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy


class Food:
    def __init__(self):
        self.x = random.randint(70, 270)
        self.y = random.randint(70, 120)
        self.food_image = pygame.image.load('apple.png')

    def draw(self):
        screen.blit(self.food_image, (self.x, self.y))


def Collision_1():
    if (food1.x in range(snake1.elements[0][0] - 20, snake1.elements[0][0])) and (food1.y in range(snake1.elements[0][1] - 20, snake1.elements[0][1])):
        snake1.is_add = False
        food1.x = random.randint(340, 430)
        food1.y = random.randint(150, 330)
    if (food2.x in range(snake1.elements[0][0] - 20, snake1.elements[0][0])) and (food2.y in range(snake1.elements[0][1] - 20, snake1.elements[0][1])):
        snake1.is_add = False
        food2.x = random.randint(70, 270)
        food2.y = random.randint(70, 100)


def Collision_2():
    if (food1.x in range(snake1.elements[0][0] - 20, snake1.elements[0][0])) and (food1.y in range(snake1.elements[0][1] - 20, snake1.elements[0][1])):
        snake1.is_add = False
        food1.x = random.randint(340, 430)
        food1.y = random.randint(150, 330)
    if (food1.x in range(snake2.elements[0][0] - 20, snake2.elements[0][0])) and (food1.y in range(snake2.elements[0][1] - 20, snake2.elements[0][1])):
        snake2.is_add = False
        food1.x = random.randint(70, 270)
        food1.y = random.randint(390, 430)
    if (food2.x in range(snake1.elements[0][0] - 20, snake1.elements[0][0])) and (food2.y in range(snake1.elements[0][1] - 20, snake1.elements[0][1])):
        snake1.is_add = False
        food2.x = random.randint(70, 270)
        food2.y = random.randint(70, 100)
    if (food2.x in range(snake2.elements[0][0] - 20, snake2.elements[0][0])) and (food2.y in range(snake2.elements[0][1] - 20, snake2.elements[0][1])):
        snake2.is_add = False
        food2.x = random.randint(340, 430)
        food2.y = random.randint(350,440)


wall1_image = pygame.image.load('wall1.png')
wall2_image = pygame.image.load('wall2.png')


def wall1():
    for i in range(0, WIDTH, 15):
        screen.blit(wall1_image, (0, i))
        screen.blit(wall1_image, (WIDTH - 32, i))


def wall2():
    for i in range(32, WIDTH-45, 15):
        screen.blit(wall2_image, (i, 0))
        screen.blit(wall2_image, (i, HEIGHT - 32))


def out_of_borders_1():
    if (snake1.elements[0][0] < 40) or (snake1.elements[0][0] > WIDTH - 40) or (snake1.elements[0][1] < 40) or (snake1.elements[0][1] > HEIGHT - 40):
        return True

    if snake1.is_level_2:
        if 145 < snake1.elements[0][0] < 440 and 120 < snake1.elements[0][1] < 152:
            return True
        if 145 < snake1.elements[0][0] < 440 and 345 < snake1.elements[0][1] < 384:
            return True

    if snake1.is_level_3:
        if 284 < snake1.elements[0][0] < 316 and 220 < snake1.elements[0][1] < 270:
            return True


def out_of_borders_2():
    if (snake1.elements[0][0] < 40) or (snake1.elements[0][0] > WIDTH - 40) or (snake1.elements[0][1] < 40) or (snake1.elements[0][1] > HEIGHT - 40):
        return True
    if (snake2.elements[0][0] < 40) or (snake2.elements[0][0] > WIDTH - 40) or (snake2.elements[0][1] < 40) or (snake2.elements[0][1] > HEIGHT - 40):
        return True

    if snake1.is_level_2:
        if 145 < snake1.elements[0][0] < 440 and 120 < snake1.elements[0][1] < 152:
            return True
        if 145 < snake1.elements[0][0] < 440 and 345 < snake1.elements[0][1] < 384:
            return True
    if snake2.is_level_2:
        if 140 < snake2.elements[0][0] < 440 and 120 < snake2.elements[0][1] < 152:
            return True
        if 140 < snake2.elements[0][0] < 440 and 350 < snake2.elements[0][1] < 384:
            return True

    if snake1.is_level_3:
        if 284 < snake1.elements[0][0] < 316 and 220 < snake1.elements[0][1] < 270:
            return True
    if snake2.is_level_3:
        if 284 < snake2.elements[0][0] < 316 and 220 < snake2.elements[0][1] < 270:
            return True


def show_score_1():
    show = font1.render('Score of R: ' + str(snake1.score), True, (0, 0, 0))
    screen.blit(show, (35, 30))


def show_score_2():
    show = font1.render('Score of R: ' + str(snake1.score), True, (0, 0, 0))
    show2 = font1.render('Score of B: ' + str(snake2.score), True, (0, 0, 0))
    screen.blit(show, (35, 30))
    screen.blit(show2, (410, 30))


def show_level_2_player():
    show_level_1 = font_for_levels.render('Level of R: ' + str(snake1.level), True, (0, 0, 0))
    show_level_2 = font_for_levels.render('Level of B: ' + str(snake2.level), True, (0, 0, 0))
    screen.blit(show_level_1, (35, 55))
    screen.blit(show_level_2, (440, 55))


def show_level_1_player():
    show_level_1 = font_for_levels.render('Level of R: ' + str(snake1.level), True, (0, 0, 0))
    screen.blit(show_level_1, (35, 55))


def game_over_1():
    with open('scores.txt', 'a') as f:
        f.write('\n\n\nScore of R: ' + str(snake1.score) + '\nLevel of R: ' + str(snake1.level))
        f.close()

    screen.fill((220, 253, 218))
    over = font2.render("GAME OVER!", True, (0, 0, 0))
    score_1 = font1.render('Score of R: ' + str(snake1.score), True, (0, 0, 0))
    level_1 = font_for_levels.render('Level of R: ' + str(snake1.level), True, (0, 0, 0))
    screen.blit(over, (150, 170))
    screen.blit(score_1, (45, 300))
    screen.blit(level_1, (45, 330))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()


def game_over_2():
    with open('scores.txt', 'a') as f:
        f.write('\n\n\nScore of R: ' + str(snake1.score) + '\nLevel of R: ' + str(snake1.level))
        f.write('\n\nScore of B: ' + str(snake2.score) + '\nLevel of B: ' + str(snake2.level))
        f.close()

    screen.fill((220, 253, 218))
    over = font2.render("GAME OVER!", True, (0, 0, 0))
    score_1 = font1.render('Score of R: ' + str(snake1.score), True, (0, 0, 0))
    score_2 = font1.render('Score of B: ' + str(snake2.score), True, (0, 0, 0))
    level_1 = font_for_levels.render('Level of R: ' + str(snake1.level), True, (0, 0, 0))
    level_2 = font_for_levels.render('Level of B: ' + str(snake2.level), True, (0, 0, 0))
    screen.blit(over, (150, 170))
    screen.blit(score_1, (45, 300))
    screen.blit(score_2, (400, 300))
    screen.blit(level_1, (45, 330))
    screen.blit(level_2, (400, 330))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()


def walls_of_level2():
    for i in range(160, 420, 15):
        screen.blit(wall2_image, (i, 120))
        screen.blit(wall2_image, (i, 350))


def walls_of_level3():
    for i in range(230, 260, 15):
        screen.blit(wall1_image, (284, i))


def level_changing_1():
    if snake1.score > 8:
        snake1.level = 2
        snake1.block = 7
        walls_of_level2()
    if snake1.score > 16:
        snake1.level = 3
        snake1.block = 9
        walls_of_level3()


def level_changing_2():
    if snake1.score > 8:
        snake1.level = 2
        snake1.block = 7
        walls_of_level2()
    if snake1.score > 16:
        snake1.level = 3
        snake1.block = 9
        walls_of_level3()
    if snake2.score > 8:
        snake2.level = 2
        snake2.block = 7
        walls_of_level2()
    if snake2.score > 16:
        snake2.level = 3
        snake2.block = 9
        walls_of_level3()


snake1 = Snake()
snake1.color = (255, 0, 0)
food1 = Food()
snake2 = Snake()
snake2.color = (0, 0, 255)
food2 = Food()

seconds_of_level_2_for_R = []
seconds_of_level_3_for_R = []

seconds_of_level_2_for_B = []
seconds_of_level_3_for_B = []


def Menu():
    click = False
    menu = True
    snake_image = pygame.image.load('snake.png')
    while menu:
        screen.fill((220, 253, 218))
        player_1 = pygame.Rect(90, 230, 200, 60)
        player_2 = pygame.Rect(345, 230, 200, 60)
        pygame.draw.rect(screen, (220, 253, 218), player_1)
        pygame.draw.rect(screen, (220, 253, 218), player_2)
        screen.blit(snake_image, (250, 77))
        txt_for_player_1 = font2.render("1 player", True, (0, 64, 1))
        txt_for_player_2 = font2.render("2 players", True, (0, 64, 1))
        screen.blit(txt_for_player_1, (100, 232))
        screen.blit(txt_for_player_2, (355, 232))

        mx, my = pygame.mouse.get_pos()
        if player_1.collidepoint((mx, my)):
            if click:
                Player_1()
        if player_2.collidepoint((mx, my)):
            if click:
                Player_2()

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


def Player_2():
    run1 = True
    while run1:
        screen.fill((220, 253, 218))
        mil = clock.tick(FPS)
        curr = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake1.dx = -snake1.block
                    snake1.dy = 0
                if event.key == pygame.K_RIGHT:
                    snake1.dx = snake1.block
                    snake1.dy = 0
                if event.key == pygame.K_UP:
                    snake1.dx = 0
                    snake1.dy = -snake1.block
                if event.key == pygame.K_DOWN:
                    snake1.dx = 0
                    snake1.dy = snake1.block
                if event.key == pygame.K_a:
                    snake2.dx = -snake2.block
                    snake2.dy = 0
                if event.key == pygame.K_d:
                    snake2.dx = snake2.block
                    snake2.dy = 0
                if event.key == pygame.K_w:
                    snake2.dx = 0
                    snake2.dy = -snake2.block
                if event.key == pygame.K_s:
                    snake2.dx = 0
                    snake2.dy = snake2.block

        if out_of_borders_2():
            game_over_2()
            run1 = False

        if snake1.score == 9:
            seconds_of_level_2_for_R.append(pygame.time.get_ticks())

        if snake1.score > 8 and (curr - seconds_of_level_2_for_R[0]) > 3000:
            snake1.is_level_2 = True

        if snake1.score == 17:
            seconds_of_level_3_for_R.append(pygame.time.get_ticks())

        if snake1.score > 16 and (curr - seconds_of_level_3_for_R[0]) > 3000:
            snake1.is_level_3 = True

        if snake2.score == 9:
            seconds_of_level_2_for_B.append(pygame.time.get_ticks())

        if snake2.score > 8 and (curr - seconds_of_level_2_for_B[0]) > 3000:
            snake2.is_level_2 = True

        if snake2.score == 17:
            seconds_of_level_3_for_B.append(pygame.time.get_ticks())

        if snake2.score > 16 and (curr - seconds_of_level_3_for_B[0]) > 3000:
            snake2.is_level_3 = True

        Collision_2()
        snake1.move()
        snake2.move()
        snake1.draw()
        snake2.draw()
        food1.draw()
        food2.draw()
        wall1()
        wall2()
        show_score_2()
        show_level_2_player()
        level_changing_2()
        pygame.display.flip()


def Player_1():
    run = True
    while run:
        screen.fill((220, 253, 218))
        mil = clock.tick(FPS)
        curr = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake1.dx = -snake1.block
                    snake1.dy = 0
                if event.key == pygame.K_RIGHT:
                    snake1.dx = snake1.block
                    snake1.dy = 0
                if event.key == pygame.K_UP:
                    snake1.dx = 0
                    snake1.dy = -snake1.block
                if event.key == pygame.K_DOWN:
                    snake1.dx = 0
                    snake1.dy = snake1.block

        if out_of_borders_1():
            game_over_1()
            run = False

        if snake1.score == 9:
            seconds_of_level_2_for_R.append(pygame.time.get_ticks())

        if snake1.score > 8 and (curr - seconds_of_level_2_for_R[0]) > 3000:
            snake1.is_level_2 = True

        if snake1.score == 17:
            seconds_of_level_3_for_R.append(pygame.time.get_ticks())

        if snake1.score > 16 and (curr - seconds_of_level_3_for_R[0]) > 3000:
            snake1.is_level_3 = True

        Collision_1()
        snake1.move()
        snake1.draw()
        food1.draw()
        food2.draw()
        wall1()
        wall2()
        show_score_1()
        show_level_1_player()
        level_changing_1()
        pygame.display.flip()

Menu()