import pygame
import random
import csv
from models import *

def parserMap(initialX, initialY,pantalla):

    if initialX > 0:
        initialX = 0

    if initialY > 0:
        initialY = 0
    grass = pygame.image.load('img/Grass.png')
    dirtBrown = pygame.image.load('img/Dirt.png')
    treeH = pygame.image.load('img/Tree.png')
    stone1 = pygame.image.load('img/Stone1.png')
    stone2 = pygame.image.load('img/Stone2.png')
    generator1 = pygame.image.load('img/Generator1.png')
    generator1 = pygame.image.load('img/Generator1.png')
    wall1 = pygame.image.load('img/Wall1.png')
    castle = pygame.image.load('img/castle.png')
    pantalla.blit(grass, (0, 0))

    treesPosition = []
    stonePosition = []
    stone2Position = []
    generator1Position = []
    wall1Position = []
    CastlePosition = []

    pixelRow = initialX
    pixelCol = initialY

    with open('map/map1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            for col in row:
                if col == "1": 
                    pantalla.blit(grass, (pixelRow, pixelCol))
                if col == "2":
                    pantalla.blit(dirtBrown, (pixelRow, pixelCol))
                if col == "3":
                    wall1Position.append([pixelRow, pixelCol])
                    pantalla.blit(grass, (pixelRow, pixelCol))
                if col == "4": 
                    pantalla.blit(grass, (pixelRow, pixelCol))
                if col == "12": 
                    stonePosition.append([pixelRow, pixelCol])
                    pantalla.blit(grass, (pixelRow, pixelCol))
                if col == "14": 
                    stone2Position.append([pixelRow, pixelCol])
                    pantalla.blit(grass, (pixelRow, pixelCol))
                if col == "10": 
                    pantalla.blit(grass, (pixelRow, pixelCol))
                if col == "20": 
                    pantalla.blit(grass, (pixelRow, pixelCol))

                pixelRow += 10

            pixelCol += 10
            pixelRow = initialX
        
        for eachtree in stonePosition:
            pantalla.blit(stone1, (eachtree[0], eachtree[1]))

        for eachtree in stone2Position:
            pantalla.blit(stone2, (eachtree[0], eachtree[1]))

def parserColi(initialX, initialY,pantalla):

    blocks=pygame.sprite.Group()

    treeH = pygame.image.load('img/Tree.png')
    generator1 = pygame.image.load('img/Generator1.png')
    wall1 = pygame.image.load('img/Wall1.png')
    castle = pygame.image.load('img/castle.png')

    treesPosition = []
    stonePosition = []
    stone2Position = []
    generator1Position = []
    wall1Position = []
    CastlePosition = []

    pixelRow = initialX
    pixelCol = initialY

    with open('map/map1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            for col in row:
                if col == "3":
                    wall1Position.append([pixelRow, pixelCol])
                if col == "4":
                    treesPosition.append([pixelRow, pixelCol])
                if col == "10": 
                    generator1Position.append([pixelRow, pixelCol])
                if col == "20": 
                    CastlePosition.append([pixelRow, pixelCol])

                pixelRow += 10

            pixelCol += 10
            pixelRow = initialX
        
        for eachtree in treesPosition:
            b1 = Block ([50,61], eachtree, treeH)
            blocks.add(b1)

        for eachtree in generator1Position:
            b1 = Block ([41,55], eachtree, generator1)
            blocks.add(b1)
        
        for eachtree in wall1Position:
            b1 = Block ([30,10], eachtree, wall1)
            blocks.add(b1)
        
        for eachtree in CastlePosition:
            pantalla.blit(castle, (eachtree[0], eachtree[1]))  
    
    return blocks