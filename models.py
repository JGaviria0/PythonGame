from utilities import *


class Block(pygame.sprite.Sprite):
    def __init__(self,dim,pos,cl):
        pygame.sprite.Sprite.__init__(self)
        self.image = cl
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos,velx,vely, cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5,5])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]       
        self.vely= vely
        self.velx=velx

    def update(self):
        self.rect.y += self.vely
        self.rect.x += self.velx





class Player(pygame.sprite.Sprite):

    def __init__(self,animations,direction,action,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.animations=animations
        self.action=action
        self.actualPositionOfAnimation=0
        self.direction=direction
        self.image = animations[direction][action][0]
        self.rect = pygame.Rect(posX, posY, 40, 50)
        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y, 40, 50)
        self.velx=0
        self.vely=0
        self.puntos=0
        self.salud=100
        self.blocks=[]
    
        

class Player(pygame.sprite.Sprite):

    def __init__(self,animations,direction,action,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.animations=animations
        self.action=action
        self.actualPositionOfAnimation=0
        self.direction=direction
        self.image = animations[direction][action][0]
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(self.rect.x + 20, self.rect.y+13, 30, 45)
        self.velx=0
        self.vely=0
        self.puntos=0
        self.salud=100
        self.blocks=[]
    
        

    def update(self):
        # print (self.hitbox)
        self.image = self.animations[self.direction][self.action][self.actualPositionOfAnimation]
        self.actualPositionOfAnimation+=1
        self.actualPositionOfAnimation= self.actualPositionOfAnimation%len(self.animations[self.direction][self.action])
        
        self.rect.x += self.velx
        self.hitbox = pygame.Rect(self.rect.x+20, self.rect.y+13, 30, 45) 
        if self.hitbox.right > ANCHO:
            print("hola muy buenas")
            self.rect.right = ANCHO
            self.velx=0

        if self.hitbox.left <= 0:
            self.rect.left = 0
            self.velx=0

        # Collider horizontal whit blocks
        ls_col=pygame.sprite.spritecollide(self, self.blocks, False) 
        for b in ls_col:

            if self.velx >0:
                # Derecha
                if self.hitbox.right > b.rect.left and self.hitbox.right < b.rect.right:
                    self.rect.right = b.rect.left
                    self.velx= 0

            else:
                # Izquierda
                if self.hitbox.left-10 < b.rect.right:
                    self.rect.left = b.rect.right - 15
                    self.velx=0


        self.rect.y += self.vely
        self.hitbox = pygame.Rect(self.rect.x + 20, self.rect.y+13, 30, 45) 
        if self.hitbox.bottom >= ALTO:
            self.rect.bottom = ALTO
            self.vely=0

        if self.hitbox.top < 0:
            self.rect.top = 0
            self.vely=0

        # Collider Vertical with blocks
        ls_col=pygame.sprite.spritecollide(self, self.blocks, False) 
        for b in ls_col:

            if self.vely == 0:
                print("Hola")
                continue

            if self.vely > 0:
                # Debajo
                if self.hitbox.bottom > b.rect.top :
                    self.rect.bottom = b.rect.top
                    self.vely=0
                    
            else:
                # Arriba
                if self.hitbox.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom 
                    self.vely=0


        self.hitbox = pygame.Rect(self.rect.x + 20, self.rect.y+13, 30, 45) 


class Enemy(pygame.sprite.Sprite):

    def __init__(self,animations,direction,action,velx,vely,healt,isAttacking,time,posX,posY,name):
        pygame.sprite.Sprite.__init__(self)
        self.animations=animations
        self.action=action
        self.actualPositionOfAnimation=0
        self.direction=direction
        self.image = animations[direction][action][0]
        self.rect = self.image.get_rect()
        self.rect.x=posX
        self.rect.y=posY
        self.velx=velx
        self.vely=vely
        self.healt=healt
        self.isAttacking=isAttacking
        self.time=time
        self.name=name

    def update(self):
        self.image = self.animations[self.direction][self.action][self.actualPositionOfAnimation]
        self.actualPositionOfAnimation+=1
        self.actualPositionOfAnimation= self.actualPositionOfAnimation%len(self.animations[self.direction][self.action])

        if self.time>0:
            self.time-=1
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
