import pygame
# O RANDOM É PARA GERAR NUMEROS ALEATORIOS
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

pygame.init()

tela = pygame.display.set_mode((640,480))

pygame.display.set_caption('Colisão')

# CRIA O RECT PARA O QUADRADO
 
quadrado = pygame.Rect(300,random.randint(0,460),20,20)
jogador = pygame.Vector2(20,210)
jogador2 = pygame.Vector2(600,210)
jogadorPontos=0
jogador2Pontos=0
velocidade = 0.5
velocidadeY = 0.5

relogio = pygame.time.Clock()

color = WHITE

while True:
    fps = relogio.tick(60)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jogador.y -= 10
    if keys[pygame.K_s]:
        jogador.y += 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        jogador2.y -= 10
    if keys[pygame.K_DOWN]:
        jogador2.y +=10

    tela.fill(BLACK)

    # CRIA O RECT PARA OS PADS
    pa_esquerda = pygame.draw.rect(tela,WHITE,[jogador.x,jogador.y,20,60])
    pa_direita = pygame.draw.rect(tela,WHITE,[jogador2.x,jogador2.y,20,60])

    # DESENHA O QUADRADO USANDO O RECT

    pygame.draw.rect(tela,color,quadrado)

    # USA A FUNÇÃO MOVE_IP PARA MOVER O QUADRADO PELO EIXO X E Y DE ACORDO A VELOCIDADE, O FPS E
    quadrado.move_ip(velocidade * fps, velocidadeY * fps)

    # CHECA POR COLISÃO COM OS PAS
    # O METODO COLLIDERECT() RETORNA TRUE SE HOUVER COLISÃO E FAÇSE SE NAO HOUVER, NESTE ASO A COLIAO E FEIA ENTRE O QUADRADO E AS PAS
    if quadrado.colliderect(pa_esquerda):
        color = RED
        velocidade = -velocidade

    if quadrado.colliderect(pa_direita):
        color = BLUE
        velocidade = -velocidade

    # MOSTRA OS PONTOS NA TABELA
    fonte = pygame.font.SysFont('arial',30)
    texto =f'Jogador 1 = {jogadorPontos} \|/ Jogador 2 = {jogador2Pontos}'
    texto = fonte.render(texto,True, YELLOW)
    tela.blit(texto,[150,10])

    # CASO O QUADRADO SAIA DA TELA
    if quadrado.x <0:
        color = WHITE
        quadrado = pygame.Rect(300,random.randint(0,460),20,20)
        jogador2Pontos +=1
    
    if quadrado.x >640:
        color = WHITE
        quadrado = pygame.Rect(300,random.randint(0,460),20,20)
        jogadorPontos +=1
    
    # CHECA POR COLISÃO NA TELA NA PARTE DE CIMA E DE BAIXO
    if quadrado.y >440:
        velocidadeY = -velocidadeY
    if quadrado.y < 0:
        velocidadeY = -velocidadeY

    if jogador.y<0:
        jogador.y=0
    if jogador.y > 400:
        jogador.y=400
    if jogador2.y<0:
        jogador2.y=0
    if jogador2.y>400:
        jogador2.y=400

    # ATUALIZANDO TELA
    pygame.display.flip()