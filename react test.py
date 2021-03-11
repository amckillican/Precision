import pygame, pygame.gfxdraw, random

# Initialize pygame
pygame.init()
pygame.font.init()
Title_Font = pygame.font.SysFont("Arial", 60)
Subtitle_font = pygame.font.SysFont("Arial", 30)

# Variables
done = False
game_state = "start"
count = 0
start_time = 0
average_time = 0
current_time = pygame.time.get_ticks()

font = pygame.font.SysFont("Calibri", 30)

text = font.render("PRESS ANY KEY TO START TEST", True, (255, 255, 255))
w = font.render("PRESS ANY KEY", True, (0, 255, 0))
r_surf = None
ar_surf = None

# Initialing colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (39, 41, 44)

# Set the width and height of the screen [width, height]
res = (1280, 720)
screen = pygame.display.set_mode(res)


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


# Running the reaction time game
# def React():


# Setting the title of the window
pygame.display.set_caption("Reaction Time Test")

# Setting the screen refresh rate
fps = 60
clock = pygame.time.Clock()

# Main program loop
while not done:
    # Main event loop
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
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
                r_surf = font.render(f"REACTION TIME: {reaction_time:.03f}", True, (255, 255, 255))
                ar_surf = font.render(f"AVERAGE REACTION TIME IS: {average_time:.03f}", True, (255, 255, 255))

    if game_state == "wait":
        if current_time >= start_time:
            game_state = "wait_for_reaction"

            # Clearing the screen
            screen.fill((39, 41, 44))

    center = screen.get_rect().center
    if game_state == "start":
        screen.blit(text, text.get_rect(center=center))
    if game_state == "wait_for_reaction":
        screen.blit(w, w.get_rect(center=center))
    if r_surf:
        screen.blit(r_surf, r_surf.get_rect(center=(center[0], 350)))
    if ar_surf:
        screen.blit(ar_surf, ar_surf.get_rect(center=(center[0], 400)))

    # Update the screen with what we've drawn
    pygame.display.flip()

    # Limit to 60 fps
    clock.tick(fps)

# Close the window and quit
pygame.quit()
