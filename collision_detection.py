# PyGame Collision Detection Practice, Johnson Bruce, January 04, 2022, 2:06pm, v0.2

import pygame, sys, random
from pygame.locals import*

# Setup PyGame
pygame.init()
mainClock = pygame.time.Clock() 

# Setup the PyGame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.sett_caption('collision Detection 2022')