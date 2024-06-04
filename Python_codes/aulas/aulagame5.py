import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()

tela = pygame.display.set_mode((640,480))

pygame.display.set_caption('Game Loop')
# DEFININDO O RELEGIO PARA LIMITAR O FPS
relogio=pygame.time.Clock()
# VARIAVEIS DOS JOGADORES
# VECTOR2 E UM MODULO DO PYGAME QUE PERMITE CRIAR VETOROES NO EIXO X E Y
# ELA É FREQUENTEMENTE UTILIZADO PARA REPRESENTAR POSIÇÕES, VELOCIDADE, ACELERAÇÕES E DIREÇÕES EM JOGOS.
jogador_pos = pygame.Vector2(tela.get_width() / 2, tela.get_height() / 2)

jogador2_pos = pygame.Vector2(100,60)

velocidade = 1

# Iniciando o loop de jogo

while True:
# PROCESSAMENTO DE ENTRADA
# LIMITANDO O FPS A 60 POR SEGUNDO
    fps=relogio.tick(60)

    # CAPTURANDO EVENTOS
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # ATUALIZAÇÃO D JOGO
    # MOVENDO A BOLA
    # KEY.GET_PRESSED() CAPTURA AS TECLAS PRESSIONADAS E RETORNA UM ARRAY DE 0 A 1 PARA CADA TECLA
    keys = pygame.key.get_pressed()
    # PYGAME.K É UM DICIONARIO COM TODAS AS TECLAS DO TECLADO
    # DEFININDO O MOVIMENTO DO JOGADOR
    if keys[pygame.K_w]:
        jogador_pos.y -= velocidade * fps
    if keys[pygame.K_s]:
        jogador_pos.y += velocidade * fps
    if keys[pygame.K_a]:
        jogador_pos.x -= velocidade * fps
    if keys[pygame.K_d]:
        jogador_pos.x += velocidade * fps

    # DEFININDO O MOVIMENTO DO JOGADOR 2
    if keys[pygame.K_UP]:
        jogador2_pos.y -= 1 * fps
    if keys[pygame.K_DOWN]:
        jogador2_pos.y += 1 * fps
    if keys [pygame.K_LEFT]:
        jogador2_pos.x -= 1 * fps
    if keys[pygame.K_RIGHT]:
        jogador2_pos.x += 1 * fps

    # PREECHENDO O FUNDO
    tela.fill(GREEN)

    # DESENHANDO A BOLA QUE IRÁ REPRESENTAR O JOGADOR
    pygame.draw.ellipse(tela, BLUE, [jogador_pos.x, jogador_pos.y, 40, 40])
    pygame.draw.rect(tela, BLACK, [jogador2_pos.x, jogador2_pos.y,40, 40])

    # ATUALIZANDO A TELA
    pygame.display.flip()