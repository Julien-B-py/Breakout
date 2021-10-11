import pygame

from ball import Ball
from brick import Brick
from paddle import Paddle
from settings import COLORS, WINDOW
from sounds import Sound

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW['width'], WINDOW['height']))


background = pygame.image.load('bg.png')
brick_regular = pygame.image.load("brick.png")
brick_damaged = pygame.image.load("brick_damaged.png")

first_row = [Brick(x * 128, 0) for x in range(10)]
second_row = [Brick(x * 128, 40) for x in range(10)]
third_row = [Brick(x * 128, 80) for x in range(10)]
bricks = first_row + second_row + third_row

# bricks = [Brick(0,0)]

sound = Sound()

paddle = Paddle()
ball = Ball(paddle, bricks, sound)

running = True

while running:

    screen.fill(COLORS['BLACK'])
    screen.blit(background, (0, 0))
    paddle.draw(screen)
    ball.move()
    ball.draw(screen)
    # screen.blit(ball_img,(ball.x-10,ball.y-10))
    for brick in bricks:
        brick.draw(screen)
        if not brick.damaged:
            screen.blit(brick_regular, (brick.x, brick.y))
        else:
            screen.blit(brick_damaged, (brick.x, brick.y))

    # Update the display to the screen
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
