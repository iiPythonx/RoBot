# Modules
import pygame
from .colors import Colors

# Main class
class Metrics():

    """Class to handle displaying X & Y coordinates at the top-left"""

    def __init__(self, screen, color):

        self.pos = None
        self.color = color
        self.screen = screen

    def setPos(self, pos):

        """Sets the current position for the metric update"""

        self.pos = pos

    def show(self):

        """Displays metrics using the currently set position"""

        # Just utilize the font size property
        font = pygame.font.SysFont(None, 25)

        # Blit the X & Y positions
        x = font.render("X: " + str(self.pos[0]), True, self.color)
        y = font.render("Y: " + str(self.pos[1]), True, self.color)

        self.screen.blit(x, (5, 5))
        self.screen.blit(y, (5, 25))

        # Just some credits for me :)
        self.screen.blit(font.render("Made by iiPython", True, self.color), (490, 0))
