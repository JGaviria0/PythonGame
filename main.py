import pygame
import random
import csv

from pygame import time
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

    # pygame.mixer.init()
    # sonido_fondo = pygame.mixer.Sound("sounds/End.wav")
    # pygame.mixer.Sound.play(sonido_fondo)
   

    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pygame.font.init() 
                  
    parserMap(0, 0,pantalla)
    lim_ventana=ANCHO - 2400
    lim_ventanaAlto=ALTO - 1800
    lim_movDer =750
    lim_movIzq =50
    lim_movAba = 550
    lim_movArr = 50

    # Healt Icon
    healtIcon=pygame.image.load('./icon/heart.png')

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

    # Group of Knife
    knifes = pygame.sprite.Group()

    # Group of beers
    beers = pygame.sprite.Group()

    # Group of hearts
    hearts = pygame.sprite.Group()

    #Group of water
    waters = pygame.sprite.Group()

    # Group of flag
    flags = pygame.sprite.Group()
    flag1= Flag([2100,1600], './icon/flag.png')
    flags.add(flag1)

    water1 = Water((290,1390), character['Water'])
    waters.add(water1)
    water2 = Water((390, 1390), character['Water'])
    waters.add(water2)
    water3 = Water((490,1390), character['Water'])
    waters.add(water3)
    water4 = Water((590,1390), character['Water'])
    waters.add(water4)
    water4 = Water((690,1390), character['Water'])
    waters.add(water4)
    






    generatorSkeleton = pygame.sprite.Group()
    generatorSkeleton = parserSkeletonGenerator(0,0)
    generatorGreen = pygame.sprite.Group()


    player1=Player(character['Principal_Character'],'Down','Idle',50,50,100,20,100)
    players.add(player1)
    blocks = parserColi(0,0,pantalla)
    player1.blocks= blocks

    book = Magic_Book((70,120),character['Magic_Book'],'Hola querido viajero,aqui empieza tu aventura')
    books.add(book)

    book2 = Magic_Book((600,150),character['Magic_Book'],'Debes destruir todas las casas de color negro y los enemigos!')
    books.add(book2)
    

    positions = [ [1660,100], [1800,790], [1100, 810], [1200, 100], [680, 1110], [250, 1530], [1270,1440]]

    # Beer

    for i in range(1):
        position = random.choice(positions)
        positions.remove(position)
        beer1= Beer(position, character['Beer'])
        beers.add(beer1)
        book2 = Magic_Book([position[0] + 30, position[1]],character['Magic_Book'],'La cerveza te da alaaaaas.')
        books.add(book2)

    # potion
    for i in range(2):
        position = random.choice(positions)
        positions.remove(position)
        knife1=Knife(position, character['Knife'])
        knifes.add(knife1)
        book2 = Magic_Book([position[0] + 30, position[1]],character['Magic_Book'],'Las espadas te dan mas poder.')
        books.add(book2)

    for i in range(3):
        position = random.choice(positions)
        positions.remove(position)
        heart1= Heart(position, './heart/potion.png')
        hearts.add(heart1)
        book2 = Magic_Book([position[0] + 20, position[1]],character['Magic_Book'],'Las posiones te dan salud.')
        books.add(book2)

    f_posx= 0
    f_velx= -5
    f_posy= 0
    f_vely= -5

    reloj=pygame.time.Clock()
    seconds = 0
    fin=False
    gameOver=False
    while not fin and not gameOver:
        seconds += reloj.get_time()
        f_velx = -player1.baseVel
        f_vely = -player1.baseVel
        
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
                    player1.velx = player1.baseVel
                
                 # Left Direction
                if event.key == pygame.K_a and player1.action!='Attack'and player1.action!='Death':
                    if player1.direction!='Left':
                        player1.actualPositionOfAnimation=0
                    
                    player1.direction='Left'
                    player1.action='Walk'
                    player1.velx = -player1.baseVel
                
                # Up Direction
                if event.key == pygame.K_w and player1.action!='Attack'and player1.action!='Death':
                    if player1.direction!='Up':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Up'
                    player1.action='Walk'
                    player1.vely = -player1.baseVel

                # Down Direction
                if event.key == pygame.K_s and player1.action!='Attack'and player1.action!='Death':
                    if player1.direction!='Down':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Down'
                    player1.action='Walk'
                    player1.vely = player1.baseVel
                
                # Attack
                if event.key == pygame.K_k and player1.action!='Attack'and player1.action!='Death':
                    ls_col=pygame.sprite.spritecollide(player1.rigidBody, enemies, False)  # If we attack
                    for enemy in ls_col:
                        enemy.healt-=player1.damage
                        enemy.actualPositionOfAnimation=0
                        enemy.action='Hurt'
                        if enemy.healt<=0:
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
                if enemy.rect.colliderect(player1.rigidBody.rect) and enemy.action!='Hurt' and enemy.action!='Death' and enemy.action!='Attack':
                    enemy.action='Attack'
                    enemy.actualPositionOfAnimation=0
                    enemy.velx=0
                    enemy.vely=0
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

                    if player1.action!='Death':
                        player1.healt-=0.2
               

                    if player1.healt<=0:
                        player1.healt=0
                        player1.action='Death'
                        player1.actualPositionOfAnimation=0
                        enemy.action='Idle'

                elif enemy.action!='Idle' and enemy.action!='Hurt' and enemy.action!='Death' and enemy.action != "Walk":
                    enemy.actualPositionOfAnimation=0
                    enemy.action='Idle'
                    enemy.direction=player1.direction
                    player1.actualPositionOfAnimation=0
            
            if player1.healt<=0:
                enemy.action='Idle'
                enemy.actualPositionOfAnimation=0


        if seconds >= 10000 and len(enemies) < 40:

            seconds = 0

            for generator in generatorSkeleton:
                # print(generator.path)
                enemyGeneration = random.choice(['Skeleton_Enemy', 'Green_Enemy'])
                enemyn=Enemy(character[enemyGeneration], 'Left', 'Walk', -5, 0, 100, True, 15,generator.rect.x,generator.rect.y + 20,enemyGeneration, generator.path.copy())
                enemies.add(enemyn)

            # print("pasaron 10s")

        # check if we are hiting a generator

        ls_col=pygame.sprite.spritecollide(player1.rigidBody, generatorSkeleton, False)
        for generator in ls_col:
            if player1.action == "Attack":
                # print(generator.healt)
                generator.healt -= 3
            
            if generator.healt <=0:
                generatorSkeleton.remove(generator)
            

        #Check if a bullet shoot me
        ls_col=pygame.sprite.spritecollide(player1.rigidBody, bullets, False)
        for bullet in ls_col:
            # print(player1.healt)
            if player1.action!='Death':
                player1.healt-=5
            if player1.action!='Hurt':
                player1.action='Hurt'
                player1.actualPositionOfAnimation=0
            if player1.healt<=0:
                player1.healt=0
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
                            if enemy.name =='Green_Enemy':
                                enemy.direction =getOppositeDirection(enemy.direction,player1.direction)
                            if enemy.healt<=0:
                                enemies.remove(enemy)
                        
                        player1.action='Idle'
                        player1.actualPositionOfAnimation=0

                if player1.action=='Death':
                    if player1.actualPositionOfAnimation==3:
                        players.remove(player1)
                    

        # Check if we touch a heart
        ls_col=pygame.sprite.spritecollide(player1.rigidBody, hearts, False)
        for heart in ls_col:
            player1.healt+=10
            if player1.healt>100:
                player1.healt=100
            hearts.remove(heart)

        # Check if we touch a flag
        ls_col=pygame.sprite.spritecollide(player1.rigidBody, flags, False)
        for flag in ls_col:
            if len(generatorSkeleton)==0 and len(enemies)==0:
                texto= "GANASTE, GRAN AVENTURA!"
                gameOver=True
            else:
                myfont =pygame.font.Font('./Storytime.ttf',30)
                txt_info=myfont.render('Primero destruye todas las casas negras y los enemigos', True , VERDE)
                pantalla.blit(txt_info, (5,5))

        # Check if we touch a Beer
        ls_col=pygame.sprite.spritecollide(player1.rigidBody, beers, False)
        for beer in ls_col:
            player1.baseVel+=5
            beers.remove(beer)
   
        #Check if we touch a Knife
        ls_col=pygame.sprite.spritecollide(player1.rigidBody, knifes, False)
        for knife in ls_col:
            player1.damage+=20
            knifes.remove(knife)

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
                    e.limit[0] += f_velx
                    e.limit[1] += f_velx

                for book in books:
                    book.rect.x += f_velx
                
                for bullet in bullets:
                    bullet.rect.x+=f_velx

                for generator in generatorSkeleton:
                    generator.rect.x+=f_velx
                    generator.path[0]+=f_velx
                    generator.path[1]+=f_velx
                
                for knife in knifes:
                    knife.rect.x+=f_velx

                for beer in beers:
                    beer.rect.x+=f_velx

                for heart in hearts:
                    heart.rect.x+=f_velx


                for water in waters:
                    water.rect.x+=f_velx

                for flag in flags:
                    flag.rect.x+=f_velx
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
                    e.limit[0] -= f_velx
                    e.limit[1] -= f_velx
                
                for book in books:
                    book.rect.x -= f_velx

                for bullet in bullets:
                    bullet.rect.x-=f_velx
                
                for generator in generatorSkeleton:
                    generator.rect.x-=f_velx
                    generator.path[0]-=f_velx
                    generator.path[1]-=f_velx
                for knife in knifes:
                    knife.rect.x-=f_velx

                for beer in beers:
                    beer.rect.x-=f_velx
                for heart in hearts:
                    heart.rect.x-=f_velx
                
                for water in waters:
                    water.rect.x-=f_velx
                
                for flag in flags:
                    flag.rect.x-=f_velx

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
                    e.limit[2] += f_vely
                    e.limit[3] += f_vely
                
                for book in books:
                    book.rect.y+= f_vely

                for bullet in bullets:
                    bullet.rect.y+=f_vely
                
                for generator in generatorSkeleton:
                    generator.rect.y+=f_vely
                    generator.path[2]+=f_vely
                    generator.path[3]+=f_vely

                for knife in knifes:
                    knife.rect.y+=f_vely
                for beer in beers:
                    beer.rect.y+=f_vely
                
                for heart in hearts:
                    heart.rect.y+=f_vely
                
                for water in waters:
                    water.rect.y+=f_vely
                
                for flag in flags:
                    flag.rect.y+=f_vely
        
        
        
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
                    e.limit[2] -= f_vely
                    e.limit[3] -= f_vely
                
                for book in books:
                    book.rect.y -= f_vely
                
                
                for bullet in bullets:
                    bullet.rect.y-=f_vely

                for generator in generatorSkeleton:
                    generator.rect.y-=f_vely
                    generator.path[2]-=f_vely
                    generator.path[3]-=f_vely
                for knife in knifes:
                    knife.rect.y-=f_vely

                for beer in beers:
                    beer.rect.y-=f_vely

                for heart in hearts:
                    heart.rect.y-=f_vely

                
                for water in waters:
                    water.rect.y-=f_vely

                for flag in flags:
                    flag.rect.y-=f_vely

        pygame.display.flip()

        #Update elements
        beers.update()
        players.update()
        knifes.update()
        bullets.update()
        enemies.update()
        books.update()
        generatorSkeleton.update()
        waters.update()

        pantalla.fill(NEGRO)
        parserMap(f_posx,f_posy,pantalla)

        # Draw Elements
        beers.draw(pantalla)
        bullets.draw(pantalla)
        players.draw(pantalla)
        enemies.draw(pantalla)
        blocks.draw(pantalla) 
        books.draw(pantalla)
        knifes.draw(pantalla)
        generatorSkeleton.draw(pantalla)
        hearts.draw(pantalla)
        waters.draw(pantalla)
        flags.draw(pantalla)

        # Helth Bar
        pantalla.blit(healtIcon, [20,560])
        myfont =pygame.font.Font('./Storytime.ttf',25)
        healt=myfont.render(str(int(player1.healt)), True , BLANCO)
        pantalla.blit(healt, (50,560))
        pygame.draw.rect(pantalla, ROJO, pygame.Rect(20, 550, player1.healt, 10))


        if player1.action=='Death':
            texto='PERDISTE, VUELVE A INTENTARLO'
            gameOver=True

        reloj.tick(20)
    
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        pantalla.fill(NEGRO)
        Fuente =pygame.font.Font('./Storytime.ttf',30)
        img_texto=Fuente.render(texto, True, BLANCO)
        pantalla.blit(img_texto,[200,300])
        pygame.display.flip()
        

     
    pygame.quit()
            
