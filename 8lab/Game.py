#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

#Setting up Fonts

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

coinIcon = pygame.image.load('coin.png')
cX = random.randint(50, 350)
cY = random.randint(10, 300)
cX_change = 0
cY_change = 5
score_coins = 0

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

def coin(x, y):
    DISPLAYSURF.blit(coinIcon, (x, y))


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.speed = random.randint(1, 5)
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40, SCREEN_WIDTH-40), 0))

      def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.speed = random.randint(1, 5)
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        
        if self.rect.left > 40:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH - 40:
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)



#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    coins_scores = font_small.render(str(score_coins), True, BLACK)
    DISPLAYSURF.blit(coins_scores, (370, 10))




    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()



    cY += cY_change
    if cY > 600:
        cX = random.randint(40, 350)
        cY = random.randint(10, 300)

    coin(cX, cY)

    if P1.rect.collidepoint(cX+10, cY+10):
        score_coins += 1
        cX = random.randint(40, 350)
        cY = random.randint(10, 300)

    coins_scores = font_small.render(str(score_coins), True, BLACK)
    DISPLAYSURF.blit(coins_scores, (590, 10))

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))

        pygame.display.update()
        for entity in all_sprites:
               entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()


    pygame.display.update()
    FramePerSec.tick(FPS)
    

