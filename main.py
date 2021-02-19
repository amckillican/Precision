# importing modules
import pygame
import pygame.gfxdraw
from pygame.locals import *
import random
import sys


# function to draw a rounded rectangle
def draw_rounded_rect(surface, rect, color, corner_radius):
    if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
        raise ValueError(corner_radius)

    # draw circles
    pygame.gfxdraw.aacircle(surface, rect.left + corner_radius, rect.top + corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right - corner_radius - 1, rect.top + corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.left + corner_radius, rect.bottom - corner_radius - 1, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right - corner_radius - 1, rect.bottom - corner_radius - 1, corner_radius, color)

    # fill them in
    pygame.gfxdraw.filled_circle(surface, rect.left + corner_radius, rect.top + corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right - corner_radius - 1, rect.top + corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.left + corner_radius, rect.bottom - corner_radius - 1, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right - corner_radius - 1, rect.bottom - corner_radius - 1, corner_radius, color)

    # draw rectangles using the position and measurements
    rect_tmp = pygame.Rect(rect)

    rect_tmp.width -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)

    rect_tmp.width = rect.width
    rect_tmp.height -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)


# initialing colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (39, 41, 44)
button = (65, 68, 73)

# initialize pygame
pygame.init()

# initialize images
aim_button = pygame.image.load("aim_button.png")
aim_button_s = pygame.image.load("aim_button_s.png")
quit_button = pygame.image.load("quit_button.png")
quit_button_s = pygame.image.load("quit_button_s.png")
reaction_button = pygame.image.load("reaction_button.png")
reaction_button_s = pygame.image.load("reaction_button_s.png")
title = pygame.image.load("title.png")


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

    '''pygame.draw.rect(screen, button, [538, 262, 204, 116], border_radius=20)
    pygame.draw.rect(screen, button, [538, 410, 204, 116], border_radius=20)
    pygame.draw.rect(screen, button, [538, 558, 204, 116], border_radius=20)'''

    # This line says "Draw surf onto the screen at the center"
    screen.blit(screen, reaction_button, (1280 / 2, 720 / 2))
    #screen.blit(reaction_button, screen, [538, 262])
    #screen.blit(reaction_button, screen, [538, 262, 204, 116], )
    #pygame.draw.rect(screen, red, [538, 410], border_radius=20)

    # update the screen with what we've drawn
    pygame.display.flip()

    # limit to 60 fps
    clock.tick(fps)

# close the window and quit
pygame.quit()
