# Importing modules
import pygame, pygame.gfxdraw, time, random

# Variables
is_menu = 1
react = 0
aim = 0
done = False
text = ""
center = (0, 0)
delay = 0

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
reaction_time_lightning = pygame.image.load("reaction_time/reaction_time_lightning.png").convert_alpha(screen)
too_soon = pygame.image.load("reaction_time/too_soon.png").convert_alpha(screen)
delay_image = pygame.image.load("reaction_time/delay.png").convert_alpha(screen)


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
            # time.sleep(0.4)

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
    # Display the start text
    screen.blit(reaction_time_lightning, [570, 120])
    Text(size=80, text="Reaction Time Test", color=white, center=(640, 450))
    Text(size=40, text="When the screen turns green, click as quickly as you can.", color=white, center=(640, 530))
    Text(size=40, text="Click anywhere to start.", color=white, center=(640, 580))

    # Starting the actual game
    if pygame.mouse.get_pressed(num_buttons=3)[0] == 1:
        # Display the get ready screen
        screen.fill(red)
        Text(size=100, text="Wait For Green", color=white, center=(640, 360))

        # Wait a random amount of time
        # event = threading.Event()
        # threading.Event.wait(self=event, timeout=(random.randint(4, 11)))
        time.sleep(random.randint(4, 11))

        # # If clicked before react screen
        # if pygame.mouse.get_pressed(num_buttons=3)[0]:  # & wait time is not over **********************
        #     # Display the try again screen
        #     screen.fill(background)
        #     screen.blit(too_soon, [543, 120])
        #     Text(size=100, text="Too Soon!", color=white, center=(640, 450))
        #     Text(size=40, text="Click to restart", color=white, center=(640, 530))

        # Display the react screen
        screen.fill(green)
        Text(size=100, text="Click!", color=white, center=(640, 450))

        # Start a timer
        current_time = time.time_ns() // 1_000_000

        # Wait for user to click
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1:
            # Stop the timer
            click_time = time.time_ns() // 1_000_000
            print(current_time, click_time, click_time-current_time)

            # Display the time screen
            screen.fill(background)
            screen.blit(delay_image, [543, 120])
            Text(size=100, text=(str(delay) + " ms"), color=white, center=(640, 450))

            # Display a varying message based on the reaction time
            if delay <= 140:
                Text(size=40, text="WOW! You have inhuman reactions!", color=white, center=(640, 530))
            elif 141 <= delay & delay <= 190:
                Text(size=40, text="Nice! You are above average!", color=white, center=(640, 530))
            elif 191 <= delay <= 230:
                Text(size=40, text="Good Job! You are in the average.", color=white, center=(640, 530))
            elif 231 <= delay <= 300:
                Text(size=40, text="You are below the average.", color=white, center=(640, 530))
            elif 301 >= delay:
                Text(size=40, text="Are you paying attention?", color=white, center=(640, 530))


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
