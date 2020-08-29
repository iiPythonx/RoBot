# Modules
import pygame
from .colors import Colors

# Functions
def clear(screen, color):

    screen.fill(color)

def getInfo():

    X, Y = pygame.mouse.get_pos()

    W, H = pygame.display.get_surface().get_size()

    return X, Y, W, H
