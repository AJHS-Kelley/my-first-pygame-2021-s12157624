# Simple Animation with PyGame, Bruce Johnson, 12/9/21, 2:14pm. v0.1 

import pygame, sys, time
from pygame.locals import *

# Sutup PyGame
pygame.init()

# setup the widow
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example')
