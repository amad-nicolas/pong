import pygame,sys

#inicialização básica
pygame.init()
clock=pygame.time.Clock()

#configurando tela
lar=1000
alt=500
cor_fundo=pygame.Color('black')
tela=pygame.display.set_mode((lar,alt))
pygame.display.set_caption('Pong')

#objetos principais do jogo:traves do jogador e inimigo e bola
cor_objetos=pygame.Color('gray')
bola=pygame.Rect((lar/2-10,alt/2-10),(20,20))
jogador=pygame.Rect((5,alt/2-70),(10,140))

#variáveis de controle
vx_bola=7
vy_bola=7
v_jogador=7

#loop principal
while True:
    
    #Captura de eventos
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    #renderização dos objetos
    tela.fill(cor_fundo) 
    pygame.draw.ellipse(tela,cor_objetos,bola)
    pygame.draw.rect(tela,cor_objetos,jogador)
    
    #animações
    bola.x+=vx_bola
    bola.y+=vy_bola
    
    #controle de colisão
    
    #colisões com as bordas
    if bola.left<=0 or bola.right>=lar:
        vx_bola*=-1
    if bola.top<=0 or bola.bottom>=alt:
        vy_bola*=-1
    
    #colisão com jogador e oponente
    if bola.colliderect(jogador):
        vx_bola*=-1      
    
    #movimentação do jogador
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        jogador.y-=v_jogador
        
    if keys[pygame.K_DOWN]:
        jogador.y+=v_jogador
        
    #Atualização da tela
    pygame.display.flip()
    
    #Controle de FPS
    clock.tick(60)