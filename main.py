import pygame
import random
import csv
from models import *



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

    # Group Of Players 
    players=pygame.sprite.Group()

    # Group of Enemies
    enemies=pygame.sprite.Group()

    # Group of bullets 
    bullets = pygame.sprite.Group()

    # Group of blocks
    blocks=pygame.sprite.Group()


    player1=Player(character['Principal_Character'],'Down','Idle',50,50)
    players.add(player1)


    enemy1=Enemy(character['Green_Enemy'], 'Right', 'Attack', 0, 0, 10, True,15,50,100,'Green_Enemy')
    enemies.add(enemy1)

    # b1=Block ([50,50], [1400,300])
    # blocks.add(b1)

    blocks = parserColi(0,0)
    player1.blocks= blocks

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
                player1.velx=0
                player1.vely=0

                # Right Direction
                if event.key == pygame.K_d and player1.action!='Attack':
                    if player1.direction!='Right':
                        player1.actualPositionOfAnimation=0
                    
                    player1.direction='Right'
                    player1.action='Walk'
                    player1.velx = 5
                
                 # Left Direction
                if event.key == pygame.K_a and player1.action!='Attack':
                    if player1.direction!='Left':
                        player1.actualPositionOfAnimation=0
                    
                    player1.direction='Left'
                    player1.action='Walk'
                    player1.velx = -5
                
                # Up Direction
                if event.key == pygame.K_w and player1.action!='Attack':
                    if player1.direction!='Up':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Up'
                    player1.action='Walk'
                    player1.vely = -5

                # Down Direction
                if event.key == pygame.K_s and player1.action!='Attack':
                    if player1.direction!='Down':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Down'
                    player1.action='Walk'
                    player1.vely = 5
                
                # Attack
                if event.key == pygame.K_k:
                    player1.action='Attack'
                    player1.actualPositionOfAnimation=0
                    player1.velx=0
                    player1.vely=0


            #Static in a position
            if event.type == pygame.KEYUP:
                if player1.action!='Idle' and player1.action!='Attack':
                    player1.action='Idle'
                    player1.actualPositionOfAnimation=0
                player1.velx=0
                player1.vely=0





        for enemy in enemies:

            # Green Enemy
            if enemy.name=='Green_Enemy':
                if enemy.actualPositionOfAnimation ==10 or enemy.actualPositionOfAnimation==15:
                    enemy.isAttacking=True

                if enemy.isAttacking and enemy.action=='Attack':
                    velxBullet =0
                    velyBullet=0
                    #Right
                    if enemy.direction=="Right":
                        pos=[enemy.rect.x + 50 , enemy.rect.bottom-35]
                        velxBullet=5

                    #Lef
                    if enemy.direction=="Left":
                        pos=[enemy.rect.x  , enemy.rect.bottom-35]
                        velxBullet=-5
                        
                    # Up
                    if enemy.direction=="Up":
                        pos=[enemy.rect.x + 35 , enemy.rect.bottom-50]
                        velyBullet=-5

                    # Down
                    if enemy.direction=="Down":
                        pos=[enemy.rect.x + 35 , enemy.rect.bottom-50]
                        velyBullet=5

                    bullet=Bullet(pos,velxBullet,velyBullet) # WE CAN CONTROL THE DIRECTON WITH THE SECOND PARAMETER
                    bullets.add(bullet)
                    enemy.isAttacking=False

            # Skeleton Enemy
            if enemy.name == "Skeleton_Enemy":
                pass

        # Check movement complete for the atack

        if player1.action!='Idle':
                if player1.action=='Attack':
                    if player1.actualPositionOfAnimation>len(player1.animations[player1.direction]['Attack'])-2:
                        player1.action='Idle'
                        player1.actualPositionOfAnimation=0
   


        # Right
        if player1.rigidBody.rect.right > lim_movDer:
            player1.rigidBody.rect.right = lim_movDer
            player1.rect.right = lim_movDer+20

            if f_posx > lim_ventana:
                f_posx += f_velx

                for b in blocks:
                    b.rect.x += f_velx

        # Left
        if player1.rigidBody.rect.left <= lim_movIzq:
            player1.rigidBody.rect.left = lim_movIzq
            player1.rect.left = lim_movIzq-20

            if f_posx <= 0:
                f_posx -= f_velx

                for b in blocks:
                    b.rect.x -= f_velx

        # Down
        if player1.rigidBody.rect.bottom >= lim_movAba:
            player1.rigidBody.rect.bottom = lim_movAba
            player1.rect.bottom = lim_movAba+10

            if f_posy >= lim_ventanaAlto:
                f_posy += f_vely

                for b in blocks:
                    b.rect.y += f_vely
        # up
        if player1.rigidBody.rect.top < lim_movArr:
            player1.rigidBody.rect.top = lim_movArr
            player1.rect.top=lim_movArr-10

            if f_posy <= 0:
                f_posy -= f_vely

                for b in blocks:
                    b.rect.y -= f_vely
        players.update()
        bullets.update()
        enemies.update()

        pantalla.fill(NEGRO)
        parserMap(f_posx,f_posy)


        for block in blocks:
            pygame.draw.rect(pantalla, AZUL,block.rect,1)
        pygame.draw.rect(pantalla, ROJO,player1.rect,1)
        pygame.draw.rect(pantalla, VERDE,player1.rigidBody.rect,1)
        bullets.draw(pantalla)
        enemies.draw(pantalla)
        players.draw(pantalla)    
        blocks.draw(pantalla) 

        pygame.display.flip()
        reloj.tick(20)

     
    pygame.quit()
            
