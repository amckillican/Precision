# Importing modules
import pygame
import pygame.gfxdraw
from openpyxl import Workbook
from openpyxl import load_workbook

# Initializing everything
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
Title_Font = pygame.font.SysFont("Arial", 60)
Subtitle_font = pygame.font.SysFont("Arial", 30)
pygame.display.set_caption("Precision")
clock = pygame.time.Clock()
wb = Workbook()
wb = load_workbook("Precision.xlsx", data_only=True)
ws = wb.active

# Initialing colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background = (39, 41, 44)

# Variables
game_screen = "menu"
difficulty = ""
name = ""
center = (640, 360)
delay = 0
start_time = 0
average_time = 0
count = 0
current_time = 0
reaction_time = 0
done = False

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
def Title_text(text="NULL", color=white, position=(640, 360)):
    rendered_text = (Title_Font.render(text, True, color))
    rendered_text_rect = rendered_text.get_rect(center=position)
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


def React_score_disp():
    name1 = f"1. {ws['A1'].value}"
    name2 = f"2. {ws['A2'].value}"
    name3 = f"3. {ws['A3'].value}"
    name4 = f"4. {ws['A4'].value}"
    name5 = f"5. {ws['A5'].value}"

    score1 = ws['B1'].value
    score2 = ws['B2'].value
    score3 = ws['B3'].value
    score4 = ws['B4'].value
    score5 = ws['B5'].value

    if name1 != "1. None":
        Subtitle_text(text="Top Reaction Time", color=white, position=[270, 325])
        Subtitle_textL(text=name1, color=white, position=[95, 375])
        Subtitle_textL(text=score1, color=white, position=[350, 375])
    if name2 != "2. None":
        Subtitle_textL(text=name2, color=white, position=[95, 425])
        Subtitle_textL(text=score2, color=white, position=[350, 425])
    if name3 != "3. None":
        Subtitle_textL(text=name3, color=white, position=[95, 475])
        Subtitle_textL(text=score3, color=white, position=[350, 475])
    if name4 != "4. None":
        Subtitle_textL(text=name4, color=white, position=[95, 525])
        Subtitle_textL(text=score4, color=white, position=[350, 525])
    if name5 != "5. None":
        Subtitle_textL(text=name5, color=white, position=[95, 575])
        Subtitle_textL(text=score5, color=white, position=[350, 575])


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

    React_score_disp()

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


def Difficulty():
    global game_screen, difficulty

    pygame.Surface.fill(screen, background)

    # Rendering images
    screen.blit(title, [160, 80])
    Title_text(text="Choose A Difficulty", color=white, position=[640, 300])
    screen.blit(easy, [93, 400])
    screen.blit(medium, [389, 400])
    screen.blit(hard, [686, 400])
    screen.blit(quit_button, [983, 400])

    if easy.get_rect(topleft=[93, 400]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(easy_s, [93, 400])
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & easy.get_rect(topleft=[93, 400]).collidepoint(
                pygame.mouse.get_pos()):
            difficulty = "easy"
            print(difficulty)

    elif medium.get_rect(topleft=[389, 400]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(medium_s, [389, 400])
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & medium.get_rect(topleft=[389, 400]).collidepoint(
                pygame.mouse.get_pos()):
            difficulty = "medium"
            print(difficulty)
    elif hard.get_rect(topleft=[686, 400]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(hard_s, [686, 400])
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & hard.get_rect(topleft=[686, 400]).collidepoint(
                pygame.mouse.get_pos()):
            difficulty = "hard"
            print(difficulty)

    elif quit_button.get_rect(topleft=[983, 400]).collidepoint(pygame.mouse.get_pos()):
        screen.blit(quit_button_s, [983, 400])

        # Quitting the game
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1 & quit_button.get_rect(topleft=[983, 400]).collidepoint(
                pygame.mouse.get_pos()):
            game_screen = "menu"


# Main program loop
while not done:
    # Main event loop
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        # Clearing the screen
        screen.fill(background)

        # Drawing code should go here
        if game_screen == "menu":
            View_menu()

        if game_screen == "aim":
            Difficulty()

    # Update the screen with what we've drawn
    pygame.display.flip()

    # Limit to 60 fps
    clock.tick(60)

# Close the window and quit
pygame.quit()
