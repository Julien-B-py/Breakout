import random

import pygame.rect

from settings import WINDOW


class Ball:
    def __init__(self, paddle, bricks, sound, game):
        """ Create a new instance of the ball object. """
        self.radius = 10
        self.bounces_count = 0
        # Starting position of the center of the ball
        self.x = WINDOW['width'] / 2
        self.y = WINDOW['height'] - self.radius - 30


        # # bottom left corner
        # self.x = 0+self.radius
        # self.y=720-self.radius

        self.image = pygame.image.load('images/ball.png')

        self.paddle = paddle
        self.bricks = bricks
        self.sound = sound
        self.game = game

        self.init_velocity()

    def draw(self, surface):

        surface.blit(self.image, (self.x - 10, self.y - 10))

        # pygame.draw.circle(surface, COLORS['WHITE'], (self.x, self.y), self.radius)

    def init_velocity(self):
        self.x_vel = random.randint(-5, 5)
        while self.x_vel == 0:
            self.x_vel = random.randint(-5, 5)
        self.y_vel = random.randint(-5, -3)

    def move(self):
        if self.x < self.radius or self.x > WINDOW['width'] - self.radius:
            self.bounce_x()
            self.sound.play('wall_bounce')
        self.x += self.x_vel

        if self.y < self.radius or self.is_in_collision_with_paddle():
            self.bounce_y()
            if self.y < self.radius:
                self.sound.play('wall_bounce')
            else:

                self.sound.play('paddle_bounce')

        self.y += self.y_vel

        self.is_in_collision_with_brick()

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
        # If ball position is between left and right sides of the paddle
        if self.paddle.rect.left <= self.x <= self.paddle.rect.right:
            # If ball position above the paddle and the distance between ball and paddle is less than a ball radius
            if self.y < self.paddle.rect.top and self.paddle.rect.top - self.y <= self.radius:
                return True
        return False

    def is_in_collision_with_brick(self):
        for brick in self.bricks:
            # Check vertical collisions
            if brick.rect.left <= self.x <= brick.rect.right:
                # Collision with bottom side of the brick
                # If ball is under the brick and distance between the ball and the bottom of brick is less than a ball radius
                if self.y > brick.rect.bottom and self.y - brick.rect.bottom <= self.radius:

                    self.bounce_y()

                    self.sound.play('brick_hit')

                    if brick.hp > 1:
                        brick.hp -= 1
                        brick.damaged = True
                    else:
                        self.bricks.remove(brick)

                    self.game.increment_score()

                    break

                # Collision with top side of the brick
                # If ball is above the brick and distance between the ball and the top of brick is less than a ball radius
                elif self.y < brick.rect.top and brick.rect.top - self.y <= self.radius:

                    self.bounce_y()

                    self.sound.play('brick_hit')

                    if brick.hp > 1:
                        brick.hp -= 1
                        brick.damaged = True
                    else:
                        self.bricks.remove(brick)

                    self.game.increment_score()

                    break

            # Check horizontal collisions
            if brick.rect.top <= self.y <= brick.rect.bottom:
                # Collision with right side of the brick
                # If ball is on the right of the brick and distance between the ball and the right of brick is less than a ball radius
                if self.x > brick.rect.right and self.x - brick.rect.right <= self.radius:

                    self.bounce_x()

                    self.sound.play('brick_hit')

                    if brick.hp > 1:
                        brick.hp -= 1
                        brick.damaged = True
                    else:
                        self.bricks.remove(brick)

                    self.game.increment_score()

                    break

                # Collision with left side of the brick
                # If ball is on the left of the brick and distance between the ball and the left of brick is less than a ball radius
                elif self.x < brick.rect.left and brick.rect.left - self.x <= self.radius:

                    self.bounce_x()

                    self.sound.play('brick_hit')

                    if brick.hp > 1:
                        brick.hp -= 1
                        brick.damaged = True
                    else:
                        self.bricks.remove(brick)

                    self.game.increment_score()

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
