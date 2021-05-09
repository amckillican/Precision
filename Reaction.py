# Importing modules
import pygame.gfxdraw
import random

# Initializing everything
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
Title_Font = pygame.font.SysFont("Arial", 60)
Subtitle_font = pygame.font.SysFont("Arial", 30)
pygame.display.set_caption("Reaction Time Test")
clock = pygame.time.Clock()
names_file = open("names_file.txt", "a")
times_file = open("times_file.txt", "a")

# Variables
current_time = pygame.time.get_ticks()
game_state = "start"
name = ""
count = 0
start_time = 0
average_time = 0
reaction_time = 0
split_name = []
done = False

# Initialing colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (39, 41, 44)


# Render some text
def Title_text(text="NULL", color=white, position=(640, 360)):
    rendered_text = Title_Font.render(text, True, color)
    rendered_text_rect = rendered_text.get_rect(center=position)
    screen.blit(rendered_text, rendered_text_rect)


# Render some text
def Title_textL(text="NULL", color=white, position=(640, 360)):
    rendered_text = (Title_Font.render(text, True, color))
    rendered_text_rect = rendered_text.get_rect(topleft=position)
    screen.blit(rendered_text, rendered_text_rect)


# Render some text
def Subtitle_text(text="NULL", color=white, position=(640, 360)):
    rendered_text = (Subtitle_font.render(text, True, color))
    rendered_text_rect = rendered_text.get_rect(center=position)
    screen.blit(rendered_text, rendered_text_rect)


# Render some text
def Subtitle_textL(text="NULL", color=white, position=(640, 360)):
    rendered_text = (Subtitle_font.render(text, True, color))
    rendered_text_rect = rendered_text.get_rect(topleft=position)
    screen.blit(rendered_text, rendered_text_rect)


# Updating the excel sheet
def Write_data():
    global name, final_average, game_state, count, average_time, reaction_time
    names_file.write(f"{name}\n")
    times_file.write(f"{final_average:.0f}\n")

    game_state = "start"
    count = 0
    average_time = 0
    reaction_time = 0
    name = ""


# Main program loop
while not done:
    # Main event loop
    screen.fill(background)
    current_time = pygame.time.get_ticks()

    # Tracking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            names_file.close()
            times_file.close()
            quit()

        # If key is pressed
        if event.type == pygame.KEYDOWN:
            if game_state == "start":
                game_state = "wait"

                # Run the game 3 times in a row
                if count >= 1:
                    Title_text(f"Reaction Time: {reaction_time}", white, (640, 600))

                start_time = current_time + random.randint(1000, 4000)

            # Measure the reaction time
            if game_state == "wait_for_reaction":
                game_state = "wait"
                reaction_time = (current_time - start_time) / 1000
                start_time = current_time + random.randint(1000, 4000)
                count += 1
                average_time = ((average_time * (count - 1) + reaction_time) / count)

        # Saving the users name and time
        if game_state == "results":
            if event.type == pygame.KEYDOWN:
                if len(name) <= 9:
                    if event.key == pygame.K_a: name += str(chr(event.key))
                    if event.key == pygame.K_b: name += str(chr(event.key))
                    if event.key == pygame.K_c: name += str(chr(event.key))
                    if event.key == pygame.K_d: name += str(chr(event.key))
                    if event.key == pygame.K_e: name += str(chr(event.key))
                    if event.key == pygame.K_f: name += str(chr(event.key))
                    if event.key == pygame.K_g: name += str(chr(event.key))
                    if event.key == pygame.K_h: name += str(chr(event.key))
                    if event.key == pygame.K_i: name += str(chr(event.key))
                    if event.key == pygame.K_j: name += str(chr(event.key))
                    if event.key == pygame.K_k: name += str(chr(event.key))
                    if event.key == pygame.K_l: name += str(chr(event.key))
                    if event.key == pygame.K_m: name += str(chr(event.key))
                    if event.key == pygame.K_n: name += str(chr(event.key))
                    if event.key == pygame.K_o: name += str(chr(event.key))
                    if event.key == pygame.K_p: name += str(chr(event.key))
                    if event.key == pygame.K_q: name += str(chr(event.key))
                    if event.key == pygame.K_r: name += str(chr(event.key))
                    if event.key == pygame.K_s: name += str(chr(event.key))
                    if event.key == pygame.K_t: name += str(chr(event.key))
                    if event.key == pygame.K_u: name += str(chr(event.key))
                    if event.key == pygame.K_v: name += str(chr(event.key))
                    if event.key == pygame.K_w: name += str(chr(event.key))
                    if event.key == pygame.K_x: name += str(chr(event.key))
                    if event.key == pygame.K_y: name += str(chr(event.key))
                    if event.key == pygame.K_z: name += str(chr(event.key))
                    if event.key == pygame.K_SPACE: name += str(chr(event.key))
                if event.key == pygame.K_BACKSPACE: name = name[:-1]
                if event.key == pygame.K_RETURN: Write_data()

    # Showing the previous reaction time
    if game_state == "wait":
        if count >= 1:
            Title_text(f"Reaction Time: {reaction_time * 1000:.0f} MS", white, (640, 600))

        if current_time >= start_time:
            game_state = "wait_for_reaction"

            # Clearing the screen
            screen.fill(background)

    # After 3 tries display the results
    if count == 3:
        game_state = "results"

    # Prompt the user to start
    if count < 3:
        if game_state == "start":
            Title_text("Press Any Key To Start")
        if game_state == "wait_for_reaction":
            Title_text("Press Any Key")

            if count >= 1:
                Title_text(f"Reaction Time: {reaction_time * 1000:.0f} MS", white, (640, 600))

    # Saving the users name and reaction time
    if game_state == "results":
        screen.fill(background)
        final_average = average_time * 1000
        Title_text("Average Reaction", white, (640, 100))
        Title_text(f"Time: {final_average:.0f} MS", white, (640, 200))
        Title_text("Please Type Your", white, (640, 450))
        Title_text(f"Name: {name}", white, (640, 550))

    # Update the screen with what we've drawn
    pygame.display.flip()

    # Limit to 60 fps
    clock.tick(60)

# Close the window and quit
pygame.quit()
