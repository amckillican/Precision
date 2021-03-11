# Importing modules
import pygame, pygame.gfxdraw, random

# Variables
game_screen = "menu"
done = False
text = ""
delay = 0
center = (640, 360)
start_time = 0
average_time = 0
difficulty = ""

# Initialing colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (39, 41, 44)

# Initialize pygame
pygame.init()
pygame.font.init()
Title_Font = pygame.font.SysFont("Arial", 60)
Subtitle_font = pygame.font.SysFont("Arial", 30)

# Set the width and height of the screen [width, height]
res = (1280, 720)
screen = pygame.display.set_mode(res)

# Initialize images
aim_button = pygame.image.load("main_menu/aim_button.png").convert_alpha(screen)
aim_button_s = pygame.image.load("main_menu/aim_button_s.png").convert_alpha(screen)
quit_button = pygame.image.load("main_menu/quit_button.png").convert_alpha(screen)
quit_button_s = pygame.image.load("main_menu/quit_button_s.png").convert_alpha(screen)
reaction_button = pygame.image.load("main_menu/reaction_button.png").convert_alpha(screen)
reaction_button_s = pygame.image.load("main_menu/reaction_button_s.png").convert_alpha(screen)
title = pygame.image.load("main_menu/title.png").convert_alpha(screen)
easy = pygame.image.load("difficulty/easy.png").convert_alpha(screen)
easy_s = pygame.image.load("difficulty/easy_s.png").convert_alpha(screen)
medium = pygame.image.load("difficulty/medium.png").convert_alpha(screen)
medium_s = pygame.image.load("difficulty/medium_s.png").convert_alpha(screen)
hard = pygame.image.load("difficulty/hard.png").convert_alpha(screen)
hard_s = pygame.image.load("difficulty/hard_s.png").convert_alpha(screen)


# Render some text
def Title_text(text="NULL", color=white, center=(640, 360)):
    rendered_text = (Title_Font.render(text, True, color))
    rendered_text_rect = rendered_text.get_rect(center=center)
    screen.blit(rendered_text, rendered_text_rect)


# Render some text
def Subtitle_text(text="NULL", color=white, center=(640, 360)):
    rendered_text = (Subtitle_font.render(text, True, color))
    rendered_text_rect = rendered_text.get_rect(center=center)
    screen.blit(rendered_text, rendered_text_rect)


# View the menu
def View_menu():
    global game_screen

    # Clear the screen
    pygame.Surface.fill(screen, background)

    # Displaying the menu images
    screen.blit(title, [160, 80])
    screen.blit(reaction_button, [538, 262])
    screen.blit(aim_button, [538, 410])
    screen.blit(quit_button, [538, 558])

    # Highlighting the buttons if the mouse is overtop of it
    if reaction_button.get_rect(topleft=[538, 262]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(reaction_button_s, [538, 262])

        # Change to the reaction time game scene
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & reaction_button.get_rect(topleft=[538, 262]).collidepoint(
                pygame.mouse.get_pos()):  # clicks on reaction time
            pygame.Surface.fill(screen, background)
            game_screen = "react"

    # Highlighting the buttons if the mouse is overtop of it
    elif aim_button.get_rect(topleft=[538, 410]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(aim_button_s, [538, 410])

        # Change to the aim training game scene
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & aim_button.get_rect(topleft=[538, 410]).collidepoint(
                pygame.mouse.get_pos()):  # clicks on aim trainer
            pygame.Surface.fill(screen, background)
            game_screen = "aim"

    # Highlighting the buttons if the mouse is overtop of it
    elif quit_button.get_rect(topleft=[538, 558]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(quit_button_s, [538, 558])

        # Quitting the game
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & quit_button.get_rect(topleft=[538, 558]).collidepoint(
                pygame.mouse.get_pos()):  # clicks on quit
            quit()


# Running the reaction time game
def React():
    game_state = "start"
    count = 0
    current_time = pygame.time.get_ticks()

    if game_state == "start":
        Title_text(text="Press Any Key To Start", color=white, center=(640, 360))

    for event in pygame.event.get():
        if event == pygame.KEYDOWN:
            pygame.Surface.fill(screen, background)
            game_state = ""


def Difficulty():
    pygame.Surface.fill(screen, background)

    # Rendering images
    screen.blit(title, [160, 80])
    Title_text(text="Choose A Difficulty", color=white, center=[640, 300])
    screen.blit(easy, [93, 400])
    screen.blit(medium, [389, 400])
    screen.blit(hard, [686, 400])
    screen.blit(quit_button, [983, 400])

    #
    if easy.get_rect(topleft=[93, 400]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(easy_s, [93, 400])

        difficulty = "easy"

    elif medium.get_rect(topleft=[389, 400]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(medium_s, [389, 400])

        difficulty = "medium"

    elif hard.get_rect(topleft=[686, 400]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(hard_s, [686, 400])

        difficulty = "hard"

    elif quit_button.get_rect(topleft=[983, 400]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(quit_button_s, [983, 400])

        # Quitting the game
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & quit_button.get_rect(topleft=[983, 400]).collidepoint(
                pygame.mouse.get_pos()):
            game_screen = "menu"


# Setting the title of the window
pygame.display.set_caption("Precision")

# Setting the screen refresh rate
fps = 60
clock = pygame.time.Clock()

# Main program loop
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Clearing the screen
        screen.fill(background)

        # Drawing code should go here
        if game_screen == "menu":
            View_menu()
        if game_screen == "react":
            React()
        if game_screen == "aim":
            Difficulty()

    # Update the screen with what we've drawn
    pygame.display.flip()

    # Limit to 60 fps
    clock.tick(fps)

# Close the window and quit
pygame.quit()
