# PyGame Collision Detection Practice, Johnson Bruce, January 25, 2022, 2:19pm, v0.6

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

# Setup colors.
BLACK = (0, 0, 0)
GREEN =(0, 255, 0)
WHITE = (255, 255, 255)

# Setup the player and food data stuctures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100,50,50)
foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.radint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Movement Variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveleft = False
                moveright = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True    