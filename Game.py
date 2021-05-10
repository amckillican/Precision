# Importing modules
import pygame.gfxdraw
import random

# Initializing everything
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
Title_Font = pygame.font.SysFont("Arial", 60)
Subtitle_font = pygame.font.SysFont("Arial", 30)
pygame.display.set_caption("Precision - Main Menu")
clock = pygame.time.Clock()

# Initialing colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (39, 41, 44)

# Variables
pos_list_horizontal = [368, 516, 664, 812]
pos_list_vertical = [83, 247, 411, 575]
game_screen = "menu"
game_type = "menu"
game_mode = "start"
average_time = 0
count = 0
num_targets = 0
beginning = 0
reaction_time = 0
start_time = 0
current_time = 0
final_average = 0
game_time = 0
time_left = 60
game_start = 1
target_count = 4
done = False

# Initialize images
aim_button = pygame.image.load("assets/main_menu/aim_button.png").convert_alpha(screen)
aim_button_s = pygame.image.load("assets/main_menu/aim_button_s.png").convert_alpha(screen)
quit_button = pygame.image.load("assets/main_menu/quit_button.png").convert_alpha(screen)
quit_button_s = pygame.image.load("assets/main_menu/quit_button_s.png").convert_alpha(screen)
reaction_button = pygame.image.load("assets/main_menu/reaction_button.png").convert_alpha(screen)
reaction_button_s = pygame.image.load("assets/main_menu/reaction_button_s.png").convert_alpha(screen)
title = pygame.image.load("assets/main_menu/title.png").convert_alpha(screen)
flick = pygame.image.load("assets/difficulty/flick.png").convert_alpha(screen)
flick_s = pygame.image.load("assets/difficulty/flick_s.png").convert_alpha(screen)
spider_shot = pygame.image.load("assets/difficulty/spider_shot.png").convert_alpha(screen)
spider_shot_s = pygame.image.load("assets/difficulty/spider_shot_s.png").convert_alpha(screen)
grid_shot = pygame.image.load("assets/difficulty/grid_shot.png").convert_alpha(screen)
grid_shot_s = pygame.image.load("assets/difficulty/grid_shot_s.png").convert_alpha(screen)
red_target_image = pygame.transform.scale((pygame.image.load("assets/targets/RED.png").convert_alpha(screen)), [100, 100])


# Render text function
def Title_text(text="NULL", color=white, position=(640, 360)):
    rendered_text = Title_Font.render(text, True, color)
    rendered_text_rect = rendered_text.get_rect(center=position)
    screen.blit(rendered_text, rendered_text_rect)


# Render text function
def Title_textL(text="NULL", color=white, position=(640, 360)):
    rendered_text = (Title_Font.render(text, True, color))
    rendered_text_rect = rendered_text.get_rect(topleft=position)
    screen.blit(rendered_text, rendered_text_rect)


# Render text function
def Title_textR(text="NULL", color=white, position=(640, 360)):
    rendered_text = (Title_Font.render(text, True, color))
    rendered_text_rect = rendered_text.get_rect(topright=position)
    screen.blit(rendered_text, rendered_text_rect)


