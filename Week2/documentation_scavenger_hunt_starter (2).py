"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
SEA_GREEN= (13, 255, 112)
SKY_BLUE= (12, 218, 255)
LEPRECHAUN= (73, 220, 75)
FOAM_GREEN= (12, 232, 133)
ORANGE= (255, 80, 13)
YELLOW= (255, 244, 25)
MAGENTA= (255, 25, 113)
PURPLE= (95, 25, 113)

pygame.init()

# Set the width and height of the screen [width, height]
#**size= (700, 500)
#**screen= pygame.display.set_mode(size)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE







# -------- Main Program Loop -----------
x=350
y=250
x_speed=random.randint(-10,10)
y_speed= random.randint(-10, 10)
size=random.randint(20,80)
colors= [BLACK, WHITE, GREEN, RED, BLUE, GREY, SEA_GREEN, SKY_BLUE, LEPRECHAUN, FOAM_GREEN, ORANGE, YELLOW, MAGENTA, PURPLE]
color= random.choice(colors)
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # --- Game logic should go here
#**put in score, lives here
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(color)
    #**then redraw what is going on

    # --- Drawing code should go here
    color= random.choice(colors)
    pygame.draw.circle(screen, color, [x, y], size)
    x+=x_speed
    y+=y_speed
    if (y >=500): 
        y_speed = -2
    elif y<=0 :
        y_speed = 2
    if (x >=700):
        x_speed= -2
    elif x<=0:
        x_speed= 2
        
        
    #**anything that changes position of object would go here


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
