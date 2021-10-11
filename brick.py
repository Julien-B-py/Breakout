import random

import pygame


class Brick:
    def __init__(self, x, y):
        # Pick a random color and a random amount of health points for each new brick created
        self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.hp = random.randint(1, 3)

        self.width = 128
        self.height = 40
        self.damaged = False
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect((self.x, self.y, self.width, self.height))

    def draw(self, surface):
        """
        Draw the paddle image on the game screen surface.
        Determine his rectangular coordinates to allow movements and ball interactions
        """
        pygame.draw.rect(surface, self.color, self.rect)
        self.rect = pygame.rect.Rect((self.x, self.y, self.width, self.height))

    def take_damage(self, bricks_list):
        """
        Lower current brick HP from 1 when the ball hits it.
        Destroy it if no HP left.
        """
        # If brick HP greater than 1 remove 1 HP
        if self.hp > 1:
            self.hp -= 1
            # Set damage attribute to True to change the brick appearance
            self.damaged = True
        # If brick HP reach zero the brick is destroyed and removed
        else:
            bricks_list.remove(self)


