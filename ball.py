import random

import pygame.rect

from settings import WINDOW


class Ball:
    def __init__(self, paddle, bricks, sound, game):
        self.radius = 10
        self.bounces_count = 0
        # Starting position of the center of the ball
        # Horizontally centered
        self.x = WINDOW['width'] / 2
        self.y = WINDOW['height'] - self.radius - 30
        self.image = pygame.image.load('images/ball.png')

        self.paddle = paddle
        self.bricks = bricks
        self.sound = sound
        self.game = game

        self.init_velocity()

    def draw(self, surface):
        """
        Draw the ball image on the game screen surface.
        """
        surface.blit(self.image, (self.x - 10, self.y - 10))

    def init_velocity(self):
        """
        Determine initial ball x and y movement behavior
        """
        # Pick a random value to determine how much pixels the ball will travel horizontally
        self.x_vel = random.randint(-5, 5)
        # If random value is 0, pick another random value until it is different from 0 so we dont have the ball moving
        # up/down in a straight line.
        while self.x_vel == 0:
            self.x_vel = random.randint(-5, 5)
        # Pick a random value to determine how much pixels the ball will travel vertically
        self.y_vel = random.randint(-7, -4)

    def move(self):
        """
        Move the ball depending on x-velocity and y-velocity values
        """
        # If ball hits left or right wall
        if self.x < self.radius or self.x > WINDOW['width'] - self.radius:
            self.bounce_x()
            self.sound.play('wall_bounce')

        # If ball hits the top wall or the paddle
        if self.y < self.radius or self.is_in_collision_with_paddle():
            self.bounce_y()
            # If ball hits the top wall play a sound
            if self.y < self.radius:
                self.sound.play('wall_bounce')
            # If ball hits the paddle play another sound
            else:
                self.sound.play('paddle_bounce')

        self.check_collision_with_brick()

        # If ball drop under the paddle: GAME OVER
        if self.y >= WINDOW['height'] + self.radius:
            self.game.game_over = True

        # Update ball x and y coordinates
        self.x += self.x_vel
        self.y += self.y_vel

    def bounce_x(self):
        """
        Reverse the x-velocity value to make the ball travel in the other direction
        """
        self.x_vel = - self.x_vel
        self.bounces_count += 1

        # Every 20 bounces increase ball speed
        if self.bounces_count % 20 == 0:
            self.speed_up()

    def bounce_y(self):
        """
        Reverse the y-velocity value to make the ball travel in the other direction
        """
        self.y_vel = - self.y_vel
        self.bounces_count += 1

        # Every 20 bounces increase ball speed
        if self.bounces_count % 20 == 0:
            self.speed_up()

    def is_in_collision_with_paddle(self):
        """
        Check if the ball and the paddle are touching each other
            Returns:
                bool: True if paddle and ball are in contact. False otherwise.
        """
        # If ball x-position is between left and right sides of the paddle
        # If ball y-position is above the paddle and the distance between ball and paddle is less than a ball radius
        return (
            self.paddle.rect.left <= self.x <= self.paddle.rect.right
            and self.y < self.paddle.rect.top
            and self.paddle.rect.top - self.y <= self.radius
        )

    def check_collision_with_brick(self):
        """
        Check if the ball and any of the bricks are touching each other.
        Depending on the side the ball is in contact with the bounce direction will be different.
        """
        for brick in self.bricks:
            collision = False
            # Check vertical collisions
            # Collision with bottom or top side of the brick
            if brick.rect.left <= self.x <= brick.rect.right:

                # If ball is under the brick and distance between the ball and the bottom of brick is less than a
                # ball radius
                collision_with_bottom = self.y > brick.rect.bottom and self.y - brick.rect.bottom <= self.radius
                # If ball is above the brick and distance between the ball and the top of brick is less than a ball
                # radius
                collision_with_top = self.y < brick.rect.top and brick.rect.top - self.y <= self.radius

                # If any vertical collision is detected
                if collision_with_bottom or collision_with_top:
                    collision = True
                    self.bounce_y()

            # Check horizontal collisions
            # Collision with right or left side of the brick
            elif brick.rect.top <= self.y <= brick.rect.bottom:

                # If ball is on the right of the brick and distance between the ball and the right of brick is less
                # than a ball radius
                collision_with_right = self.x > brick.rect.right and self.x - brick.rect.right <= self.radius
                # Collision with left side of the brick If ball is on the left of the brick and distance between the
                # ball and the left of brick is less than a ball radius
                collision_with_left = self.x < brick.rect.left and brick.rect.left - self.x <= self.radius

                # If any horizontal collision is detected
                if collision_with_right or collision_with_left:
                    collision = True
                    self.bounce_x()

            # If any collision is detected with a brick
            if collision:
                # Play sound effect
                self.sound.play('brick_hit')
                # Reduce brick HP
                brick.take_damage(self.bricks)
                # Add 10 to player score
                self.game.increment_score()

    def speed_up(self):
        """
        Increase ball velocity
        """
        # If current x-axis velocity is positive add positive offset
        if self.x_vel > 0:
            self.x_vel += 1
        else:
            self.x_vel -= 1

        # If current y-axis velocity is positive add positive offset
        if self.y_vel > 0:
            self.y_vel += 1
        else:
            self.y_vel -= 1
