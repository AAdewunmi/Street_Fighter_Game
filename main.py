# Street Fighter Game
# By: Adrian Adewunmi
# Date: 04/09/2022
# Version: 1.0
# Description: This is the main file for the Street Fighter Game.
#             It contains the main game loop and the main game functions.
#             It also contains the main menu and the game over screen.
#             It also contains the high score screen.
#             It also contains the pause screen.
#             It also contains the game over screen.
# Adapted from:
# Coding With Ross
# Youtube URL: https://www.youtube.com/watch?v=s5bd9KMSSW4
# GitHub URL: https://github.com/russs123/brawler_tut


import pygame
from fighter import Fighter

# Initialise Pygame
pygame.init()

# Create Game Window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Fighter!")

# Set Framerate
clock = pygame.time.Clock()
FPS = 60

# Load Background Image
bg_image = pygame.image.load("assets/images/background.jpg").convert_alpha()


# Function For Drawing Background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# Create Two Instances Of Fighter
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

# Create Game Loop
run = True
while run:
    clock.tick(FPS)
    # Draw Background
    draw_bg()
    # Move Fighters
    fighter_1.move(SCREEN_WIDTH)
    # fighter_2.move()
    # Draw Fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    # Implement Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Update Display
    pygame.display.update()
# Exit PyGame
pygame.quit()
