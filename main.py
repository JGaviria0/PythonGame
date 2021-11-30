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
    
    enemy1=Enemy(character['Skeleton_Enemy'], 'Right', 'Attack', 0, 0, 10, True,15,200,200,'Skeleton_Enemy')
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