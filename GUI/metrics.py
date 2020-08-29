# Modules
import pygame
from .colors import Colors

# Main class
class Metrics():

    def __init__(self, screen, color):

        self.screen = screen

        self.pos = None

        self.color = color

    def setPos(self, pos):

        self.pos = pos

    def show(self):

        font = pygame.font.SysFont(None, 25)

        x = font.render("X: " + str(self.pos[0]), True, self.color)

        y = font.render("Y: " + str(self.pos[1]), True, self.color)

        self.screen.blit(x, (5, 5))

        self.screen.blit(y, (5, 25))

        self.screen.blit(font.render("Made by iiPython", True, self.color), (500, 0))
