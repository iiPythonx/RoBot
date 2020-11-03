# Modules
import pygame
from .colors import Colors

# Functions
def clear(screen, color):

    """Clears the pygame window via filling it with the current color"""

    screen.fill(color)

def getInfo():

    """Returns information about the mouse position and display size"""

    X, Y = pygame.mouse.get_pos()
    W, H = pygame.display.get_surface().get_size()

    return X, Y, W, H
