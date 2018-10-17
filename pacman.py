import pygame

import pygame.gfxdraw

from maze import Maze
from eventloop import EventLoop
from player import Player
from settings import Settings
from red import Red
from blue import Blue
from orange import Orange
from pink import Pink
from start_menu import Menu
from button import Button
from game_stats import Stats
from scoreboard import Scoreboard


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((735, 800))
        pygame.display.set_caption("Pac-man")
        self.settings = Settings()

        self.radius = 1
        self.start = 2
        self.end = 10
        self.begin = pygame.time.get_ticks()
        self.wait = 800

        self.stats = Stats(self.settings)

        self.pb = Button(self.screen)
        self.menu = Menu(self.screen, self.pb)

        self.maze = Maze(self.screen, 'images/maze.txt', 'images/cube0.png', 'images/gate0.png', 'images/dot0.png')

        self.sb = Scoreboard(self.settings, self.screen, self.stats, self.maze)

        self.player = Player(self.settings, self.screen, self.stats, self.sb, self.maze)
        self.red = Red(self.screen, 'images/maze.txt')
        self.blue = Blue(self.screen, 'images/maze.txt')
        self.orange = Orange(self.screen, 'images/maze.txt')
        self.pink = Pink(self.screen, 'images/maze.txt')

    def open_portal(self, x, y, color):
        for r in range(self.start, self.end):
            pygame.gfxdraw.circle(self.screen, x, y, r, color)
        now = pygame.time.get_ticks()
        if (now < self.begin + self.wait):
            self.inc = 1
        elif (now < self.begin + 4 * self.wait):
            self.inc = 0
        else:
            self.inc = -1

        self.start += self.inc
        self.start = max(1, self.start)
        self.end += self.inc

    def play(self):
        clock = pygame.time.Clock()
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.check_events(self.settings, self.stats, self.player, self.pb, self.maze)
            self.menu.prep_screen()

            if self.stats.game_active:
                self.player.update(self.maze)
                self.red.update(self.maze)
                self.blue.update(self.maze)
                self.orange.update(self.maze)
                self.pink.update(self.maze)

            self.display_game()
            clock.tick(20)

    def display_game(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme()
        self.open_portal(365, 550, (240, 100, 20))
        self.player.blitme()
        self.red.blitme()
        self.blue.blitme()
        self.orange.blitme()
        self.pink.blitme()
        self.sb.show_score()

        if not self.stats.game_active:
            self.menu.draw_menu()

        pygame.display.flip()


game = Game()
game.play()
