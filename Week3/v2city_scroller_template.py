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
from random import randint
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
Lightgray= (127, 122, 92)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point= x_point
        self.y_point=y_point
        self.width=width
        self.height=height
        self.color=color

    def draw(self, x_point):
        pygame.draw.rect(screen, self.color, (self.x_point,self.y_point,self.width,self.height))
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        screen, GREY,

    def move(self, speed):

        self.x_point+=speed
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right ->
            A negative integer moves the building to the left  <-
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """



class Scroller(object):

    
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, base, color, speed):
        self.width=width
        self.height=height
        self.base=base
        self.color=color
        self.speed=speed
        self.buildinglist=[]
        self.combined_width=0
        self.add_buildings()



    def add_buildings(self):
        print("one")
        # for building in self.buildinglist:
        #     self.combined_width+= buildinglist[-1].width
            
        while self.combined_width < self.width:
            self.add_building(self.combined_width)
            # self.combined_width+= self.buildinglist[-1].width
            print("no")
    
            

        """
        Will call add_building until there the buildings fill up the width of the
        scroller.
        """

    def add_building(self, x_location):
        width=random.randint(60, 100)
        self.combined_width+= width
        Building1= Building(x_location, self.height, width  ,random.randint(-250,-100),self.color)
        self.buildinglist.append(Building1)
        print("hi")

       
    """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
    """

    def draw_buildings(self):
        #for each building in buildinglist, draw it on the screen
        for current_building in self.buildinglist:
            current_building.draw(self.combined_width)            

    

       

    
        # """
        # This calls the draw method on each building.
        # """

    def move_buildings(self):
        for current_building in self.buildinglist:
            current_building.move(-2)



        if self.buildinglist[-1].x_point> SCREEN_WIDTH:
            self.buildinglist.remove(self.buildinglist[-1])
        if self.buildinglist[0].x_point <0:
            width=random.randint(60,100)
            x_location= self.buildinglist[-1].x_point + width-20
            building=Building(x_location, self.height, width, random.randint(-250, -100), self.color)
            self.buildinglist.insert(800, building)

        


        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
    # """
FRONT_SCROLLER_COLOR = (0, 0, 30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (13, 157, 255)


Road=Building(0, 450, 800, 150, Lightgray)

class cloud():
    def __init__(self, screen, speed, x_position, y_position):
        self.screen= screen
        self.speed=speed
        self.x_position=x_position
        self.y_position= y_position
    def create_cloud(self):

        cloud = pygame.image.load("clouds.png.png")
        cloud = pygame. transform.scale(cloud, (80, 35))
        screen.blit(cloud, (self.x_position, self.y_position))

    def move(self, speed):
        self.x_position += self.speed

        # if cloud.x_point <0:
        #     width=random.randint(60,100)
        #     cloud=cloud(0, self.height, width, 100, WHITE)
        #     self.cloud(screen, 1, 0, 100)


# def drawCloud(): 
#     for i in range(1,16):  
#         size=random.randint(20,70)
#         xOffset=random.randint(-40,40)
#         yOffset=random.randint(-30,30)
#         pygame.draw.ellipse(screen, WHITE, (300, 100, 40, 80), 10)



build1 = Scroller(SCREEN_WIDTH, 450, SCREEN_HEIGHT, MIDDLE_SCROLLER_COLOR,1)
build2 = Scroller(SCREEN_WIDTH, 425, (SCREEN_HEIGHT - 50), BACK_SCROLLER_COLOR, 1)
build3 = Scroller(SCREEN_WIDTH, 400, (SCREEN_HEIGHT - 100), FRONT_SCROLLER_COLOR, 1)
cloud= cloud(screen, 1, 0, 100)
# build1.add_buildings()
# build2.add_buildings()
# build3.add_buildings()

class RunnerSprite(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.width=width
        self.height=height
        self.color = color
        self.image=pygame.Surface((width, height))
        self.image.fill(color)
        mouseposition= pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center=mouseposition)





# # -------- Main Program Loop -----------
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
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    # drawCloud()
    all_sprites_list = pygame.sprite.Group()
    player1=RunnerSprite(25, 55, GREEN)
    all_sprites_list.add(player1)
   

    Road.draw(1)
    cloud.move(1)
    cloud.create_cloud()
    build3.draw_buildings()
    build3.move_buildings()
    build2.draw_buildings()
    build2.move_buildings()
    build1.draw_buildings()
    build1.move_buildings()

    all_sprites_list.draw(screen)

  


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
