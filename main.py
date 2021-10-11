import pygame

from ball import Ball
from brick import Brick
from game import Game
from paddle import Paddle
from settings import WINDOW
from sounds import Sound

pygame.init()

# Create a clock object to track time
clock = pygame.time.Clock()

# GAME WINDOW
# Set the game window dimensions
screen = pygame.display.set_mode((WINDOW['width'], WINDOW['height']))
# Set the title
pygame.display.set_caption('Breakout!')
# Set the icon
icon = pygame.image.load('images/ball.png')
pygame.display.set_icon(icon)

# IMAGES
background = pygame.image.load('images/bg3.png')
brick_regular = pygame.image.load("images/brick.png")
brick_damaged = pygame.image.load("images/brick_damaged.png")

# Create all objects
# Create 3 lines of 10 bricks with a 128px horizontal spacing and 40px vertical spacing
first_row = [Brick(x * 128, 0) for x in range(10)]
second_row = [Brick(x * 128, 40) for x in range(10)]
third_row = [Brick(x * 128, 80) for x in range(10)]
# Merge all rows of bricks into one
bricks = first_row + second_row + third_row

# Testing line with only one brick
# bricks = [Brick(0,0)]

game = Game()
sound = Sound()
paddle = Paddle()
ball = Ball(paddle, bricks, sound, game)


# Game main loop
while not game.game_over:

    # Draw the background image
    screen.blit(background, (0, 0))
    # Draw the paddle
    paddle.draw(screen)

    # Ball movement and display
    ball.move()
    ball.draw(screen)
    # screen.blit(ball_img,(ball.x-10,ball.y-10))

    # Bricks display
    for brick in bricks:
        # Draw simple rectangle
        brick.draw(screen)
        # Draw brick image overlay depending on brick state
        if not brick.damaged:
            screen.blit(brick_regular, (brick.x, brick.y))
        # If brick is damaged draw a damaged brick image
        else:
            screen.blit(brick_damaged, (brick.x, brick.y))

    # If all bricks have been destroyed game is over
    if not bricks:
        game.game_over = True

    # Draw the score board
    game.display_score(screen)

    # Quit the game if the user click the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.game_over = True

    # Paddle movements with keypresses detection
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_q]:
        paddle.move_left()
    if keys_pressed[pygame.K_d]:
        paddle.move_right()

    # Update the display to the screen
    pygame.display.update()
    # Set framerate limit to 60
    clock.tick(60)
