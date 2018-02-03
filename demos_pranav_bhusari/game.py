import pygame
from math import pi, sin, cos, radians, degrees
pygame.init()

def cross(x1, y1, x2, y2):
    return x1*y2 - y1*x2



BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

size = [100, 100]

#player position
player_x= 50
player_y = 50
theta = 0


screen = pygame.display.set_mode(size)
#screen1 = pygame.display.set_mode(size)

wall_x1 = 70
wall_y1 = 20

wall_x2 = 70
wall_y2 = 70

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:

    clock.tick(10)
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    screen.fill(BLACK)
  
    # Draw on the screen a GREEN line from (0,0) to (50.75) 
    # 5 pixels wide.
    #pygame.draw.line(screen, GREEN, [wall_x1, wall_y1], [wall_x2, wall_y2], 2)

    #draw player sight line
    #pygame.draw.line(screen, WHITE, [50, 50], [cos(radians(90))*5 + 50, sin(radians(90))*5+ 50],2)

    #draw the player
    #pygame.draw.line(screen, RED, [player_x, player_y], [player_x, player_y],2)

    #transform the edges
    transformed_x1 = wall_x1 - player_x
    transformed_y1 = wall_y1 - player_y
    transformed_x2 = wall_x2 - player_x
    transformed_y2 = wall_y2 - player_y
    #trotate arond the player
    transformed_z1 = (transformed_x1 * cos(theta)) + (transformed_y1 * sin(theta))
    transformed_z2 = (transformed_x2 * cos(theta)) + (transformed_y2 * sin(theta))
    transformed_x1 = (transformed_x1 * sin(theta)) - (transformed_y1 * cos(theta))
    transformed_x2 = (transformed_x2 * sin(theta)) - (transformed_y2 * cos(theta))
    
    #pygame.draw.line(screen, GREEN, [50 - transformed_x1, 50 - transformed_z1], [50 - transformed_x2, 50 - transformed_z2],2)
    #pygame.draw.line(screen, BLUE, [50, 50], [50, 50], 1)
    #pygame.draw.line(screen, BLUE, [50, 50], [5, 45], 1)

    if ((transformed_z1 > 0) or (transformed_z2 > 0)):
        ix1 = cross(transformed_x1, transformed_z1, transformed_x2, transformed_z2)
        iz1 = cross(-0.0001, 0.0001, 20, 5)
        det = cross((transformed_x1 - transformed_x2), (transformed_z1 - transformed_z2), (-0.0001 + 20),(0.0001 -5))
        ix1 = cross(ix1, transformed_x1 - transformed_x2, iz1, -0.001 - 20) / det
        iz1 = cross(ix1, transformed_y1 - transformed_y2, iz1, 0.001 - 5) / det

        ix2 = cross(transformed_x1, transformed_z1, transformed_x2, transformed_z2)
        iz2 = cross(0.0001, 0.0001, 20, 5)
        det = cross((transformed_x1 - transformed_x2), (transformed_z1 - transformed_z2), (0.0001 - 20),(0.0001 -5))
        ix2 = cross(ix2, transformed_x1 - transformed_x2, iz2, -0.001 - 20) / det
        iz2 = cross(ix2, transformed_y1 - transformed_y2, iz2, 0.001 - 5) / det

    
                
        d_x1 = -16*transformed_x1 / transformed_z1
        d_y1a = -50 / transformed_z1
        d_y1b = 50 / transformed_z1
        
        d_x2 = -16* transformed_x2 / transformed_z2 
        d_y2a = -50/ transformed_z2
        d_y2b = 50 / transformed_z2

        pygame.draw.line(screen, BLUE, [50 + d_x1, 50 + d_y1a], [50 + d_x2, 50 + d_y2a], 2)
        pygame.draw.line(screen, BLUE, [50 + d_x1, 50 + d_y1b], [50 + d_x2, 50 + d_y2b], 2)
        pygame.draw.line(screen, BLUE, [50 + d_x1, 50 + d_y1a], [50 + d_x1, 50 + d_y1b], 2)
        pygame.draw.line(screen, BLUE, [50 + d_x2, 50 + d_y2a], [50 + d_x2, 50 + d_y2b], 2)

    
    
    pygame.key.set_repeat (0, 100)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        player_y += sin(theta)
        player_x += cos(theta)
    if pressed[pygame.K_s]:
        player_y -= sin(theta)
        player_x -= cos(theta)
    if pressed[pygame.K_e]:
        theta -= radians(5)
    if pressed[pygame.K_q]:
        theta += radians(5)
    if pressed[pygame.K_a]:
        player_y -= cos(theta)
        player_x -= sin(theta)
    if pressed[pygame.K_d]:
        player_y += cos(theta)
        player_x += sin(theta)
      
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
pygame.quit()
