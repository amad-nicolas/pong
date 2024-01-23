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
inimigo=pygame.Rect((lar-15,alt/2-70),(10,140))

#variáveis de controle
vx_bola=7
vy_bola=7
v_jogador=7
v_inimigo=5

def animacaoBola():
    global vx_bola,vy_bola
    
    bola.x+=vx_bola
    bola.y+=vy_bola   
    
    if bola.left<=0 or bola.right>=lar:
        vx_bola*=-1
    if bola.top<=0 or bola.bottom>=alt:
        vy_bola*=-1
        
    if bola.colliderect(jogador)or bola.colliderect(inimigo):
        vx_bola*=-1
  
def animacaoJogador():
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        jogador.y-=v_jogador 
    if keys[pygame.K_DOWN]:
        jogador.y+=v_jogador
        
    if jogador.top<=0:
        jogador.top=0
    if jogador.bottom>=alt:
        jogador.bottom=alt
        
def animacaoInimigo():
    
    if inimigo.centery < bola.centery:
        inimigo.y += v_inimigo
    elif inimigo.centery > bola.centery:
        inimigo.y -= v_inimigo

    if inimigo.top <= 0:
        inimigo.top = 0
    if inimigo.bottom >= alt:
        inimigo.bottom = alt
             
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
    pygame.draw.rect(tela,cor_objetos,inimigo)
    pygame.draw.aaline(tela, cor_objetos, (lar/2, 0),(lar/2, alt))
    
    #animações
    animacaoBola()
    animacaoJogador()
    animacaoInimigo()
                             
    #Atualização da tela
    pygame.display.flip()
    
    #Controle de FPS
    clock.tick(60)