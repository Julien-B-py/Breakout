import pygame


class Sound:

    def __init__(self):
        # Create a dict of new Sound objects from audio files
        self.sounds = {
            'wall_bounce': pygame.mixer.Sound("sounds/wall_bounce.ogg"),
            'paddle_bounce': pygame.mixer.Sound("sounds/paddle_bounce.ogg"),
            'brick_hit': pygame.mixer.Sound("sounds/brick_hit.ogg"),
        }

    def play(self, sound_name):
        """
        Begin specified Sound object playback
        """
        self.sounds[sound_name].play()
