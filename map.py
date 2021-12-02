import pygame
import random
import csv
from models import *

# Map
grass = pygame.image.load('img/Grass.png')
dirtBrown = pygame.image.load('img/Dirt.png')
water2 = pygame.image.load('img/water2.png')
stone1 = pygame.image.load('img/Stone1.png')
stone2 = pygame.image.load('img/Stone2.png')
plant = pygame.image.load('img/plant.png')
plant2 = pygame.image.load('img/plant2.png')
rock1 = pygame.image.load('img/rock.png')
rock2 = pygame.image.load('img/rock2.png')
book = pygame.image.load('img/book.png')
gun = pygame.image.load('img/gun.gif')
treedown31 = pygame.image.load('img/treedown3.1.png')

# Colin
treeH = pygame.image.load('img/Tree.png')
tree2 = pygame.image.load('img/tree2.png')
treedown = pygame.image.load('img/treedown.png')
treedown2 = pygame.image.load('img/treedown2.png')
treedown3 = pygame.image.load('img/treedown3.png')
generator1 = pygame.image.load('img/Generator1.png')
generator2 = pygame.image.load('img/Generator2.png')
wall1 = pygame.image.load('img/Wall1.png')
wall2 = pygame.image.load('img/Wall2.png')
wall3 = pygame.image.load('img/Wall3.png')
castle = pygame.image.load('img/castle.png')
house1 = pygame.image.load('img/house1.png')
house2 = pygame.image.load('img/house2.png')
house3 = pygame.image.load('img/house3.png')
house4 = pygame.image.load('img/house4.png')
house5 = pygame.image.load('img/house5.png')
house6 = pygame.image.load('img/house6.png')
heap = pygame.image.load('img/heap.png')
water = pygame.image.load('img/water.png')
ship = pygame.image.load('img/ship.png')

def parserMap(initialX, initialY, pantalla):

    if initialX > 0:
        initialX = 0

    if initialY > 0:
        initialY = 0
    pantalla.blit(grass, (0, 0))

    stonePosition = []
    stone2Position = []
    wall1Position = []
    plantPosition = []
    plant2Position = []
    rockPosition = []
    rock2Position = []
    bookPosition = []
    gunPosition = []
    treedown31Position = []
    water2Position = []

    pixelRow = initialX
    pixelCol = initialY

    with open('map/map1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            for col in row:
                pantalla.blit(grass, (pixelRow, pixelCol))
                if col == "2":
                    pantalla.blit(dirtBrown, (pixelRow, pixelCol))
                if col == "3":
                    wall1Position.append([pixelRow, pixelCol])
                if col == "6":
                    plantPosition.append([pixelRow, pixelCol]) 
                if col == "7":
                    plant2Position.append([pixelRow, pixelCol]) 
                if col == "8":
                    rockPosition.append([pixelRow, pixelCol]) 
                if col == "9":
                    rock2Position.append([pixelRow, pixelCol])
                if col == "11":
                    pantalla.blit(dirtBrown, (pixelRow, pixelCol))
                    bookPosition.append([pixelRow, pixelCol])  
                if col == "12": 
                    stonePosition.append([pixelRow, pixelCol])
                if col == "13": 
                    pantalla.blit(dirtBrown, (pixelRow, pixelCol))
                    gunPosition.append([pixelRow, pixelCol])
                if col == "14": 
                    stone2Position.append([pixelRow, pixelCol])
                if col == "19": 
                    treedown31Position.append([pixelRow, pixelCol])
                if col == "30":
                    water2Position.append([pixelRow, pixelCol])
                pixelRow += 10

            pixelCol += 10
            pixelRow = initialX
        
        for eachtree in stonePosition:
            pantalla.blit(stone1, (eachtree[0], eachtree[1]))

        for eachtree in stone2Position:
            pantalla.blit(stone2, (eachtree[0], eachtree[1]))
        
        for eachtree in plantPosition:
            pantalla.blit(plant, (eachtree[0], eachtree[1]))

        for eachtree in plant2Position:
            pantalla.blit(plant2, (eachtree[0], eachtree[1]))
        
        for eachtree in rockPosition:
            pantalla.blit(rock1, (eachtree[0], eachtree[1]))
        
        for eachtree in rock2Position:
            pantalla.blit(rock2, (eachtree[0], eachtree[1]))
        
        for eachtree in bookPosition:
            pantalla.blit(book, (eachtree[0], eachtree[1]))
        
        for eachtree in gunPosition:
            pantalla.blit(gun, (eachtree[0], eachtree[1]))
        
        for eachtree in treedown31Position:
            pantalla.blit(treedown31, (eachtree[0], eachtree[1]))
        
        for eachtree in water2Position:
            pantalla.blit(water2, (eachtree[0], eachtree[1]))

def parserColi(initialX, initialY, pantalla):

    Blocks=pygame.sprite.Group()

    treesPosition = []
    treedownPosition = []
    treedown2Position = []
    treedown3Position = []
    generator1Position = []
    generator2Position = []
    wall1Position = []
    wall2Position = []
    wall3Position = []
    CastlePosition = []
    house1Position = []
    house2Position = []
    house3Position = []
    house4Position = []
    house5Position = []
    house6Position = []
    heapPosition = []
    waterPosition = []
    shipPosition = []
    tree2Position = []

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
                if col == "5":
                    wall2Position.append([pixelRow, pixelCol])
                # if col == "10": 
                #     generator1Position.append([pixelRow, pixelCol])
                if col == "15": 
                    generator2Position.append([pixelRow, pixelCol])
                if col == "16": 
                    treedownPosition.append([pixelRow, pixelCol])
                if col == "17": 
                    treedown2Position.append([pixelRow, pixelCol])
                if col == "18": 
                    treedown3Position.append([pixelRow, pixelCol])
                if col == "20": 
                    CastlePosition.append([pixelRow, pixelCol])
                if col == "21":
                    house1Position.append([pixelRow, pixelCol])
                if col == "22":
                    house2Position.append([pixelRow, pixelCol])
                if col == "23":
                    house3Position.append([pixelRow, pixelCol])
                if col == "24":
                    house4Position.append([pixelRow, pixelCol])
                if col == "25":
                    house5Position.append([pixelRow, pixelCol])
                if col == "26":
                    house6Position.append([pixelRow, pixelCol])
                if col == "27":
                    wall3Position.append([pixelRow, pixelCol])
                if col == "28":
                    heapPosition.append([pixelRow, pixelCol])
                if col == "29":
                    waterPosition.append([pixelRow, pixelCol])
                    
                if col == "31":
                    shipPosition.append([pixelRow, pixelCol])
                if col == "32":
                    tree2Position.append([pixelRow, pixelCol])

                pixelRow += 10
            pixelCol += 10
            pixelRow = initialX
        
        for eachtree in treesPosition:
            b1 = Block ([50,61], eachtree, treeH)
            Blocks.add(b1)
        
        for eachtree in treedownPosition:
            aux = treedown
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in treedown2Position:
            aux = treedown2
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)

        for eachtree in treedown3Position:
            aux = treedown3
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)

        for eachtree in generator1Position:
            b1 = Block ([41,55], eachtree, generator1)
            Blocks.add(b1)
        
        for eachtree in generator2Position:
            b1 = Block ([41,55], eachtree, generator2)
            Blocks.add(b1)
        
        for eachtree in wall1Position:
            b1 = Block ([30,10], eachtree, wall1)
            Blocks.add(b1)
        
        for eachtree in wall2Position:
            b1 = Block ([10,30], eachtree, wall2)
            Blocks.add(b1)
        
        for eachtree in wall3Position:
            aux = wall3
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in CastlePosition:
            aux = castle
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, castle)
            Blocks.add(b1)

        for eachtree in house1Position:
            aux = house1
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in house2Position:
            aux = house2
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in house3Position:
            aux = house3
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in house4Position:
            aux = house4
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in house5Position:
            aux = house5
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in house6Position:
            aux = house6
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in heapPosition:
            aux = heap
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in waterPosition:
            aux = water
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in shipPosition:
            aux = ship
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
        for eachtree in tree2Position:
            aux = tree2
            tam = [aux.get_height(), aux.get_height()]
            b1 = Block (tam, eachtree, aux)
            Blocks.add(b1)
        
    
    return Blocks

