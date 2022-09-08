import pygame


# Fighter Class
class Fighter():
    def __init__(self, x: object, y: object) -> object:
        self.rect = pygame.Rect((x, y, 80, 180))

    def move(self):
        SPEED = 10
        dx = 0
        dy = 0

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
