import pygame
from functions.colors import BLACK

class Screen:
    screen = None
    HEIGHT = 800
    WIDTH = 600

    def getScreenSize(self):
        return (self.HEIGHT, self.WIDTH)
    
    def setScreenSize(self, size):
        (self.HEIGHT, self.WIDTH) = size

    def resetScreen(self):
        self.screen.fill(BLACK)

    def __init__(self):
        screenInfo = pygame.display.Info()
        screenSize = (screenInfo.current_w, screenInfo.current_h)
        self.setScreenSize(screenSize)

        self.screen = pygame.display.set_mode(screenSize)
        self.screen.fill(BLACK)

        pygame.display.set_caption('MAZE.AI')

        logoIcon = pygame.image.load('assets/icons/logo.png')
        pygame.display.set_icon(logoIcon)
