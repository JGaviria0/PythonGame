from models import *

def main():
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    players=pygame.sprite.Group()
    # player1=Player(character['Principal_Character'],'Right'dd,'Idle')
    # player1=Player(character['Skeleton_Enemy'],'Right','Idle')
    player1=Player(character['Green_Enemy'],'Right','Idle')

    players.add(player1)
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
                if event.key == pygame.K_d:
                    if player1.direction!='Right' or player1.action=='Attack':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Right'
                    player1.action='Walk'
                    player1.velx = 5
                
                 # Left Direction
                if event.key == pygame.K_a:
                    if player1.direction!='Left' or player1.action=='Attack':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Left'
                    player1.action='Walk'
                    player1.velx = -5
                
                # Up Direction
                if event.key == pygame.K_w:
                    if player1.direction!='Up' or player1.action=='Attack':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Up'
                    player1.action='Walk'
                    player1.vely = -5

                # Down Direction
                if event.key == pygame.K_s:
                    if player1.direction!='Down' or player1.action=='Attack':
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
                

        # Check movement complete for the atack

        if player1.action!='Idle':
                if player1.action=='Attack':
                    if player1.actualPositionOfAnimation>len(player1.animations[player1.direction]['Attack'])-2:
                        player1.action='Idle'
                        player1.actualPositionOfAnimation=0




        pantalla.fill(NEGRO)
        players.update()
        players.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)
        
            
    pygame.quit()






if __name__=='__main__':
    main()