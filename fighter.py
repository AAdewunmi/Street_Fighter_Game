import pygame


# Fighter Class
class Fighter():
    def __init__(self, x: object, y: object) -> object:
        self.rect = pygame.Rect((x, y, 80, 180))

    @staticmethod
    def move(self):
        SPEED = 10
        dx = 0
        dy = 0

        # Get Key-presses
        key = pygame.key.get_pressed()

        # Player movement coordinates
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
        # Update Player Position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
