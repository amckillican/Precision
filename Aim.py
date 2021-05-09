# Importing modules
import pygame.gfxdraw
import random

# Initializing everything
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
Title_Font = pygame.font.SysFont("Arial", 60)
Subtitle_font = pygame.font.SysFont("Arial", 30)
pygame.display.set_caption("Aim Trainer")
clock = pygame.time.Clock()
reaction_names = open("reaction_names.txt", "a")
reaction_times = open("reaction_times.txt", "a")

# Variables
current_time = pygame.time.get_ticks()
game_state = "start"
name = ""
beginning = 0
new_target = 1
num_targets = 0
count = 0
start_time = 0
average_time = 0
final_average = 0
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

# Initializing images
red_target_image = pygame.transform.scale((pygame.image.load("targets/RED.png").convert_alpha(screen)), [100, 100])
blue_target_image = pygame.transform.scale((pygame.image.load("targets/BLUE.png").convert_alpha(screen)), [100, 100])
orange_target_image = pygame.transform.scale((pygame.image.load("targets/ORANGE.png").convert_alpha(screen)),
                                             [100, 100])


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


# Render some text
def Title_textR(text="NULL", color=white, position=(640, 360)):
    rendered_text = (Title_Font.render(text, True, color))
    rendered_text_rect = rendered_text.get_rect(topright=position)
    screen.blit(rendered_text, rendered_text_rect)


# Updating the excel sheet
def Write_data():
    global name, final_average, game_state, count, average_time, reaction_time, beginning, new_target, num_targets, start_time
    reaction_names.write(f"{name}\n")
    reaction_times.write(f"{final_average:.0f}\n")

    game_state = "start"
    name = ""
    beginning = 0
    new_target = 1
    num_targets = 0
    count = 0
    start_time = 0
    average_time = 0
    reaction_time = 0


# Main program loop
while not done:
    # Main event loop
    if beginning == 0:
        screen.fill(background)
        beginning = 1
    current_time = pygame.time.get_ticks()
    game_time = (current_time - start_time) / 1000
    time_left = (60 - game_time) // 1

    # Tracking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            reaction_names.close()
            reaction_times.close()
            quit()

        if game_state == "start":
            Title_text("Click To Start")

        if game_state == "start":
            if pygame.mouse.get_pressed(num_buttons=3)[0] == 1:
                screen.fill(background)
                start_time = current_time
                game_state = "generate"

        if game_time < 60:
            if game_state == "generate":
                horizontal_red = random.randint(0, 1020)
                vertical_red = random.randint(0, 520)
                screen.blit(red_target_image, [horizontal_red, vertical_red])
                game_state = "react"

            if game_state == "react":
                if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 and red_target_image.get_rect(
                        topleft=[horizontal_red, vertical_red]).collidepoint(pygame.mouse.get_pos()):
                    screen.fill(background)
                    num_targets += 1
                    game_state = "generate"

        if game_time > 60:
            game_state = "results"
            screen.fill(background)

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

    # Display the time left
    if game_state != "results" or game_state != "start":
        Title_textL("Targets: " + str(num_targets), white, (10, 0))
        Title_textR(str(time_left)[:2], white, (1270, 0))

    # Saving the users name and reaction time
    if game_state == "results":
        screen.fill(background)
        final_average = 60000 / num_targets
        Title_text(f"Targets Hit: {num_targets}", white, (640, 100))
        Title_text(f"Average Response", white, (640, 250))
        Title_text(f"Time: {final_average:.0f} MS", white, (640, 350))
        Title_text("Please Type Your", white, (640, 550))
        Title_text(f"Name: {name}", white, (640, 650))

    pygame.display.flip()

    clock.tick(60)

# Close the window and quit.
pygame.quit()
