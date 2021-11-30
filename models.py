from utilities import *
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

class Enemy(pygame.sprite.Sprite):

    def __init__(self,animations,direction,action,velx,vely,healt,shooting,timeBetweenShoot):
        pygame.sprite.Sprite.__init__(self)
        self.animations=animations
        self.action=action
        self.actualPositionOfAnimation=0
        self.direction=direction
        self.image = animations[direction][action][0]
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.rect.y=ALTO - 70
        self.velx=velx
        self.vely=vely
        self.healt=healt
        self.shooting=shooting
        self.timeBetweenShoot=timeBetweenShoot
        

    def update(self):
        self.image = self.animations[self.direction][self.action][self.actualPositionOfAnimation]
        self.actualPositionOfAnimation+=1
        self.actualPositionOfAnimation= self.actualPositionOfAnimation%len(self.animations[self.direction][self.action])

        if self.timeBetweenShoot>0:
            self.timeBetweenShoot-=1
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
