import pygame
from pygame.locals import *

from datetime import datetime, timedelta

pygame.init()
width, height = 1200,679
screen = pygame.display.set_mode((width, height))

background = pygame.image.load('Images/StartPageBackground.png')
welcome = pygame.image.load('Images/welcomeMessage.png')
rings = pygame.image.load('Images/rings.png')
tableTennis = pygame.image.load('Images/tableTennis.png')
hurdles = pygame.image.load('Images/hurdles.png')
characterSelection = pygame.image.load('Images/characterSelection.png')
uk = pygame.image.load('Images/rotated/uk.png')
us = pygame.image.load('Images/rotated/usa.png')
china = pygame.image.load('Images/rotated/china.png')
roc = pygame.image.load('Images/rotated/roc.png')
brazil = pygame.image.load('Images/rotated/brazil.png')
germany = pygame.image.load('Images/rotated/germany.png')
start = pygame.image.load('Images/start.png')
warning = pygame.image.load('Images/warning.png')

runningTrack = pygame.image.load('Images/Hurdles/runningTrack.png')
hurdle = pygame.image.load('Images/Hurdles/hurdle.png')
fallen = pygame.image.load('Images/Hurdles/fallenHurdle.png')

countries = [us, uk, roc, germany, china, brazil]
country = 0

clicked = False

startScreen = True
hurdleGame = False
tableTennisGame = False
jumping = False

hurdleCoord = [1200,400]
hurdleType = hurdle
jumperCoord = [250, 275]
counter = 0
counterStarted = False
successfulJump = 0
knockedOver = 0

while True:
    while startScreen:
        screen.fill(0)
        screen.blit(background, (0,0))
        screen.blit(welcome, (50,50))
        screen.blit (rings, (975,25))
        screen.blit (tableTennis, (100,450))
        screen.blit (hurdles, (350,450))
        screen.blit (characterSelection, (700,150))
        screen.blit (countries[country], (820, 200))
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
            print("SUCCESS: ", successfulJump, "FAILED: ",knockedOver)

            if hurdleCoord[0] == 0:
                hurdleCoord[0] = 2000
                if hurdleType == fallen:
                    hurdleType = hurdle
                    knockedOver += 1
                else:
                    successfulJump += 1


            screen.fill(0)
            screen.blit(runningTrack, (0,0))
            screen.blit(hurdleType, hurdleCoord)
            screen.blit(countries[country], jumperCoord)
            hurdleCoord[0] -=5
            pygame.display.flip()

            playerRect = pygame.Rect(countries[country].get_rect(topleft=(jumperCoord)))
            hurdleRect = pygame.Rect(hurdle.get_rect(topleft=(hurdleCoord)))

            if playerRect.colliderect(hurdleRect):
                collision = True
                hurdleType = fallen

            if counterStarted:
                counter +=1
            
            if counter > 20 and jumperCoord[1] < 275:
                jumperCoord[1] += 1
                counterStarted = False
            
            if counter == 45:
                counter = 0

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit() 
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and jumperCoord[1] > 225:
                        jumperCoord[1] -= 300
                        counterStarted = True


        while tableTennisGame and not startScreen:
            screen.fill(0)
            pygame.display.flip()
            exit(0)