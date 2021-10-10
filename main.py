import pygame

from ball import Ball
from brick import Brick
from paddle import Paddle
from settings import COLORS, WINDOW

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW['width'], WINDOW['height']))

first_row = [Brick(x * 128, 0) for x in range(10)]
second_row = [Brick(x * 128, 40) for x in range(10)]
third_row = [Brick(x * 128, 80) for x in range(10)]
bricks = first_row + second_row + third_row

# bricks = [Brick(0,0)]

paddle = Paddle()
ball = Ball(paddle, bricks)

running = True

while running:

    screen.fill(COLORS['BLACK'])
    paddle.draw(screen)
    ball.move()
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_q]:
        paddle.move_left()
    if keys_pressed[pygame.K_d]:
        paddle.move_right()

    clock.tick(60)
