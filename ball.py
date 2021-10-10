import random

import pygame.rect

from settings import WINDOW, COLORS


class Ball:
    def __init__(self, paddle, bricks):
        self.radius = 10
        self.bounces_count = 0
        self.x = (WINDOW['width'] - self.radius) / 2
        self.y = WINDOW['height'] - self.radius - 20

        self.paddle = paddle
        self.bricks = bricks

        self.init_velocity()

    def draw(self, surface):
        pygame.draw.circle(surface, COLORS['WHITE'], (self.x, self.y), self.radius)

    def init_velocity(self):
        self.x_vel = random.randint(-5, 5)
        self.y_vel = -5

    def move(self):
        if self.x < 20 or self.x > WINDOW['width'] - self.radius:
            self.bounce_x()
        self.x += self.x_vel

        if self.y < 20 or self.is_in_collision_with_paddle() or self.is_in_collision_with_brick():
            self.bounce_y()
        self.y += self.y_vel

    def bounce_x(self):
        self.x_vel = - self.x_vel
        self.bounces_count += 1

        if self.bounces_count % 20 == 0:
            self.speed_up()

    def bounce_y(self):
        self.y_vel = - self.y_vel
        self.bounces_count += 1

        if self.bounces_count % 20 == 0:
            self.speed_up()

    def is_in_collision_with_paddle(self):
        return self.paddle.rect.collidepoint(self.x, self.y)

    def is_in_collision_with_brick(self):
        for brick in self.bricks:
            if brick.rect.collidepoint(self.x, self.y):
                if brick.hp > 1:
                    brick.hp -= 1
                else:
                    self.bricks.remove(brick)
                return True

    def speed_up(self):
        if self.x_vel > 0:
            self.x_vel += 1
        else:
            self.x_vel -= 1

        if self.y_vel > 0:
            self.y_vel += 1
        else:
            self.y_vel -= 1
