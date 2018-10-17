import pygame.font
from pygame.sprite import Group

from player import Player


class Scoreboard:
    def __init__(self, settings, screen, stats, maze):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.settings = settings
        self.maze = maze
        self.stats = stats

        self.text_color = (250, 250, 210)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives(self.settings, self.screen, self.stats, self.maze)

    def prep_score(self):
        score_str = "Score: {:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.lives.draw(self.screen)

    def prep_high_score(self):
        high_score_str = "High score: {:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        current_level = self.stats.level
        current_level_str = "Level: {:,}".format(current_level)
        self.level_image = self.font.render(current_level_str, True, self.text_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.score_rect.bottom

    def prep_lives(self, settings, screen, stats, maze):
        self.lives = Group()

        for lives_number in range(stats.pacman_lives):
            life = Player(settings, screen, stats, self, maze)
            life.rect.centerx = (self.screen_rect.left + 45) + (lives_number * 45)
            life.rect.centery = self.screen_rect.bottom - 100
            self.lives.add(life)