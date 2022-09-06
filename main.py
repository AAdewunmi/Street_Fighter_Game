import pygame

# Initialise Pygame
pygame.init()

# Create Game Window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Fighter!")

# Load Background Image
bg_image = pygame.image.load("assets/images/background.jpg").convert_alpha()


# Function For Drawing Background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# Create Game Loop
run = True
while run:
    # Draw Background
    draw_bg()
    # Implement Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Update Display
    pygame.display.update()
# Exit PyGame
pygame.quit()
