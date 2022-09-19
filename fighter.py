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
    def __init__(self, x, y, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.flip = False
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def load_images(self, sprite_sheet, animation_steps):
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)
        return animation_list

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # Get Key-presses
        key = pygame.key.get_pressed()

        # Can only perform other actions if not currently attacking
        if not self.attacking:

            # Player movement coordinates
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED

            # Player Jumping
            if key[pygame.K_UP] and self.jump == False:
                self.vel_y = -30
                self.jump = True

            # Player Attacking
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)
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

        # Ensure Players Face Each Other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True
        # Update Player Position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip),
                                     self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
