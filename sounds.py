import pygame


class Sound:

    def __init__(self):
        self.sounds = {
            'wall_bounce': pygame.mixer.Sound("wall_bounce.ogg"),
            'paddle_bounce': pygame.mixer.Sound("paddle_bounce.ogg"),
            'brick_hit': pygame.mixer.Sound("brick_hit.mp3"),
        }

    def play(self, name):
        self.sounds[name].play()
