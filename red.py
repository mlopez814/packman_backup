import pygame
from settings import Settings


def load_image(self):
    image = pygame.image.load(self)
    return image


class Red:
    BRICK_SIZE = 15

    def __init__(self, screen, mazefile):
        self.screen = screen
        self.settings = Settings()
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.deltax = self.deltay = Red.BRICK_SIZE

        self.centerx = 0
        self.centery = 0
        self.build()

        self.images = []
        self.images.append(load_image('images/Ghost/Red/RedD3.png'))
        self.images.append(load_image('images/Ghost/Red/RedD4.png'))
        self.images.append(load_image('images/Ghost/Red/RedL3.png'))
        self.images.append(load_image('images/Ghost/Red/RedL4.png'))
        self.images.append(load_image('images/Ghost/Red/RedR3.png'))
        self.images.append(load_image('images/Ghost/Red/RedR4.png'))
        self.images.append(load_image('images/Ghost/Red/RedU3.png'))
        self.images.append(load_image('images/Ghost/Red/RedU4.png'))

        self.index = self.settings.pac_man_index
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def build(self):
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'R':
                    self.centerx += (ncol + .5) * dx
                    self.centery += (nrow + .5) * dy

    def blitme(self):
            self.screen.blit(self.image, self.rect)

    def update(self, maze):
        collisions = pygame.Rect.colliderect(self.rect, maze.bricks[501])

        if self.moving_up:
            self.centery -= self.settings.pac_man_speedfactor
            self.index = 6
        if self.moving_down:
            self.centery += self.settings.pac_man_speedfactor
            self.index = 0
        if self.moving_right:
            self.centerx += self.settings.pac_man_speedfactor
            self.index = 4
        if self.moving_left and not collisions:
            self.centerx -= self.settings.pac_man_speedfactor
            self.index = 2

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

        self.animate()

    def animate(self):
        self.index += 1
        if self.index == 2:
             self.index = 0
        if self.index == 4:
            self.index = 2
        if self.index == 6:
            self.index = 4
        if self.index >= 8:
            self.index = 6
        self.image = self.images[self.index]
