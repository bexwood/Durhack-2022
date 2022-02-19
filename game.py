import pygame
from pygame.locals import *

pygame.init()
width, height = 1200,729
screen = pygame.display.set_mode((width, height))

background = pygame.image.load('Images/logo.png')

while True:
    screen.blit(background, (0,0))