def parserSkeletonGenerator(initialX, initialY):

    generatorSkeleton = pygame.sprite.Group()
    generatorGreen= pygame.sprite.Group()

    pixelRow = initialX
    pixelCol = initialY

    with open('map/map1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        cont = 0
        for row in csv_reader:
            for col in row:
                if col == "10":
                    if cont == 0:
                        generator1=Generator([pixelRow, pixelCol], 100, 'img/Generator1.png', [1660, 2140, 110, 43])
                        generatorSkeleton.add(generator1)
                    if cont == 1:
                        generator1=Generator([pixelRow, pixelCol], 100, 'img/Generator1.png', [200, 655, 400, 165])
                        generatorSkeleton.add(generator1)
                    if cont == 2:
                        generator1=Generator([pixelRow, pixelCol], 100, 'img/Generator1.png', [1080, 1500, 400, 70])
                        generatorSkeleton.add(generator1)
                    if cont == 3:
                        generator1=Generator([pixelRow, pixelCol], 100, 'img/Generator1.png', [680, 870, 1150, 700])
                        generatorSkeleton.add(generator1)
                    if cont == 4:
                        generator1=Generator([pixelRow, pixelCol], 100, 'img/Generator1.png', [1240, 1480, 1100, 750])
                        generatorSkeleton.add(generator1)
                    if cont == 5:
                        generator1=Generator([pixelRow, pixelCol], 100, 'img/Generator1.png', [1660, 1970, 1090, 830])
                        generatorSkeleton.add(generator1)
                    if cont == 6:
                        generator1=Generator([pixelRow, pixelCol], 100, 'img/Generator1.png', [840, 1140, 1660, 1510])
                        generatorSkeleton.add(generator1)
                    if cont == 7:
                        print(pixelRow, pixelCol)
                        generator1=Generator([pixelRow, pixelCol], 100, 'img/Generator1.png', [1140, 1480, 1660, 1510])
                        generatorSkeleton.add(generator1)
                    if cont == 8:
                        print(pixelRow, pixelCol)
                        generator1=Generator([pixelRow, pixelCol], 100, 'img/Generator1.png', [1720, 2030, 1630, 1530])
                        generatorSkeleton.add(generator1)
                    
                    cont += 1

                pixelRow += 10
            pixelCol += 10
            pixelRow = initialX

    return generatorSkeleton