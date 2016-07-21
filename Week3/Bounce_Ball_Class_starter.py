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
 



pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]


# BOUNCING BALL CLASS CODE  

class BouncingBall(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, colors, screen_width, screen_height):

        x_speed = random.randint(-10, 10)
        y_speed = random.randint(-10, 10)

        x_location = 350
        y_location = 250

        ball_color = random.choice(colors) # This is outside because of variable scoping.

        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        self.screen = screen
        self.colors = colors
        self.screen_width = screen_width
        self.screen_height = screen_height

        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)


        

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN) 
    


    # --- Drawing code should go here
    # ball_color = random.choice(colors)
    # x_location=350
    # y_location=250
    # ball_size = random.randint(10, 30)
    # x_speed = random.randint(-10, 10)
    # y_speed = random.randint(-10, 10)

    # pygame.draw.circle(screen, ball_color, [x_location, y_location], ball_size)


    # if x_location >= SCREEN_WIDTH - ball_size or x_location < ball_size:
    #     x_speed = x_speed * -1

    # if y_location >= SCREEN_HEIGHT - ball_size or y_location < ball_size:
    #     y_speed = y_speed * -1


    # x_location += x_speed
    # y_location += y_speed

        

    Ball_1= BouncingBall(random.randint(SCREEN_WIDTH/2), random.randint(SCREEN_HEIGHT/2) 2, 2, 1, 100)
    # BouncingBall = flashBounce(screen, "Blue", 700, 500)
    Ball_1.flashBounce(screen, ball_color, 700, 500)
    if x_location >= SCREEN_WIDTH - ball_size or x_location < ball_size:
        x_speed = x_speed * -1

    if y_location >= SCREEN_HEIGHT - ball_size or y_location < ball_size:
        y_speed = y_speed * -1


    x_location += x_speed
    y_location += y_speed

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


