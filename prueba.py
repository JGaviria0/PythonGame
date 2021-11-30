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
        self.rect.x=200
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

def parserColi(initialX, initialY):

    bloques=pygame.sprite.Group()

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
            b1 = Bloque ([50,61], eachtree, treeH)
            bloques.add(b1)

        for eachtree in generator1Position:
            b1 = Bloque ([41,55], eachtree, generator1)
            bloques.add(b1)
        
        for eachtree in wall1Position:
            b1 = Bloque ([30,10], eachtree, wall1)
            bloques.add(b1)
        
        for eachtree in CastlePosition:
            pantalla.blit(castle, (eachtree[0], eachtree[1]))  
    
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

    # b1=Bloque ([50,50], [1400,300])
    # bloques.add(b1)

    bloques = parserColi(0,0)
    j1.bloques= bloques

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

        if j1.rect.left <= lim_movIzq:
            j1.rect.left = lim_movIzq

            if f_posx <= 0:
                f_posx -= f_velx

                for b in bloques:
                    b.rect.x -= f_velx

        if j1.rect.bottom >= lim_movAba:
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
            
