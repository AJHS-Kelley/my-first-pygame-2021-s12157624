# Simple Animation with PyGame, Bruce Johnson, 1/11/22, 2:19pm. v0.2

import pygame, sys, time
from pygame.locals import *

# Sutup PyGame
pygame.init()

# setup the widow
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example')

# setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4 
