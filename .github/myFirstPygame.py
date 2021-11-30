# My First PyGame, Gabriel Gilley, 11/30/21, 2:36PM, v 0.3

import pygame, sys
from pygame.locals import *

# Start PyGame
pygame.init()

# Setup the game window.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup color values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LAVISHPURPLE = (129, 66, 212)