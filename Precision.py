# Importing modules
import pygame, pygame.gfxdraw, time, random

# Variables
is_menu = 1
react = 0
aim = 0
done = False
text = ""
delay = 0
center = (640, 360)

# Initialing colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (39, 41, 44)
button = (65, 68, 73)

# Initialize pygame
pygame.init()
pygame.font.init()

# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)

# Initialize images
aim_button = pygame.image.load("main_menu/aim_button.png").convert_alpha(screen)
aim_button_s = pygame.image.load("main_menu/aim_button_s.png").convert_alpha(screen)
quit_button = pygame.image.load("main_menu/quit_button.png").convert_alpha(screen)
quit_button_s = pygame.image.load("main_menu/quit_button_s.png").convert_alpha(screen)
reaction_button = pygame.image.load("main_menu/reaction_button.png").convert_alpha(screen)
reaction_button_s = pygame.image.load("main_menu/reaction_button_s.png").convert_alpha(screen)
title = pygame.image.load("main_menu/title.png").convert_alpha(screen)


# Render some text
def Text(size=40, text="NULL", color=white, center=(0, 0)):
    myfont = pygame.font.SysFont("Calibri", size)
    rendered_text = (myfont.render(text, True, color))
    rendered_text_rext = rendered_text.get_rect(center=center)
    screen.blit(rendered_text, rendered_text_rext)


# View the menu
def View_menu():
    global is_menu, aim, react

    # Clear the screen
    pygame.Surface.fill(screen, background)

    # Displaying the menu images
    screen.blit(title, [142, 80])
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
            is_menu = 0
            react = 1

    # Highlighting the buttons if the mouse is overtop of it
    elif aim_button.get_rect(topleft=[538, 410]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(aim_button_s, [538, 410])

        # Change to the aim training game scene
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & aim_button.get_rect(topleft=[538, 410]).collidepoint(
                pygame.mouse.get_pos()):  # clicks on aim trainer
            pygame.Surface.fill(screen, background)
            is_menu = 0
            aim = 1

    # Highlighting the buttons if the mouse is overtop of it
    elif quit_button.get_rect(topleft=[538, 558]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(quit_button_s, [538, 558])

        # Quitting the game
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & quit_button.get_rect(topleft=[538, 558]).collidepoint(
                pygame.mouse.get_pos()):  # clicks on quit
            quit()


# Running the reaction time game
def React():
    font = pygame.font.SysFont("Calibri", 30)

    text = font.render("PRESS ANY KEY TO START TEST", 0, (255, 255, 255))
    w = font.render("PRESS ANY KEY", 0, (0, 255, 0))
    r_surf = None
    ar_surf = None

    game_state = "start"
    start_time = 0
    average_time = 0

    count = 0

    if event.type == pygame.KEYDOWN:
        if game_state == "start":
            game_state = "wait"
            start_time = current_time + random.randint(1000, 4000)
        if game_state == "wait_for_reaction":
            game_state = "wait"
            reaction_time = (current_time - start_time) / 1000
            start_time = current_time + random.randint(1000, 4000)
            count += 1
            average_time = (average_time * (count - 1) + reaction_time) / count
            r_surf = font.render(f"REACTION TIME: {reaction_time:.03f}", 0, (255, 255, 255))
            ar_surf = font.render(f"AVERAGE REACTION TIME IS: {average_time:.03f}", 0, (255, 255, 255))

    if game_state == "wait":
        if current_time >= start_time:
            game_state = "wait_for_reaction"

    screen.fill(pygame.Color("black"))

    center = screen.get_rect().center
    if game_state == "start":
        screen.blit(text, text.get_rect(center=center))
    if game_state == "wait_for_reaction":
        screen.blit(w, w.get_rect(center=center))
    if r_surf:
        screen.blit(r_surf, r_surf.get_rect(center=(center[0], 350)))
    if ar_surf:
        screen.blit(ar_surf, ar_surf.get_rect(center=(center[0], 400)))




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

    # clear the screen to background color. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(background)

    # drawing code should go here
    if is_menu == 1:
        View_menu()
    if react == 1:
        React()
    if aim == 1:
        break
    # update the screen with what we've drawn
    pygame.display.flip()

    # limit to 60 fps
    clock.tick(fps)

# close the window and quit
pygame.quit()
