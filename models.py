from utilities import *

class Magic_Book(pygame.sprite.Sprite):
    def __init__(self,pos,animations,description):
        pygame.sprite.Sprite.__init__(self)
        self.animations=animations
        self.actualPositionOfAnimation=0
        self.image = animations[0]
        self.rect = self.image.get_rect()
        self.rect.y=pos[1]
        self.rect.x=pos[0]
        self.description=description
    def update(self):
        self.image = self.animations[self.actualPositionOfAnimation]
        self.actualPositionOfAnimation+=1
        self.actualPositionOfAnimation= self.actualPositionOfAnimation%len(self.animations)




class RigidBody(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 50])
        self.rect = self.image.get_rect()
        self.rect= self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]


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

    def __init__(self,animations,direction,action,posX,posY,healt):
        pygame.sprite.Sprite.__init__(self)
        self.animations=animations
        self.action=action
        self.actualPositionOfAnimation=0
        self.direction=direction
        self.image = animations[direction][action][0]
        self.rect = self.image.get_rect()
        self.rect.y=posY
        self.rect.x=posX
        self.velx=0
        self.vely=0
        self.puntos=0
        self.healt=healt
        self.blocks=[]

        self.rigidBody = RigidBody((posX+20,posY+10))

    def update(self):

        # print(f'({self.rect.x,self.rect.y}),({self.rigidBody.rect.x},{self.rigidBody.rect.y})')
        self.image = self.animations[self.direction][self.action][self.actualPositionOfAnimation]
        self.actualPositionOfAnimation+=1
        self.actualPositionOfAnimation= self.actualPositionOfAnimation%len(self.animations[self.direction][self.action])
        
        self.rect.x += self.velx
        self.rigidBody.rect.x += self.velx #This is new
                
        if self.rigidBody.rect.right > ANCHO: #This is new
            self.rigidBody.rect.right = ANCHO
            self.rect.right = ANCHO+20
            self.velx=0

        if self.rigidBody.rect.left < 1:  #This is new
            self.rigidBody.rect.left = 0
            self.rect.left= -20
            self.velx=0

        ls_col=pygame.sprite.spritecollide(self.rigidBody, self.blocks, False)  # This is new
        for b in ls_col:
            # print('COLISION  HORIZONTAL')
            
            if self.velx == 0:
                continue

            if self.velx >0:
                # Derecha
                if self.rigidBody.rect.right > b.rect.left:
                    self.rigidBody.rect.right = b.rect.left
                    self.rect.right = b.rect.left+20
                    self.velx= 0

            else:
                # Izquierda
                if self.rigidBody.rect.left < b.rect.right:
                    self.rigidBody.rect.left = b.rect.right
                    self.rect.left = b.rect.right-20
                    self.velx=0
        
        self.rigidBody.rect.y+=self.vely 
        self.rect.y += self.vely
        
        if self.rigidBody.rect.bottom > ALTO: 
            self.rigidBody.rect.bottom = ALTO
            self.rect.bottom = ALTO-10
            self.vely=0

        if self.rigidBody.rect.top < 0:
            self.rigidBody.rect.top=0
            self.rect.top = -10
            self.vely=0

        ls_col=pygame.sprite.spritecollide(self.rigidBody, self.blocks, False) 
        for b in ls_col:
            # print('COLISION VERTICAL')
            if self.vely == 0:
                continue

            if self.vely > 0:
                # Debajo
                if self.rigidBody.rect.bottom >= b.rect.top:
                    self.rigidBody.rect.bottom = b.rect.top
                    self.rect.bottom = b.rect.top+10
                    self.vely=0
                    
            else:
                # Arriba
                if self.rigidBody.rect.top <= b.rect.bottom:
                    self.rigidBody.rect.top = b.rect.bottom
                    self.rect.top = b.rect.bottom-10
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
        # if self.rect.right > ANCHO:
        #     self.rect.right = ANCHO
        #     self.velx=0

        # if self.rect.left <= 0:
        #     self.rect.left = 0
        #     self.velx=0

        # self.rect.y += self.vely
        # if self.rect.bottom > ALTO:
        #     self.rect.bottom = ALTO
        #     self.vely=0

        # if self.rect.top < 0:
        #     self.rect.top = 0
        #     self.vely=0
