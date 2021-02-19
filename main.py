# importing modules
import pygame
import random
import sys
from pygame.locals import *

# initialing colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (39, 41, 44)

# initialize pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size, RESIZABLE)

# setting the title of the window
pygame.display.set_caption("Precision")

# used to check if the user wants to quit
done = False

# setting the screen refresh rate
fps = 60
clock = pygame.time.Clock()

# main program loop
while not done:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic should go here

    # Screen-clearing code goes here

    # clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(background)

    # drawing code should go here

    # update the screen with what we've drawn
    pygame.display.flip()

    # limit to 60 fps
    clock.tick(fps)

# close the window and quit
pygame.quit()
