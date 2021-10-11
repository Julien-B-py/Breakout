import random

import pygame


class Brick:
    def __init__(self, x, y):
        self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.width = 128
        self.height = 40
        self.hp = random.randint(1, 3)
        self.damaged = False
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect((self.x, self.y, self.width, self.height))

    def draw(self, surface):
        self.rect = pygame.rect.Rect((self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, self.color, self.rect)

    # def take_damage(self):
    #     if self.hp > 1:
    #         self.hp -= 1
    #         self.damaged = True
    #     else:
    #         self.bricks.remove(brick)
