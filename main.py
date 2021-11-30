from models import *
from random import randint

def main():
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    # Group Of Players
    players=pygame.sprite.Group()

    # Group of Enemies
    enemies=pygame.sprite.Group()

    # Group of bullets 
    bullets = pygame.sprite.Group()
    
    player1=Player(character['Principal_Character'],'Right','Idle')
    players.add(player1)
    
    enemy1=Enemy(character['Green_Enemy'], 'Right', 'Attack', 0, 0, 10, True,15)
    enemies.add(enemy1)


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
                
        # Bullets Generation

        for enemy in enemies:
            if enemy.timeBetweenShoot ==0:
                enemy.shooting=True

            if enemy.shooting and enemy.action=='Attack':
                pos=[enemy.rect.x + 25 , enemy.rect.bottom-50]
                bullet=Bullet(pos,5,0) # WE CAN CONTROL THE DIRECTON WITH THE SECOND PARAMETER
                bullets.add(bullet)
                enemy.shooting=False
                enemy.timeBetweenShoot=19 #WE CAN CONTROL THIS



        # Check movement complete for the atack

        if player1.action!='Idle':
                if player1.action=='Attack':
                    if player1.actualPositionOfAnimation>len(player1.animations[player1.direction]['Attack'])-2:
                        player1.action='Idle'
                        player1.actualPositionOfAnimation=0




        pantalla.fill(NEGRO)

        bullets.update()
        bullets.draw(pantalla)

        enemies.update()
        enemies.draw(pantalla)

        players.update()
        players.draw(pantalla)

        pygame.display.flip()
        reloj.tick(20)
        
            
    pygame.quit()






if __name__=='__main__':
    main()