# My First PyGame, Bruce Johnson, 12/1/21 1:59m, v0.7

import pygame, sys 
from pygame.locals import *

#start PyGame
pygame.init() 

# Setup our window. 1
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# setup colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255)
NOTPURPLE = (154, 0, 254) 

# Setup font.
basicFont = pygame.font.SysFont(None, 48)

# Setup text.
text = basicFont.render('Hello, world!', True, WHITE, BLUE) 
textRect = text.get_rect()
textRect.centerx = windowSurface. get_rect().centerx 
textRect.centerx = windowSurface. get_rect().centery 

# Fill background color.
windowSurface.fill(NOTPURPLE) 

# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, BLACK, ((146,0), (291, 106), (236,277), (56, 277), (0, 106)))

# Draw line on the screen.
pygame.draw.line(windowSurface, WHITE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, GREEN, (75, 60), (60, 75), 2)
pygame.draw.line(windowSurface, RED, (0, 150), (150, 0), 1)

# Draw a circle.
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)