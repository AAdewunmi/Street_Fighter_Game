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

# Define Colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Load Background Image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

# Load Warrior Sprite sheets Of Images
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
# Load Wizard Sprite sheets Of Images
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

# Define number of steps in each animation for Warrior and Wizard Player
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]


# Function For Drawing Background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# Function For Drawing Fighter Health Bar
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 5, y - 5, 410, 40))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, (400 * ratio), 30))


# Create Two Instances Of Fighter
fighter_1 = Fighter(200, 310, warrior_sheet, WARRIOR_ANIMATION_STEPS)
fighter_2 = Fighter(700, 310, wizard_sheet, WIZARD_ANIMATION_STEPS)

# Create Game Loop
run = True
while run:
    clock.tick(FPS)
    # Draw Background
    draw_bg()
    # Show Player Stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)
    # Move Fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
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
