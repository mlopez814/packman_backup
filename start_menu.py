import pygame.font

from player import Player
from settings import Settings


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class Menu:

    def __init__(self, screen, play_button):
        self.settings = Settings()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.button = play_button

        self.menu_color = (190, 190, 190)
        self.text_color = (250, 250, 210)
        self.font = pygame.font.SysFont(None, 48)

        self.title = "Pac-man"

        self.prep_screen()
#        self.create_pacman()

    def prep_screen(self):
        self.title_image = self.font.render(self.title, True, self.text_color, self.menu_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.centery = self.screen_rect.centery - 175

    def draw_menu(self):
        self.screen.fill((190, 190, 190))
        self.screen.blit(self.title_image, self.title_image_rect)
        self.button.draw_button()

#    def create_pacman(self):
#        self.settings.pac_man_index = 6
#        player = Player(self.screen)
#        player.rect.centerx = self.screen_rect.centerx - 50
#        player.rect.centery = self.screen_rect.centery - 100
