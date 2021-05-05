# Importing modules
import pygame.gfxdraw

# Initializing everything
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
Title_Font = pygame.font.SysFont("Arial", 60)
Subtitle_font = pygame.font.SysFont("Arial", 30)
pygame.display.set_caption("Aim Trainer")
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
def Subtitle_text(text="NULL", color=white, position=(640, 360)):
    rendered_text = (Subtitle_font.render(text, True, color))
    rendered_text_rect = rendered_text.get_rect(center=position)
    screen.blit(rendered_text, rendered_text_rect)


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

        if game_state == "start":
            if pygame.mouse.get_pressed(3)[0] == 1:
                game_state = "react"

        if game_state == "react":
            if pygame.mouse.get_pressed(3)[0] == 1:
                print("clicked target placeholder")

    if game_state == "start":
        Title_text("Click To Start")

    pygame.display.flip()

    clock.tick(60)

# Close the window and quit.
pygame.quit()