# Main program loop
while not done:
    # Keep track of the time
    current_time = pygame.time.get_ticks()

    # If the screen is on the start menu
    if game_type == "menu":
        pygame.display.set_caption("Precision - Main Menu")
        # Check the user events
        for event in pygame.event.get():
            # If the close button is pressed
            if event.type == pygame.QUIT:
                # Quit the application
                quit()

            # Clearing the screen
            screen.fill(background)

            # If the screen is on the main menu
            if game_screen == "menu":
                # Clear the screen
                pygame.Surface.fill(screen, background)

                # Displaying the menu images
                screen.blit(title, [160, 80])
                screen.blit(reaction_button, [538, 262])
                screen.blit(aim_button, [538, 410])
                screen.blit(quit_button, [538, 558])

                # Highlighting the reaction time button if the mouse is overtop of it
                if reaction_button.get_rect(topleft=[538, 262]).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(reaction_button_s, [538, 262])

                    # Start the reaction time game
                    if event.type == pygame.MOUSEBUTTONDOWN and reaction_button.get_rect(
                            topleft=[538, 262]).collidepoint(pygame.mouse.get_pos()):
                        pygame.Surface.fill(screen, background)
                        game_type = "react"

                # Highlighting the aim training button if the mouse is overtop of it
                elif aim_button.get_rect(topleft=[538, 410]).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(aim_button_s, [538, 410])

                    # Change to the aim training selection screen
                    if event.type == pygame.MOUSEBUTTONDOWN and aim_button.get_rect(
                            topleft=[538, 410]).collidepoint(pygame.mouse.get_pos()):
                        pygame.Surface.fill(screen, background)
                        game_screen = "aim"

                # Highlighting the quit button if the mouse is overtop of it
                elif quit_button.get_rect(topleft=[538, 558]).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(quit_button_s, [538, 558])

                    # Quitting the game
                    if event.type == pygame.MOUSEBUTTONDOWN and quit_button.get_rect(
                            topleft=[538, 558]).collidepoint(pygame.mouse.get_pos()):
                        quit()

            # If the menu is on the aim trainer game selection menu
            if game_screen == "aim":
                # Clear the screen
                pygame.Surface.fill(screen, background)

                # Displaying the menu images
                screen.blit(title, [160, 80])
                Title_text(text="Choose A Game", color=white, position=[640, 350])
                screen.blit(flick, [93, 500])
                screen.blit(spider_shot, [389, 500])
                screen.blit(grid_shot, [686, 500])
                screen.blit(quit_button, [983, 500])

                # Highlighting the flicking button if the mouse is overtop of it
                if flick.get_rect(topleft=[93, 500]).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(flick_s, [93, 500])

                    # Change to the flicking game mode
                    if event.type == pygame.MOUSEBUTTONDOWN and flick.get_rect(topleft=[93, 500]).collidepoint(
                            pygame.mouse.get_pos()):
                        game_type = "flick"
                        screen.fill(background)

                # Highlighting the tracking button if the mouse is overtop of it
                elif spider_shot.get_rect(topleft=[389, 500]).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(spider_shot_s, [389, 500])

                    # Change to the tracking game mode
                    if event.type == pygame.MOUSEBUTTONDOWN and spider_shot.get_rect(topleft=[389, 500]).collidepoint(
                            pygame.mouse.get_pos()):
                        game_type = "spider_shot"
                        screen.fill(background)

                # Highlighting the grid shot button if the mouse is overtop of it
                elif grid_shot.get_rect(topleft=[686, 500]).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(grid_shot_s, [686, 500])

                    # Change to the grid shot game mode
                    if event.type == pygame.MOUSEBUTTONDOWN and grid_shot.get_rect(topleft=[686, 500]).collidepoint(
                            pygame.mouse.get_pos()):
                        game_type = "grid_shot"
                        screen.fill(background)

                # Highlighting the flicking button if the mouse is overtop of it
                elif quit_button.get_rect(topleft=[983, 500]).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(quit_button_s, [983, 500])

                    # Quitting the game
                    if event.type == pygame.MOUSEBUTTONDOWN and quit_button.get_rect(
                            topleft=[983, 500]).collidepoint(pygame.mouse.get_pos()):
                        game_screen = "menu"

    # If the reaction game mode is chosen
    if game_type == "react":
        pygame.display.set_caption("Precision - Reaction Time Test")
        screen.fill(background)
        # Tracking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            # If key is pressed
            if event.type == pygame.KEYDOWN:
                if game_mode == "start":
                    game_mode = "wait"

                    # Run the game 3 times in a row
                    if count >= 1:
                        Title_text(f"Reaction Time: {reaction_time}", white, (640, 600))

                    start_time = current_time + random.randint(1000, 4000)

                # Measure the reaction time
                if game_mode == "wait_for_reaction":
                    game_mode = "wait"
                    reaction_time = (current_time - start_time) / 1000
                    start_time = current_time + random.randint(1000, 4000)
                    count += 1
                    average_time = ((average_time * (count - 1) + reaction_time) / count)

            # If the results are being displayed
            if game_mode == "results":
                # If the user presses the enter key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Return to the main menu
                        game_screen = "menu"
                        game_type = "menu"
                        game_mode = "start"
                        average_time = 0
                        count = 0
                        reaction_time = 0
                        start_time = 0
                        current_time = 0

        # Showing the previous reaction time
        if game_mode == "wait":
            if count >= 1:
                Title_text(f"Reaction Time: {reaction_time * 1000:.0f} MS", white, (640, 600))

            if current_time >= start_time:
                game_mode = "wait_for_reaction"

                # Clearing the screen
                screen.fill(background)

        # After 3 tries display the results
        if count == 3:
            game_mode = "results"

        # Prompt the user to start
        if count < 3:
            if game_mode == "start":
                Title_text("Press Any Key To Start")
            if game_mode == "wait_for_reaction":
                Title_text("Press Any Key")

                if count >= 1:
                    Title_text(f"Reaction Time: {reaction_time * 1000:.0f} MS", white, (640, 600))

        # Saving the users name and reaction time
        if game_mode == "results":
            screen.fill(background)
            final_average = average_time * 1000
            Title_text("Average Reaction", white, (640, 250))
            Title_text(f"Time: {final_average:.0f} MS", white, (640, 320))
            Title_text("Press Enter To Exit To Menu", white, (640, 450))

    # Update the screen with what we've drawn
    pygame.display.flip()

    # Limit to 60 fps
    clock.tick(60)

# Close the window and quit
pygame.quit()
