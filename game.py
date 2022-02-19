import pygame
from pygame.locals import *

pygame.init()
width, height = 1200,679
screen = pygame.display.set_mode((width, height))

background = pygame.image.load('Images/StartPageBackground.png')
welcome = pygame.image.load('Images/welcomeMessage.png')
rings = pygame.image.load('Images/rings.png')
tableTennis = pygame.image.load('Images/tableTennis.png')
hurdles = pygame.image.load('Images/hurdles.png')
characterSelection = pygame.image.load('Images/characterSelection.png')
uk = pygame.image.load('Images/uk.png')
us = pygame.image.load('Images/usa.png')
china = pygame.image.load('Images/china.png')
roc = pygame.image.load('Images/roc.png')
brazil = pygame.image.load('Images/brazil.png')
germany = pygame.image.load('Images/germany.png')
start = pygame.image.load('Images/start.png')
warning = pygame.image.load('Images/warning.png')

countries = [us, uk, roc, germany, china, brazil]
country = 0

clicked = False

startScreen = True
hurdleGame = False
tableTennisGame = False

while True:
    while startScreen:
        screen.blit(background, (0,0))
        screen.blit(welcome, (50,50))
        screen.blit (rings, (975,25))
        screen.blit (tableTennis, (100,450))
        screen.blit (hurdles, (350,450))
        screen.blit (characterSelection, (700,150))
        screen.blit (countries[country], (760, 200))
        screen.blit (start, (790, 525))

        if clicked:
            screen.blit (warning, (765, 625))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() 
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if pos[0]>715 and pos[0]<790 and pos[1]>250 and pos[1]<365:     #back arrow
                    if country==0:
                        country=5
                    else:
                        country-=1
                if pos[0]>1050 and pos[0]<1150 and pos[1]>250 and pos[1]<365:     #next arrow
                    if country==5:
                        country=0
                    else:
                        country+=1

                if pos[0]>100 and pos[0]<295 and pos[1]>455 and pos[1]<640:
                    tableTennisGame = True
                    hurdleGame = False

                if pos[0]>350 and pos[0]<550 and pos[1]>455 and pos[1]<640:
                    hurdleGame = True
                    tableTennisGame = False
                
                if pos[0]>790 and pos[0]<1040 and pos[1]>525 and pos[1]<620:
                    if hurdleGame or tableTennisGame:
                        startScreen = False
                    else:
                        clicked = True
                        screen.blit (warning, (765, 625))
                        pygame.display.flip()

        while hurdleGame and not startScreen:
            screen.fill(0)
            pygame.display.flip()

        while tableTennisGame and not startScreen:
            screen.fill(0)
            pygame.display.flip()