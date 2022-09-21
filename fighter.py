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
    def __init__(self, x, y, flip, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        # 0:idle #1:run #2:jump #3:attack1 #4:attack2 #5:hit #6:death
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.running = False
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
                temp_img_list.append(
                    pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.running = False

        # Get Key-presses
        key = pygame.key.get_pressed()

        # Can only perform other actions if not currently attacking
        if not self.attacking:

            # Player movement coordinates
            if key[pygame.K_a]:
                dx = -SPEED
                self.running = True
            if key[pygame.K_d]:
                dx = SPEED
                self.running = True

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

    # Handle animation updates

    def update(self):
        # Check what action the player is performing
        if self.running:
            self.action = 1
        else:
            self.action = 0
        animation_cooldown = 50
        # Update Image
        self.image = self.animation_list[self.action][self.frame_index]
        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # Check if the animation has finished
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0


    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip),
                                     self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale),
                           self.rect.y - (self.offset[1] * self.image_scale)))
