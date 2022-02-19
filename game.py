import pygame
from pygame.locals import *

pygame.init()
width, height = 800,600
screen = pygame.display.set_mode((width, height))

background = pygame.image.load('Images/logo.png')

while True:
    screen.fill(0)
    screen.blit(background, (0,0))
    pygame.display.flip()
