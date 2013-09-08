#!/usr/bin/python2
#Ehhh, 'ello.  It's Per, like the fruit.

import os, sys
import pygame
import gflags
import network
from pygame.locals import *

FLAGS = gflags.FLAGS

gflags.DEFINE_string("mode", None, "join, host, or dedicated",
        short_name="m")
gflags.DEFINE_string("dedicated_ip", None, "ip to run the dedicated service on",
        short_name="dip")
gflags.DEFINE_integer("dedicated_port", None, "port to run the dedicated service on",
        short_name="dp")

FLAGS(sys.argv)

netMan = network.networkManager(FLAGS.mode, FLAGS.dedicated_ip, FLAGS.dedicated_port)

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
