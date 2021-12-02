from typing import cast
import pygame
import random
import csv

VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
BLANCO=[255,255,255]
NEGRO=[0,0,0]
AMARILLO=[255, 140, 0]
NARANJA=[255, 69, 0]
PURPURA=[128, 0, 128]
ROSADO=[255, 192, 203]
ANCHO=800
ALTO=600

class Jugador(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x=1000
        self.rect.y=ALTO - 300
        self.velx=0
        self.vely=0
        self.bloques=pygame.sprite.Group()
        self.puntos=0
        self.salud=100
        

    def update(self):
        self.rect.x += self.velx
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            self.velx=0

        if self.rect.left <= 0:
            self.rect.left = 0
            self.velx=0

        ls_col=pygame.sprite.spritecollide(self, self.bloques, False) 
        for b in ls_col:
            
            if self.vely == 0:
                continue

            if self.velx >0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    self.velx= 0

            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    self.velx=0
        
        self.rect.y += self.vely
        if self.rect.bottom > ALTO:
            self.rect.top = 0
            self.vely=0

        if self.rect.top < 0:
            self.rect.bottom = ALTO
            self.vely=0

        ls_col=pygame.sprite.spritecollide(self, self.bloques, False) 
        for b in ls_col:

            if self.vely == 0:
                continue

            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.vely=0
                    
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    self.vely=0

class Bloque(pygame.sprite.Sprite):
    def __init__(self,dim,pos,cl):
        pygame.sprite.Sprite.__init__(self)
        self.image = cl
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

def parserMap(initialX, initialY):

    if initialX > 0:
        initialX = 0

    if initialY > 0:
        initialY = 0
    grass = pygame.image.load('img/Grass.png')
    dirtBrown = pygame.image.load('img/Dirt.png')
    stone1 = pygame.image.load('img/Stone1.png')
    stone2 = pygame.image.load('img/Stone2.png')
    plant = pygame.image.load('img/plant.png')
    plant2 = pygame.image.load('img/plant2.png')
    rock1 = pygame.image.load('img/rock.png')
    rock2 = pygame.image.load('img/rock2.png')
    book = pygame.image.load('img/book.png')
    gun = pygame.image.load('img/gun.gif')
    treedown3 = pygame.image.load('img/treedown3.1.png')
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
    treedown3Position = []

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
                    treedown3Position.append([pixelRow, pixelCol])
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
        
        for eachtree in treedown3Position:
            pantalla.blit(treedown3, (eachtree[0], eachtree[1]))

def parserColi(initialX, initialY):

    bloques=pygame.sprite.Group()

    treeH = pygame.image.load('img/Tree.png')
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
                if col == "10": 
                    generator1Position.append([pixelRow, pixelCol])
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

                pixelRow += 10
            pixelCol += 10
            pixelRow = initialX
        
        for eachtree in treesPosition:
            b1 = Bloque ([50,61], eachtree, treeH)
            bloques.add(b1)
        
        for eachtree in treedownPosition:
            aux = treedown
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)
        
        for eachtree in treedown2Position:
            aux = treedown2
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)

        for eachtree in treedown3Position:
            aux = treedown3
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)

        for eachtree in generator1Position:
            b1 = Bloque ([41,55], eachtree, generator1)
            bloques.add(b1)
        
        for eachtree in generator2Position:
            b1 = Bloque ([41,55], eachtree, generator2)
            bloques.add(b1)
        
        for eachtree in wall1Position:
            b1 = Bloque ([30,10], eachtree, wall1)
            bloques.add(b1)
        
        for eachtree in wall2Position:
            b1 = Bloque ([10,30], eachtree, wall2)
            bloques.add(b1)
        
        for eachtree in wall3Position:
            aux = wall3
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)
        
        for eachtree in CastlePosition:
            aux = castle
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, castle)
            bloques.add(b1)

        for eachtree in house1Position:
            aux = house1
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)
        
        for eachtree in house2Position:
            aux = house2
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)
        
        for eachtree in house3Position:
            aux = house3
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)
        
        for eachtree in house4Position:
            aux = house4
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)
        
        for eachtree in house5Position:
            aux = house5
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)
        
        for eachtree in house6Position:
            aux = house6
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)
        
        for eachtree in heapPosition:
            aux = heap
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)
        
        for eachtree in waterPosition:
            aux = water
            tam = [aux.get_height(), aux.get_height()]
            b1 = Bloque (tam, eachtree, aux)
            bloques.add(b1)
        
    
    return bloques
          
if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    parserMap(0, 0)
    lim_ventana=ANCHO - 2400
    lim_ventanaAlto=ALTO - 1800
    lim_movDer =750
    lim_movIzq =50
    lim_movAba = 550
    lim_movArr = 50


    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    j1=Jugador()
    jugadores.add(j1)

    bloques = parserColi(0,0)
    # j1.bloques= bloques

    f_posx= 0
    f_velx= -5
    f_posy= 0
    f_vely= -5

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                j1.velx=0
                j1.vely=0
                if event.key == pygame.K_d:
                    j1.velx = 5
                if event.key == pygame.K_a:
                    j1.velx = -5
                if event.key == pygame.K_w:
                    j1.vely = -5
                if event.key == pygame.K_s:
                    j1.vely= 5
            if event.type == pygame.KEYUP:
                j1.velx=0
                j1.vely=0          

        jugadores.update()

        pantalla.fill(NEGRO)
        parserMap(f_posx,f_posy)

        jugadores.draw(pantalla)    
        bloques.draw(pantalla) 

        pygame.display.flip()
        reloj.tick(40)
        if j1.rect.right > lim_movDer:
            j1.rect.right = lim_movDer

            if f_posx > lim_ventana:
                f_posx += f_velx

                for b in bloques:
                    b.rect.x += f_velx

        if j1.rect.left < lim_movIzq:
            j1.rect.left = lim_movIzq

            if f_posx <= 0:
                f_posx -= f_velx

                for b in bloques:
                    b.rect.x -= f_velx

        if j1.rect.bottom > lim_movAba:
            j1.rect.bottom = lim_movAba

            if f_posy >= lim_ventanaAlto:
                f_posy += f_vely

                for b in bloques:
                    b.rect.y += f_vely

        if j1.rect.top < lim_movArr:
            j1.rect.top = lim_movArr

            if f_posy <= 0:
                f_posy -= f_vely

                for b in bloques:
                    b.rect.y -= f_vely

     
    pygame.quit()
            
