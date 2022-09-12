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
        self.jump = False
        self.attack_type = 0

    def move(self, screen_width, screen_height, surface):
        SPEED = 10
        GRAVITY = 2
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
        if key[pygame.K_UP] and self.jump == False:
            self.vel_y = -30
            self.jump = True

        # Player Attacking
        if key[pygame.K_r] or key[pygame.K_t]:
            self.attack(surface)
            # Determine which attack type was used
            if key[pygame.K_r]:
                self.attack_type = 1
            if key[pygame.K_t]:
                self.attack_type = 2

        # Player Return From Jumping
        self.vel_y += GRAVITY
        dy += self.vel_y

        # Ensure Player Stays On Screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom

        # Update Player Position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
