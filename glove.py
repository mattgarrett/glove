#!/usr/bin/python2
#Ehhh, 'ello.  It's Per, like the fruit.

import os, sys
import pygame
from pygame.locals import *

if not pygame.font:
    print 'Warning, fonts disabled'
if not pygame.mixer:
    print 'Warning, sound disabled'

FPS = 60

pygame.display.set_caption('Ehhh, \'ello.  It\'s Per, like the fruit.')
background = pygame.image.load('bg.gif')

screen = pygame.display.set_mode((background.get_width(), background.get_height()))
running = True

class Guy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('guy.gif')
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.maxdx = 3
        self.maxdy = sys.maxint
        self.gravity = .3
        self.friction = .3
        self.jump = -10

    def update(self, bg, keys):
        #y velocity
        if keys[K_UP] and self.y == bg.height - self.rect.height:
            self.dy = self.dy + self.jump
        self.dy = self.dy + self.gravity

        #x velocity
        if keys[K_LEFT]:
            self.dx = self.dx - .5
        if keys[K_RIGHT]:
            self.dx = self.dx + .5
        self.dx = min(self.dx, self.maxdx)
        self.dx = max(self.dx, -1 * self.maxdx)
        if self.dx > 0:
            self.dx = max(self.dx - self.friction, 0)
        elif self.dx < 0:
            self.dx = min(self.dx + self.friction, 0)

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        #stop clipping
        if self.y + self.rect.height > bg.height:
            self.y = bg.height - self.rect.height
            self.dy = 0
        if self.x + self.rect.width > bg.width:
            self.x = bg.width - self.rect.width
            self.dx = 0
        if self.x < 0:
            self.x = 0
            self.dx = 0

guy = Guy()
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()


    """update"""
    guy.update(background.get_rect(), keys)


    """draw"""
    screen.blit(background, (0, 0))
    screen.blit(guy.image, (guy.x, guy.y))
    pygame.display.flip()


    """next"""
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
