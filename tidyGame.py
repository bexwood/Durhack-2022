import pygame
from pygame.locals import *
import math
from datetime import datetime, timedelta
import time

### Loading all images ###

#Start Screen
startScreenBackground = pygame.image.load('Images/StartScreen/StartPageBackground.png')
welcomeMessage = pygame.image.load('Images/StartScreen/welcomeMessage.png')
olympicRings = pygame.image.load('Images/StartScreen/rings.png')
tableTennis = pygame.image.load('Images/StartScreen/tableTennis.png')
hurdles = pygame.image.load('Images/StartScreen/hurdles.png')
characterSelection = pygame.image.load('Images/StartScreen/characterSelection.png')
startButton = pygame.image.load('Images/StartScreen/startButton.png')
warning = pygame.image.load('Images/StartScreen/warning.png')

#Characters
uk = pygame.image.load('Images/Characters/uk.png')
us = pygame.image.load('Images/Characters/usa.png')
china = pygame.image.load('Images/Characters/china.png')
roc = pygame.image.load('Images/Characters/roc.png')
brazil = pygame.image.load('Images/Characters/brazil.png')
germany = pygame.image.load('Images/Characters/germany.png')

#Medals
gold = pygame.image.load('Images/Medals/gold.png')
silver = pygame.image.load('Images/Medals/silver.png')
bronze = pygame.image.load('Images/Medals/bronze.png')

#Hurdle Game Images
runningTrack = pygame.image.load('Images/Hurdles/runningTrack.png')
standingHurdle = pygame.image.load('Images/Hurdles/hurdle.png')
fallenHurdle = pygame.image.load('Images/Hurdles/fallenHurdle.png')
finishLine = pygame.image.load('Images/Hurdles/finishLine.png')

### Setting up parameters used throughout ###

#to determine the users country 
countries = [us, uk, roc, germany, china, brazil]
country = 0

#to determine which screen to go to
clicked = False
startScreen = True
hurdleGame = False
hurdleResults = False
tableTennisGame = False

#hurdle game parameters
jumping = False
hurdleCoord = [1200,400]
hurdleType = standingHurdle
jumperCoord = [250, 275]
counter = 0
counterStarted = False
successfulJump = 0
knockedOver = 0
finishLineCoord = [1200, 350]

pygame.init()
width, height = 1200,679
screen = pygame.display.set_mode((width, height))

base_font = pygame.font.Font(None,40)
font = pygame.font.Font('RIO2016.TTF', 48)

while True:
    while startScreen:
        screen.fill(0)
        screen.blit(startScreenBackground, (0,0))
        screen.blit(welcomeMessage, (50,50))
        screen.blit (olympicRings, (975,25))
        screen.blit (tableTennis, (100,450))
        screen.blit (hurdles, (350,450))
        screen.blit (characterSelection, (700,150))
        screen.blit (countries[country], (820, 200))
        screen.blit (startButton, (790, 525))

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

        if hurdleGame and not startScreen:
            startTime = math.floor(datetime.timestamp(datetime.now()))

        while hurdleGame and not startScreen:
            currentTime = math.floor(datetime.timestamp(datetime.now()))
            timeDelta = currentTime - startTime
            
            if hurdleCoord[0] == 0:
                hurdleCoord[0] = 2000
                if hurdleType == fallenHurdle:
                    hurdleType = standingHurdle
                    knockedOver += 1
                else:
                    successfulJump += 1

            screen.fill(0)
            screen.blit(runningTrack, (0,0))

            timerText = font.render(str(timeDelta) + ' s', True, (255, 255, 255))
            timerTextRect = timerText.get_rect()
            timerTextRect.center = (50, 50)
            screen.blit(timerText, timerTextRect)

            if counterStarted:
                counter +=1
            
            if counter > 20 and jumperCoord[1] < 275:
                jumperCoord[1] += 1
                counterStarted = False
            
            if counter == 45:
                counter = 0

            if successfulJump + knockedOver == 5 and finishLineCoord[0] > 100:
                finishLineCoord[0]-=5
                jumperCoord[1] = 275
                screen.blit (finishLine, finishLineCoord)
                screen.blit (countries[country], jumperCoord)
                pygame.display.flip()

            elif successfulJump + knockedOver == 5:
                hurdleGame = False
                hurdleResults = True 

            else:
                screen.blit(hurdleType, hurdleCoord)
                hurdleCoord[0] -=5
                screen.blit(countries[country], jumperCoord)
                pygame.display.flip()

                playerRect = pygame.Rect(countries[country].get_rect(topleft=(jumperCoord)))
                hurdleRect = pygame.Rect(standingHurdle.get_rect(topleft=(hurdleCoord)))

                if playerRect.colliderect(hurdleRect):
                    collision = True
                    hurdleType = fallenHurdle

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit() 
                        exit(0)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and jumperCoord[1] > 225:
                            jumperCoord[1] -= 300
                            counterStarted = True

        while hurdleResults:
            screen.blit (finishLine, finishLineCoord)
            screen.blit (countries[country], jumperCoord)

            hurdlesKnocked = font.render("You knocked over "+str(knockedOver)+" hurdles",True,(255,255,255))
            screen.blit(hurdlesKnocked, (600 - hurdlesKnocked.get_width()//2, 50)) 
            hurdlesStanding = font.render("You successfully jumped "+str(successfulJump)+" hurdles",True,(255,255,255))
            screen.blit(hurdlesStanding, (600 - hurdlesStanding.get_width()//2, 150)) 

            score = timeDelta + (1.5 * knockedOver)
            scoreText = font.render("Your time score is "+str(score)+"s",True,(255,255,255))
            screen.blit(scoreText, (900 - hurdlesStanding.get_width()//2, 300))

            if score <= 17:
                screen.blit (gold, (650,350))
            elif score <=20:
                screen.blit (silver, (650,350))
            elif score <=24.5:
                screen.blit (bronze, (650,350))
            else:
                medalText = font.render("Unlucky this time!",True,(255,255,255))
                screen.blit(medalText, (900 - medalText.get_width()//2, 400))
            
            pygame.display.flip()

            time.sleep(8)
            startScreen = True
            hurdleResults = False


        while tableTennisGame and not startScreen:
            screen.fill(0)
            pygame.display.flip()
            exit(0)