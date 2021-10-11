import pygame

from settings import WINDOW


class Game:
    def __init__(self):
        self.game_over = False
        self.score = 0
        self.score_pos_offset = 10
        self.text_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.update_score()

    def display_score(self, surface):
        surface.blit(self.score_surface,
                     (WINDOW['width'] - self.get_score_text_size()[0] - self.score_pos_offset,
                      WINDOW['height'] - self.get_score_text_size()[1] - self.score_pos_offset))

    # Get the actual score text width and height to allow real time positioning adjustements
    def get_score_text_size(self):
        return self.text_font.size(self.score_txt)

    def increment_score(self):
        self.score += 10
        self.update_score()

    def update_score(self):
        self.score_txt = f'Score: {self.score}'
        self.score_surface = self.text_font.render(self.score_txt, False, (255, 255, 255))
