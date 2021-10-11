import pygame

from settings import WINDOW


class Game:
    def __init__(self):
        self.game_over = False
        self.score = 0
        # Add offset value for clean positioning so the text is not touching any border
        self.score_pos_offset = 20
        # Create a Font object from the system fonts
        self.text_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.update_score()

    def display_score(self, surface):
        """
        Draw the score surface on the game screen surface
        """
        surface.blit(self.score_surface,
                     (WINDOW['width'] - self.get_score_text_size()[0] - self.score_pos_offset,
                      WINDOW['height'] - self.get_score_text_size()[1] - self.score_pos_offset))

    def get_score_text_size(self):
        """
        Get the actual score text width and height to allow dynamic positioning.
            Returns:
                tuple: text width, text height
        """
        return self.text_font.size(self.score_txt)

    def increment_score(self):
        """
        Increment the score and call update_score to be able display the updated score value
        """
        self.score += 10
        self.update_score()

    def update_score(self):
        """
        Create/update the score surface with the score text rendered on it
        """
        self.score_txt = f'Score: {self.score}'
        # Draw score text on the score surface with antialiasing enabled in white color
        self.score_surface = self.text_font.render(self.score_txt, True, (255, 255, 255))
