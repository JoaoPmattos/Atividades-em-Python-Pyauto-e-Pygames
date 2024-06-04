import pygame
import random
# INICIALIZAÇÃO DO PYGAME
pygame.init()
# DEFINIÇÃO DE CORES
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

largura_tela = 800
altura_tela= 600
tela = pygame.display.set_mode((largura_tela, altura_tela)) 
pygame.display.set_caption('Evite os Obstáculos!')


# RELOGIO PARA CONTROLE DE FPS
relogio = pygame.time.Clock()
# POSIÇÃO DO JOGADOR
jogador_x = largura_tela //2
jogador_y = altura_tela -20
# VELOCIDADE DO JOGDOR
velocidade_jogador = 0
# LISTA PARA ARMAZENAR OS OBSTÁCULOS
obstaculos = []

# FUNÇÃO PARA DESENHAR O JOGADOR NA TELA

def desenhar_jogador(local,x,y):
    pygame.draw.rect(local,WHITE,(x -25, y -25, 50,50))

# FUNÇÃO PARA DESENHAR S OBSTACULOS NA TELA
def desenhar_obstaculos (local,obstaculos):
    for obstaculo in obstaculos:
        pygame.draw.rect(local,RED,obstaculo)

# LOOP PRINCIPAL DO JOGO
jogando = True

while jogando:
    tela.fill(BLACK)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        jogando = False

    # MOVIMENTO DO JOGADOR COM O MOUSE
    # MOUSE.GET.POS() PEGA A POSIÇÃO DO MOUSE
    posicao_mouse = pygame.mouse.get_pos()
    if jogador_x < posicao_mouse[0]:
        velocidade_jogador = 10
    elif jogador_x > posicao_mouse[0]:
        velocidade_jogador = -10

    jogador_x +=velocidade_jogador

    # LIMITAR O JOGADOR DENTRO DA TELA
    if jogador_x < 25:
        jogador_x = 25
    elif jogador_x > largura_tela - 25:
        jogador_x = largura_tela - 25

    # ADICIONAR NOVO OBSTACULO
    if random.randint(0,100)<2000:
        obstaculo_x = random.randint(0,largura_tela - 30)
        obstaculo_y = -30
        obstaculos.append(pygame.Rect(obstaculo_x,obstaculo_y,30,30))
        
    # MOVIMENTO DOS OBSTACULOS
    for obstaculo in obstaculos:
        obstaculo.y += 5

    # VERIFICAR COLISÃO DO JOGADOR COM OS OBSTACULOS
    for obstaculo in obstaculos:
        if abs(jogador_x - obstaculo.centerx) < 25 and abs (jogador_y- obstaculo.centery)<25:
            jogando = False

    # DESENHAR

    desenhar_jogador(tela,jogador_x,jogador_y)
    desenhar_obstaculos(tela,obstaculos)

    # ATUALIZAR TELA
    pygame.display.flip()

    # LIMITAR FPS
    relogio.tick(60)