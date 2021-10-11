import pygame


class Sound:

    def __init__(self):
        self.sounds = {
            'wall_bounce': pygame.mixer.Sound("sounds/wall_bounce.ogg"),
            'paddle_bounce': pygame.mixer.Sound("sounds/paddle_bounce.ogg"),
            'brick_hit': pygame.mixer.Sound("sounds/brick_hit.ogg"),
        }

    def play(self, name):
        self.sounds[name].play()
