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
        while self.x_vel == 0:
            self.x_vel = random.randint(-5, 5)

        self.y_vel = -5

    def move(self):
        if self.x < self.radius or self.x > WINDOW['width'] - self.radius:
            self.bounce_x()
        self.x += self.x_vel

        if self.y < self.radius or self.is_in_collision_with_paddle() or self.is_in_collision_with_brick():
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
            # Check vertical collisions
            if brick.rect.left <= self.x <= brick.rect.right:
                # Collision with bottom side of the brick
                # If ball is under the brick and distance between the ball and the bottom of brick is less than a ball radius
                if self.y > brick.rect.bottom and self.y - brick.rect.bottom <= self.radius:


                    self.bounce_y()

                    if brick.hp > 1:
                        brick.hp -= 1
                    else:
                        self.bricks.remove(brick)

                    break

                # Collision with top side of the brick
                # If ball is above the brick and distance between the ball and the top of brick is less than a ball radius
                elif self.y < brick.rect.top and brick.rect.top - self.y <= self.radius:


                    self.bounce_y()

                    if brick.hp > 1:
                        brick.hp -= 1
                    else:
                        self.bricks.remove(brick)

                    break


            # Check horizontal collisions
            elif brick.rect.top <= self.y <= brick.rect.bottom:
                # Collision with right side of the brick
                # If ball is on the right of the brick and distance between the ball and the right of brick is less than a ball radius
                if self.x > brick.rect.right and self.x - brick.rect.right <= self.radius:


                    self.bounce_x()

                    if brick.hp > 1:
                        brick.hp -= 1
                    else:
                        self.bricks.remove(brick)

                    break

                # Collision with left side of the brick
                # If ball is on the left of the brick and distance between the ball and the left of brick is less than a ball radius
                elif self.x < brick.rect.left and brick.rect.left - self.x <= self.radius:


                    self.bounce_x()

                    if brick.hp > 1:
                        brick.hp -= 1
                    else:
                        self.bricks.remove(brick)

                    break




    def speed_up(self):
        if self.x_vel > 0:
            self.x_vel += 1
        else:
            self.x_vel -= 1

        if self.y_vel > 0:
            self.y_vel += 1
        else:
            self.y_vel -= 1
