# importing modules
import pygame
import pygame.gfxdraw

# tracking variables
isMenu = 1
react = 0
aim = 0
done = False


# function to draw a rounded rectangle
def draw_rounded_rect(surface, rect, color, corner_radius):
    if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
        raise ValueError(corner_radius)

    # draw circles
    pygame.gfxdraw.aacircle(surface, rect.left + corner_radius, rect.top + corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right - corner_radius - 1, rect.top + corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.left + corner_radius, rect.bottom - corner_radius - 1, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right - corner_radius - 1, rect.bottom - corner_radius - 1, corner_radius,
                            color)

    # fill them in
    pygame.gfxdraw.filled_circle(surface, rect.left + corner_radius, rect.top + corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right - corner_radius - 1, rect.top + corner_radius, corner_radius,
                                 color)
    pygame.gfxdraw.filled_circle(surface, rect.left + corner_radius, rect.bottom - corner_radius - 1, corner_radius,
                                 color)
    pygame.gfxdraw.filled_circle(surface, rect.right - corner_radius - 1, rect.bottom - corner_radius - 1,
                                 corner_radius, color)

    # draw rectangles using the position and measurements
    rect_tmp = pygame.Rect(rect)

    rect_tmp.width -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)

    rect_tmp.width = rect.width
    rect_tmp.height -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)


# view the menu
def view_menu():
    # displaying the menu buttons
    screen.blit(title, [142, 80])
    screen.blit(reaction_button, [538, 262])
    screen.blit(aim_button, [538, 410])
    screen.blit(quit_button, [538, 558])

    # highlighting the buttons if the mouse is overtop of it
    if reaction_button.get_rect(topleft=[538, 262]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(reaction_button_s, [538, 262])

        if pygame.mouse.get_pressed()[0] == (1) & reaction_button.get_rect(topleft=[538, 262]).collidepoint(
                pygame.mouse.get_pos()):  # clicks on reaction time
            print("react")

    elif aim_button.get_rect(topleft=[538, 410]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(aim_button_s, [538, 410])

        if pygame.mouse.get_pressed()[0] == (1) & aim_button.get_rect(topleft=[538, 410]).collidepoint(
                pygame.mouse.get_pos()):  # clicks on aim trainer
            print("aim")

    elif quit_button.get_rect(topleft=[538, 558]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(quit_button_s, [538, 558])

        if pygame.mouse.get_pressed()[0] == (1) & quit_button.get_rect(topleft=[538, 558]).collidepoint(
                pygame.mouse.get_pos()):  # clicks on quit
            quit()


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

    view_menu()

    # update the screen with what we've drawn
    pygame.display.flip()

    # limit to 60 fps
    clock.tick(fps)

# close the window and quit
pygame.quit()
