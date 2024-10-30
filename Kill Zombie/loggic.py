import pygame
import random
import math
from pygame import mixer

#initialize
pygame.init()

#game window
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space invaders')
#icon = pygame.image.load('Kill Zombie/logo.png')
#pygame.display.set_icon(icon)

# background
background = pygame.image.load('Kill Zombie/background.png')

#player
player_img = pygame.image.load('Kill Zombie/player.png')
px,py = 368, 500
pc = 0

def player(x,y):
    screen.blit(player_img, (px,py)) #draw player

#enemy
enemy_img = []
ex,ey = [], []
exc = []
eyc = []
num = 6

for i in range(num):
    enemy_img.append(pygame.image.load('Kill Zombie/enemy.png'))
    ex.append(random.randint(0,735))
    ey.append(0)
    exc.append(3)
    eyc.append(40)

def enemy(x,y, i):
    screen.blit(enemy_img[i], (ex[i],ey[i])) #draw enemy

#bullet
bullet_img = pygame.image.load('Kill Zombie/bullet.png')
bx,by = px+8, py
b_state = 'ready'

def fire(x, y):
    global b_state
    b_state = 'fire'
    screen.blit(bullet_img, (x+16, y-16))

# collision logic
def Collision(i,ex,ey,bx,by):
    distance = math.sqrt((math.pow(ex[i]-bx, 2)) + (math.pow(ey[i]-by, 2)))
    if distance < 27:
        return True
    else:
        return False

#score
score_value = 0
font = pygame.font.Font('Kill Zombie/calibrib.ttf', 32)

def show_score(x,y):
    score = font.render(f"Score : {str(score_value)}", True, (255, 255, 255))
    screen.blit(score, (x,y))

#game logic
running = True
while running:
    #fill the window
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keypreses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pc = -3

            elif event.key == pygame.K_RIGHT:
                pc = 3

            elif event.key == pygame.K_SPACE:
                if b_state == 'ready':
                    bx = px + 8
                    fire(bx, by)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pc = 0

#updating the screen
    px += pc
    if px <= 0: #player limitation
        px = 0
    elif px  >= 736:
        px = 736

    for i in range(num):
        ex[i] += exc[i]
        if ex[i] <= 0: #enemy movement
            exc[i] = 3
            ey[i] += eyc[i]
        elif ex[i]  >= 736:
            exc[i] = -3
            ey[i] += eyc[i]

        collision = Collision(i,ex,ey,bx,by) #check collision
        if collision:
            by = py
            b_state = 'ready'
            score_value += 1
            ex[i],ey[i] = random.randint(0,736), 0

        enemy(ex[i],ey[i], i)

    if by <= 0:
        by = py
        b_state = 'ready'
    if b_state == 'fire': #bullet movement
        fire(bx, by)
        by -= 10

    player(px,py)
    show_score(10,10) 
    pygame.display.update()