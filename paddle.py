import pygame.rect

from settings import WINDOW


class Paddle:
    def __init__(self):
        self.width = 150
        self.height = 20
        self.x = (WINDOW['width'] - self.width) / 2
        self.y = WINDOW['height'] - self.height
        # self.rect = pygame.rect.Rect((self.x, self.y, self.width, self.height))

        self.image = pygame.image.load('images/paddle.png')

    def draw(self, surface):
        """
        Draw the paddle image on the game screen surface.
        Determine his rectangular coordinates to allow movements and ball interactions
        """
        surface.blit(self.image, (self.x, self.y))
        self.rect = pygame.rect.Rect((self.x, self.y, self.width, self.height))

    def move_left(self):
        """Move paddle to the left if it is possible"""
        # If paddle is not touching left border
        if self.x >= 0:
            self.x -= 15

    def move_right(self):
        """Move paddle to the right if it is possible"""
        # If paddle is not touching right border
        if self.x <= WINDOW['width'] - self.width:
            self.x += 15
