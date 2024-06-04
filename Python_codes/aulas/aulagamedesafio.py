import pygame
# O RANDOM É PARA GERAR NUMEROS ALEATORIOS
import random
import time

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
PURPLE = pygame.Color(128,0,128)

pygame.init()

tela = pygame.display.set_mode((640,480))
pygame.display.set_caption('Desafio')


jogador = pygame.Vector2(200,400)
obstaculo = pygame.Rect(random.randint(80, 450), -50, 50, 50)
obstaculo2 = pygame.Rect(random.randint(80,450), -50, 50, 50)
pontos = 0
velocidade = 0
velocidadey = 0.50
velocidadeInimigos2 = 0.50
color2 = PURPLE

relogio = pygame.time.Clock()

color=WHITE

jogadorimg = pygame.image.load('imgdesafio/carro.png')
jogadorimg = pygame.transform.scale(jogadorimg,(50,50))
    
obstaculoimg = pygame.image.load('imgdesafio/obstaculo.png')
obstaculoimg= pygame.transform.scale(obstaculoimg,(50,50))

obstaculo2img = pygame.image.load('imgdesafio/carropreto.png')
obstaculo2img = pygame.transform.scale(obstaculo2img,(50,50))

fundoimg = pygame.image.load('imgdesafio/estrada.png')
fundoimg = pygame.transform.scale(fundoimg,(640,480))


  # SONS

som = pygame.mixer.Sound('imgdesafio/som.mp3')
som.play(-1)
while True:
    fps = relogio.tick(60)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    keys = pygame.key. get_pressed()
    if keys [pygame.K_a]:
        jogador.x -= 10
    if keys [pygame.K_d]:
        jogador.x +=10
    tela.fill(WHITE)
    tela.blit(fundoimg,(0,0))

    car = pygame.draw.rect(tela,WHITE,[jogador.x,jogador.y,50,60])
    pygame.draw.rect(tela, color2, obstaculo2)   
    pygame.draw.rect(tela,color,obstaculo)

    obstaculo2.move_ip(0, velocidadeInimigos2 * fps)
    obstaculo.move_ip(velocidade*fps, velocidadey*fps)

    tela.blit(fundoimg,(0,0))
   

    fontetexto = pygame.font.SysFont('arial', 30)
    texto =f'PLAYER 1 = {pontos}'
    texto = fontetexto.render(texto,True, YELLOW)
    tela.blit(texto, [0,10])

    if obstaculo2.colliderect(car):
        texto1 = f'Game Over = {pontos}'
        texto1 = fontetexto.render(texto1, True, RED)
        tela.blit(texto1,[230,200])    
        pygame.display.flip()
        time.sleep(2)
        break
    if obstaculo.colliderect(car):
        texto1 = f'GAME OVER = {pontos}'
        texto1 = fontetexto.render(texto1, True, RED)
        tela.blit(texto1, [220, 220])
        pygame.display.flip()
        time.sleep(2)
        break

    if obstaculo.y >480:
        obstaculo.y = -50
        obstaculo.x = random.randint(80,450)
        pontos +=1
    if obstaculo2.y >480:
        obstaculo2.y = -50
        obstaculo2.x = random.randint(80,450)
        pontos +=1
    if jogador.x <0:
        color = WHITE
        carro = pygame.Rect(200,random.randint(80,450),50,50)
        print('NÃO SAIA DA TELA')
    if jogador.x>610:
        color = WHITE
        carro = pygame.Rect(200,random.randint(80,450),50,50)
        print('NÃO SAIA DA TELA')
        
    if jogador.x < 80:
        jogador.x = 80
    if jogador.x >500:
        jogador.x = 500


    tela.blit(jogadorimg,(jogador.x,jogador.y,50,50))

    tela.blit(obstaculoimg,(obstaculo.x, obstaculo.y,50,50))
    tela.blit(obstaculo2img,(obstaculo2.x, obstaculo2.y,50,50))
    pygame.display.flip()

  