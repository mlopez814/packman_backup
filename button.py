import pygame.font


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class Button:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 200

        self.rect2 = pygame.Rect(0, 0, self.width, self.height)
        self.rect2.centerx = self.screen_rect.centerx
        self.rect2.centery = self.screen_rect.centery + 125

        self.prep_msg("play")

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
