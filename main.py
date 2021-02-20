# importing modules
import pygame
import pygame.gfxdraw

# tracking variables
is_menu = 1
react = 0
aim = 0
done = False

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

# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)

# initialize images
aim_button = pygame.image.load("aim_button.png").convert_alpha(screen)
aim_button_s = pygame.image.load("aim_button_s.png").convert_alpha(screen)
quit_button = pygame.image.load("quit_button.png").convert_alpha(screen)
quit_button_s = pygame.image.load("quit_button_s.png").convert_alpha(screen)
reaction_button = pygame.image.load("reaction_button.png").convert_alpha(screen)
reaction_button_s = pygame.image.load("reaction_button_s.png").convert_alpha(screen)
title = pygame.image.load("title.png").convert_alpha(screen)


# view the menu
# noinspection PyUnusedLocal
def view_menu():
    global is_menu

    # clear the screen
    pygame.Surface.fill(screen, background)

    # displaying the menu buttons
    screen.blit(title, [142, 80])
    screen.blit(reaction_button, [538, 262])
    screen.blit(aim_button, [538, 410])
    screen.blit(quit_button, [538, 558])

    # highlighting the buttons if the mouse is overtop of it
    if reaction_button.get_rect(topleft=[538, 262]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(reaction_button_s, [538, 262])

        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & reaction_button.get_rect(topleft=[538, 262]).collidepoint(
                pygame.mouse.get_pos()):  # clicks on reaction time
            pygame.Surface.fill(screen, background)
            #is_menu = 0

    elif aim_button.get_rect(topleft=[538, 410]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(aim_button_s, [538, 410])

        # noinspection PyArgumentList
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & aim_button.get_rect(topleft=[538, 410]).collidepoint(
                pygame.mouse.get_pos()):   # clicks on aim trainer
            pygame.Surface.fill(screen, background)
            #is_menu = 0

    elif quit_button.get_rect(topleft=[538, 558]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(quit_button_s, [538, 558])

        # noinspection PyArgumentList
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & quit_button.get_rect(topleft=[538, 558]).collidepoint(
                pygame.mouse.get_pos()):  # clicks on quit
            quit()


# setting the title of the window
pygame.display.set_caption("Precision")

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
    if is_menu == 1:
        view_menu()

    # update the screen with what we've drawn
    pygame.display.flip()

    # limit to 60 fps
    clock.tick(fps)

# close the window and quit
pygame.quit()
