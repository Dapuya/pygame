import pygame
import random
import math

# frame
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png')
pygame.display.set_caption("First")
icon = pygame.image.load('galaxy.png')
pygame.display.set_icon(icon)

# p - player
playerIcon = pygame.image.load('player.png')
pX = 370
pY = 480
pX_change = 0

# e = enemy
enemyIcon = []
eX = []
eY = []
eX_change = []
eY_change = []
num_enemies = 6

for i in range(num_enemies):
    enemyIcon.append(pygame.image.load('alien.png'))
    eX.append(random.randint(0, 735))
    eY.append(random.randint(50, 150))
    eX_change.append(4)
    eY_change.append(40)

# b = bullet
bulletIcon = pygame.image.load('bullet.png')
bX = 0
bY = 480
bX_change = 0
bY_change = 40
b_state = 'ready'

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerIcon, (x, y))

def enemy(x, y, i):
    screen.blit(enemyIcon[i], (x, y))

def fire_bullet(x, y):
    global b_state
    b_state = 'fire'
    screen.blit(bulletIcon, (x+16, y+10))

def isCollision(eX, eY, bX, bY):
    distance = math.sqrt((math.pow(eX - bX, 2)) + (math.pow(eY - bY, 2)))
    if distance < 27:
        return True
    else:
        return False

run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pX_change = -5
            if event.key == pygame.K_RIGHT:
                pX_change = 5
            if event.key == pygame.K_SPACE:
                if b_state is 'ready':
                    bX = pX
                    fire_bullet(bX, bY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pX_change = 0

    pX += pX_change
    if pX <= 0:
        pX = 0
    elif pX >= 736:
        pX = 736

    for i in range(num_enemies):

        if eY[i] > 440:
            for j in range(num_enemies):
                eY[j] = 2000
            game_over()
            break

        eX[i] += eX_change[i]
        if eX[i] <= 0:
            eX_change[i] = 4
            eY[i] += eY_change[i]
        elif eX[i] >= 736:
            eX_change[i] = -4
            eY[i] += eY_change[i]

        collision = isCollision(eX[i], eY[i], bX, bY)
        if collision:
            bY = 480
            b_state = 'ready'
            score_value += 1
            eX[i] = random.randint(0, 736)
            eY[i] = random.randint(50, 150)

        enemy(eX[i], eY[i], i)

    if bY <= 0:
        bY = 480
        b_state = 'ready'

    if b_state is 'fire':
        fire_bullet(bX, bY)
        bY -= bY_change


    player(pX, pY)
    show_score(textX, textY)
    pygame.display.update()

