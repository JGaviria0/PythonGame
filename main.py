from typing import DefaultDict
import pygame
import csv

ANCHO = 800
ALTO = 600

def parser():

    pixelRow = 0
    pixelCol = 0
    grass = pygame.image.load('img/Grass.png')
    dirtBrown = pygame.image.load('img/Dirt.png')
    treeH = pygame.image.load('img/Arbol.png')
    stone1 = pygame.image.load('img/Stone1.png')
    stone2 = pygame.image.load('img/Stone2.png')
    generator1 = pygame.image.load('img/Generator1.png')

    treesPosition = []
    stonePosition = []
    stone2Position = []
    generator1Position = []

    

    with open('Mapa/map1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            for col in row:
                if col == "1": 
                    pantalla.blit(grass, (pixelRow, pixelCol))
                if col == "2":
                    pantalla.blit(dirtBrown, (pixelRow, pixelCol))
                if col == "4":
                    pantalla.blit(grass, (pixelRow, pixelCol))
                    treesPosition.append([pixelRow, pixelCol])
                if col == "12": 
                    stonePosition.append([pixelRow, pixelCol])
                    pantalla.blit(grass, (pixelRow, pixelCol))
                if col == "14": 
                    stone2Position.append([pixelRow, pixelCol])
                    pantalla.blit(grass, (pixelRow, pixelCol))

                if col == "10": 
                    generator1Position.append([pixelRow, pixelCol])
                    pantalla.blit(grass, (pixelRow, pixelCol))

                pixelRow += 10

            pixelCol += 10
            pixelRow = 0
        
        for eachtree in treesPosition:
            pantalla.blit(treeH, (eachtree[0], eachtree[1]))
        
        for eachtree in stonePosition:
            pantalla.blit(stone1, (eachtree[0], eachtree[1]))

        for eachtree in stone2Position:
            pantalla.blit(stone2, (eachtree[0], eachtree[1]))
        
        for eachtree in generator1Position:
            pantalla.blit(generator1, (eachtree[0], eachtree[1]))
                    


                
if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    parser()
    fin = False
    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
                          
        grass = pygame.image.load('img/Grass.png')
        pantalla.blit(grass, (100, 100))
        
        
        pygame.display.flip()
        
            
    pygame.quit()
