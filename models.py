from animations import *
ANCHO=1200
ALTO=600

VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
BLANCO=[255,255,255]
NEGRO=[0,0,0]
AMARILLO=[255, 140, 0]
NARANJA=[255, 69, 0]
PURPURA=[128, 0, 128]
ROSADO=[255, 192, 203]
ANCHO=1200
ALTO=600




class Player(pygame.sprite.Sprite):

    def __init__(self,animations,direction,action):
        pygame.sprite.Sprite.__init__(self)
        self.animations=animations
        self.action=action
        self.actualPositionOfAnimation=0
        self.direction=direction
        self.image = animations[direction][action][0]
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.rect.y=ALTO - 70
        self.velx=0
        self.vely=0
        self.puntos=0
        self.salud=100
        

    def update(self):
        self.image = self.animations[self.direction][self.action][self.actualPositionOfAnimation]
        self.actualPositionOfAnimation+=1
        self.actualPositionOfAnimation= self.actualPositionOfAnimation%len(self.animations[self.direction][self.action])

        self.rect.x += self.velx
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            self.velx=0

        if self.rect.left <= 0:
            self.rect.left = 0
            self.velx=0

        self.rect.y += self.vely
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
            self.vely=0

        if self.rect.top < 0:
            self.rect.top = 0
            self.vely=0