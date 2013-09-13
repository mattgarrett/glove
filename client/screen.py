import pygame

DEFAULT_SCREEN_WIDTH = 660
DEFAULT_SCREEN_HEIGHT = 32*15+20

class Screen(object):

    def __init__(self, width=DEFAULT_SCREEN_WIDTH,
            height=DEFAULT_SCREEN_HEIGHT):

        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height))

    def display(self):
        self.window = pygame.display.set_mode((self.width, self.height))

    def update(self):
        self.window.blit(self.surface, self.surface.get_rect())
