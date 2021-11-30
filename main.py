from models import *

def main():
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    players=pygame.sprite.Group()

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
                if event.key == pygame.K_d:
                    if player1.direction!='Right':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Right'
                    player1.action='Walk'
                    player1.velx = 5
                if event.key == pygame.K_a:
                    if player1.direction!='Left':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Left'
                    player1.action='Walk'
                    player1.velx = -5
                if event.key == pygame.K_w:
                    if player1.direction!='Up':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Up'
                    player1.action='Walk'
                    player1.vely = -5
                if event.key == pygame.K_s:
                    if player1.direction!='Down':
                        player1.actualPositionOfAnimation=0
                    player1.direction='Down'
                    player1.action='Walk'
                    player1.vely = 5
            if event.type == pygame.KEYUP:
                if player1.action!='Idle':
                    player1.action='Idle'
                    player1.actualPositionOfAnimation=0
                player1.velx=0
                player1.vely=0
                


        pantalla.fill(NEGRO)
        players.update()
        players.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)
        
            
    pygame.quit()






if __name__=='__main__':
    main()