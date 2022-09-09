# Street Fighter Game
# By: Adrian Adewunmi
# Date: 04/09/2022
# Version: 1.0
# Description: This is the file Fighter Class.
# Adapted from:
# Coding With Ross
# Youtube URL: https://www.youtube.com/watch?v=s5bd9KMSSW4
# GitHub URL: https://github.com/russs123/brawler_tut


import pygame


# Fighter Class
class Fighter():
    def __init__(self, x: object, y: object) -> object:
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0

    def move(self, screen_width):
        SPEED = 10
        dx = 0
        dy = 0

        # Get Key-presses
        key = pygame.key.get_pressed()

        # Player movement coordinates
        if key[pygame.K_LEFT]:
            dx = -SPEED
        if key[pygame.K_RIGHT]:
            dx = SPEED

        # Player Jumping
        if key[pygame.K_UP]:
            self.vel_y = -30

        dy += self.vel_y

        # Ensure Player Stays On Screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        # Update Player Position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
