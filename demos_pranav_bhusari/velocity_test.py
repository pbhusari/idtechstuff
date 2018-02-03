import pygame
from math import sin, cos, radians, degrees, atan
import random
pi = 3.141592
pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)    
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

size = (1000, 1000)

def isonscreen(x, y):
    if x > 1000 or y > 1000:
        return False
    elif x < 0 or y < 0:
        return False
    else:
        return True

def onbounds(x, y):
    if x == 1000 or y == 1000:
        return True
    elif x == 0 or y == 0:
        return True
    else:
        return False

    
def draw_shoot(x1, y1, theta):

    pos_multi = 10

    bullet_x = (x1 + pos_multi*(cos(theta))) // 1
    bullet_y = (y1 + pos_multi*(sin(theta))) // 1

    c = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    #pygame.draw.rect(screen, c,[bullet_x, bullet_y, bullet_x, bullet_y])

    while isonscreen(bullet_x, bullet_y):
        
        pygame.draw.rect(screen, c,[bullet_x, bullet_y, bullet_x, bullet_y],  1)
        pos_multi += 10
        
        bullet_x = (x1 + pos_multi*(cos(theta))) // 1
        bullet_y = (y1 + pos_multi*(sin(theta))) // 1



bullets = []
player_x = 50
player_y = 500
player_velocity_x = 0
player_velocity_y = 0
player_acceleration_x = 0
player_acceleration_y = 0
time = 0
screen = pygame.display.set_mode(size)
angle = 0

done = False
clock = pygame.time.Clock()


while not done:

    time += 1
    clock.tick(30)
    
    screen.fill(BLACK)
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    player_x += player_velocity_x*(time) + (1/2)*(player_acceleration_x )*(pow(time, 2))
    player_y += player_velocity_y*(time) + (1/2)*(player_acceleration_y)*(pow(time, 2))
    
    pygame.draw.line(screen, WHITE, [player_x, player_y], [player_x , player_y], 1)
                     
    mpos = pygame.mouse.get_pos()

    magnitude = pow((pow(mpos[1], 2) + pow(mpos[0], 2)),0.5) 
    
    dx = (mpos[0] - player_x)
    dy = (mpos[1] - player_y)

    if dx  >  0:
        angle = atan(dy/dx)
    elif dx == 0 and  dy > 0:
        angle = pi / 2
    elif dx == 0 and dy < 0:
        angle = 3* pi/2
    elif dx < 0 and dy == 0:
        angle = pi
    elif dx < 0 and dy < 0:
        angle = pi + atan(dy/dx)
    elif dx < 0 and dy > 0:
        angle = pi + atan(dy/dx)

    
    pygame.draw.line(screen, RED, [player_x, player_y], [player_x + 10*cos(angle), player_y + 10*sin(angle)], 5)
    
    pygame.key.set_repeat (0, 100)
    pressed = pygame.key.get_pressed()

    
##    if pressed[pygame.K_w]:
##        player_acceleration_y += 1
##    if pressed[pygame.K_s]:
##        player_acceleration_y -= 1
##    if pressed[pygame.K_a]:
##        player_acceleration_x -= 1
##    if pressed[pygame.K_d]:
##        player_acceleration_x += 1

    if onbounds(player_x, player_y):
        player_acceleration_x = 0
        player_acceleration_y = 0
        player_velocity_x = -player_velocity_x
        player_velocity_y = -player_velocity_y

    if pressed[pygame.K_q]:
        #draw_shoot(player_x, player_y, angle)
        player_acceleration_x += magnitude*cos(angle)*0.0000001
        player_acceleration_y += magnitude*sin(angle)*0.0000001

    pygame.display.flip()

pygame.quit()
