#!/usr/bin/python2
#Ehhh, 'ello.  It's Per, like the fruit.

import os, sys
import pygame
import network
from pygame.locals import *

netMan = network.networkManager(sys.argv)

if not pygame.font:
    print 'Warning, fonts disabled'
if not pygame.mixer:
    print 'Warning, sound disabled'

FPS = 60

pygame.display.set_caption('Ehhh, \'ello.  It\'s Per, like the fruit.')


screen = pygame.display.set_mode((600, 400))
running = True

clock = pygame.time.Clock()

while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()


    """update"""


    """draw"""

    pygame.display.flip()


    """next"""
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
