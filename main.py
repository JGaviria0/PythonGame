import pygame
import random
import csv
from models import *
from map import *


def getOppositeDirection(enemyDirection,playerDirection):
    if player1.direction=='Right':
        return 'Left'
    if player1.direction=='Left':
        return 'Right'
    if player1.direction=='Up':
        return 'Down'
    if player1.direction=='Down':
        return 'Up'

          
if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.font.init() 
                  
    parserMap(0, 0,pantalla)
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

    # Group of magic books
    books = pygame.sprite.Group()


    player1=Player(character['Principal_Character'],'Down','Idle',50,50,100)
    players.add(player1)


    enemy1=Enemy(character['Green_Enemy'], 'Left', 'Attack', 0, 0, 100, True,15,700,400,'Green_Enemy')
    enemies.add(enemy1)
    
    enemy2=Enemy(character['Skeleton_Enemy'], 'Right', 'Idle', 0, 0, 100, True,15,200,300,'Skeleton_Enemy')
    enemies.add(enemy2)

    enemy3=Enemy(character['Skeleton_Enemy'], 'Right', 'Idle', 0, 0, 100, True,15,60,300,'Skeleton_Enemy')
    enemies.add(enemy3)

    blocks = parserColi(0,0,pantalla)
    player1.blocks= blocks
    

    book = Magic_Book((70,120),character['Magic_Book'],'Hola querido viajero,aqui empieza tu aventura')
    books.add(book)

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
                if event.key == pygame.K_d and player1.action!='Attack'and player1.action!='Death':
                    if player1.direction!='Right':
                        player1.actualPositionOfAnimation=0
                    
                    player1.direction='Right'
                    player1.action='Walk'
                    player1.velx = 5
                
                 # Left Direction
                if event.key == pygame.K_a and player1.action!='Attack'and player1.action!='Death':
                    if player1.direction!='Left':
                        player1.actualPositionOfAnimation=0
                    
                    player1.direction='Left'
                    player1.action='Walk'
                    player1.velx = -5
                
                # Up Direction
                if event.key == pygame.K_w and player1.action!='Attack'and player1.action!='Death':
                    if player1.direction!='Up':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Up'
                    player1.action='Walk'
                    player1.vely = -5

                # Down Direction
                if event.key == pygame.K_s and player1.action!='Attack'and player1.action!='Death':
                    if player1.direction!='Down':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Down'
                    player1.action='Walk'
                    player1.vely = 5
                
                # Attack
                if event.key == pygame.K_k and player1.action!='Attack'and player1.action!='Death':
                    ls_col=pygame.sprite.spritecollide(player1.rigidBody, enemies, False)  # If we attack
                    for enemy in ls_col:
                        enemy.healt-=20
                        enemy.actualPositionOfAnimation=0
                        enemy.action='Hurt'
                        if enemy.healt==0:
                            enemy.action='Death'
                            

                    player1.action='Attack'
                    player1.actualPositionOfAnimation=0
                    player1.velx=0
                    player1.vely=0


            #Static in a position
            if event.type == pygame.KEYUP:
                if player1.action!='Idle' and player1.action!='Attack' and player1.action!='Death':
                    player1.action='Idle'
                    player1.actualPositionOfAnimation=0
                player1.velx=0
                player1.vely=0

        for enemy in enemies:

            # Green Enemy
            if enemy.name=='Green_Enemy' and player1.action!='Death':
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
            if enemy.name == "Skeleton_Enemy" and player1.action!='Death':
                if enemy.rect.colliderect(player1.rigidBody.rect) and enemy.action!='Hurt' and enemy.action!='Death' :
                    enemy.direction = getOppositeDirection(enemy.direction,player1.direction)
                    if enemy.action!='Attack':
                        enemy.actualPositionOfAnimation=0
                    enemy.action='Attack'
                    
                    if player1.action!='Hurt':
                        player1.actualPositionOfAnimation=0
                        player1.action='Hurt'

                    player1.healt-=0.2
                    # print(player1.healt)

                    if player1.healt<=0:
                        player1.action='Death'
                        player1.actualPositionOfAnimation=0
                        enemy.action='Idle'

                elif enemy.action!='Idle' and enemy.action!='Hurt' and enemy.action!='Death':
                    enemy.actualPositionOfAnimation=0
                    enemy.action='Idle'
                    enemy.direction=player1.direction
                    player1.actualPositionOfAnimation=0
            
            if player1.healt<=0:
                enemy.action='Idle'
                enemy.actualPositionOfAnimation=0



        #Check if a bullet shoot me
        ls_col=pygame.sprite.spritecollide(player1.rigidBody, bullets, False)
        for bullet in ls_col:
            # print(player1.healt)
            player1.healt-=5
            if player1.action!='Hurt':
                player1.action='Hurt'
                player1.actualPositionOfAnimation=0
            if player1.healt<=0:
                player1.actualPositionOfAnimation=0
                player1.action='Death'
            bullets.remove(bullet)


        #Check if a bullet is out of screen
        for bullet in bullets.copy():
            if bullet.rect.x>800 or bullet.rect.x<=0 or bullet.rect.y>600 or bullet.rect.y<=0:
                bullets.remove(bullet)      


        # Check movement complete for the atack (Player)

        if player1.action!='Idle':
                if player1.action=='Attack':
                    if player1.actualPositionOfAnimation>len(player1.animations[player1.direction]['Attack'])-2:
                        ls_col=pygame.sprite.spritecollide(player1.rigidBody, enemies, False)  # If we attack
                        for enemy in ls_col:
                            enemy.action='Attack'
                            if enemy.healt==0:
                                enemies.remove(enemy)
                        
                        player1.action='Idle'
                        player1.actualPositionOfAnimation=0

                if player1.action=='Death':
                    if player1.actualPositionOfAnimation==3:
                        players.remove(player1)
                    
   
        # Check if we touch a book 
        ls_col=pygame.sprite.spritecollide(player1.rigidBody, books, False)
        for book in ls_col:
            myfont =pygame.font.Font('./Storytime.ttf',30)
            txt_info=myfont.render(book.description, True , VERDE)
            pantalla.blit(txt_info, (5,5))
            
            




        # Slice on screen 

        # Right
        if player1.rigidBody.rect.right > lim_movDer:
            player1.rigidBody.rect.right = lim_movDer
            player1.rect.right = lim_movDer+20

            if f_posx > lim_ventana:
                f_posx += f_velx

                for b in blocks:
                    b.rect.x += f_velx
                
                for e in enemies:
                    e.rect.x += f_velx

                for book in books:
                    book.rect.x += f_velx

        # Left
        if player1.rigidBody.rect.left < lim_movIzq:
            player1.rigidBody.rect.left = lim_movIzq
            player1.rect.left = lim_movIzq-20

            if f_posx <= 0:
                f_posx -= f_velx

                for b in blocks:
                    b.rect.x -= f_velx
                
                for e in enemies:
                    e.rect.x -= f_velx
                
                for book in books:
                    book.rect.x -= f_velx

        # Down
        if player1.rigidBody.rect.bottom > lim_movAba:
            player1.rigidBody.rect.bottom = lim_movAba
            player1.rect.bottom = lim_movAba+10

            if f_posy >= lim_ventanaAlto:
                f_posy += f_vely

                for b in blocks:
                    b.rect.y += f_vely
                
                for e in enemies:
                    e.rect.y += f_vely
                
                for book in books:
                    book.rect.y+= f_vely
        # up
        if player1.rigidBody.rect.top < lim_movArr:
            player1.rigidBody.rect.top = lim_movArr
            player1.rect.top=lim_movArr-10

            if f_posy <= 0:
                f_posy -= f_vely

                for b in blocks:
                    b.rect.y -= f_vely
                
                for e in enemies:
                    e.rect.y -= f_vely
                
                for book in books:
                    book.rect.y -= f_vely


        pygame.display.flip()

        #Update elements
        players.update()
        bullets.update()
        enemies.update()
        books.update()

        pantalla.fill(NEGRO)
        parserMap(f_posx,f_posy,pantalla)

        # Draw Elements
        bullets.draw(pantalla)
        players.draw(pantalla)
        enemies.draw(pantalla)
        blocks.draw(pantalla) 
        books.draw(pantalla)


        reloj.tick(20)

     
    pygame.quit()
            
