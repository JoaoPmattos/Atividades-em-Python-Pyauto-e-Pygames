import pygame

# DEFININDO CORES
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()

tela = pygame.display.set_mode((640,480))

pygame.display.set_caption('Game Loop')

# VARIAVEIS DA BOLA

posicao_x=300
posicao_y=200
velocidade_x=1 # ALTERAR VALOR DA VELOCIDADE X
velocidade_y=1 # ALTERAR VALOR DA VELOCIDADE Y

# INICIANDO O LOOP DO JOGO
while True:
    # PROCESSAMENTO DE ENTRADA

    # CAPTURANDO EVENTOS
    # EVENTOS.POLL() CAPTURA UM EVENTO OCORRIDO NA TELA
    event = pygame.event.poll()
    # CASO O EVENTO QUIT (CLICAR NO X DA JANELA)SEJA DISPARADO
    if event.type == pygame.QUIT:
        # SAIA DO LOOP FINALIZANDO O PROGRAMA
        break

    # ATUALIZAÇÃO DO JOGO

    # MOVENDO A BOLA
    posicao_x += velocidade_x
    posicao_y += velocidade_y

    # MUDANDO A DIREÇÃO NO EIXO X NAS BORDAS
    if posicao_x >600:
        velocidade_x= -0.1
    elif posicao_x <0:
        velocidade_x = 0.1
    
    # MUDANDO A DIREÇÃO NO EIXO Y NAS BORDAS
    if posicao_y > 440:
        velocidade_y = -0.1
    elif posicao_y <0:
        velocidade_y = 0.1

    # DESENHO

    # PREENCHENDO O FUNDO COM PRETO
    tela.fill(BLACK)

    # desenhando a bola
    pygame.draw.ellipse(tela,RED,[posicao_x,posicao_y,40,40])

    # ATUALIZANDO A TELA
    pygame.display.flip()