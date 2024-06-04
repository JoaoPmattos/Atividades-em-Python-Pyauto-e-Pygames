import pygame
# IMPORTA A BIBLIOTECA MATH, QUE CONTEM FUNÇÕES MATEMATICAS
import math
import random
# O MIXER PERMITE CARREGAR E EXECUTAR MUSICAS E SONS
from pygame import mixer

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

tela = pygame.display.set_mode((800,600))
# CARREGA A IMAGEM DE FUNDO DO JOGO
fundo = pygame.image.load('ufo/fundo.png')
fundo = pygame.transform.scale(fundo,(800,600))

# CARREGA A MUSICA DE FUNDO DO JOGO
mixer.music.load('ufo/fundo.wav')
# DEFINE O VOLUME DA MUSICA
mixer.music.set_volume(0.5)
# DA PLAY NA MUSICA
# -1 INDICA QUE A MUSICA VAI SER REPETIDA INFINITAMENTE
mixer.music.play(-1)

pygame.display.set_caption('Invasores Espaciais')
# CARREGA UMA IMAGEM E DEFINE O ICONE DO JOGO
icone = pygame.image.load('ufo/ufo.png')
pygame.display.set_icon(icone)

# DEFINIÇÕES DO JOGADOR
jogadorImg = pygame.image.load('ufo/nave.png')
jogadorX= 370
jogadorY = 480
jogadorX_movimento = 0

# DEFINIÇÃO DOS INIMIGOS
inimigoImg =[]
inimigoX = []
inimigoY = []
inimigoX_movimento = []
inimigoY_movimento = []
num_inimigos = 6

for i in range(num_inimigos):
    inimigoImg.append(pygame.image.load('ufo/inimigo.png'))
    inimigoX.append(random.randint(0,736))
    inimigoY.append(random.randint(50,150))
    inimigoX_movimento.append(4)
    inimigoY_movimento.append(40)

# DEFINIÇÕES DO TIRO
tiroImg = pygame.image.load('ufo/tiro.png')
tiroX = 0
tiroY = 480
tiroX_movimento = 0
tiroY_movimento = 20
tiro_estado = 'pronto'
tiro_som = mixer.Sound('ufo/tiro.wav')

# DEFINIÇÕES DA PONTUAÇÃO
pontos = 0
fonte = pygame.font.Font('freesansbold.ttf',32)
textoX = 10
textoY = 10

# DEFINIÇÕES DA MENSAGEM DE FIM DE JOGO
fonte_fim = pygame.font.Font('freesansbold.ttf',64)

# FUNCIONALIDADE DO JOGO
# FUNCIONALIDADE PARA MOSTRAR OS PONTOS
def mostrar_pontos(x,y):
    texto = fonte.render(f'Pontos: {pontos}', True, WHITE)
    tela.blit(texto,(x,y))
# FUNCIONALIDADE PARA MOSTRAR A MENSAGEM DE FIM DE JOGO
def game_over():
    texto = fonte_fim.render('GAME OVER', True, WHITE)
    tela.blit(texto,(200,250))
# FUNCIONALIDADE PARA MOSTRAR JOGADOR E INIMIGO
def mostrar_jogador(x,y):
    tela.blit(jogadorImg,(x,y))

def mostrar_inimigo(x,y,i):
    tela.blit(inimigoImg[i],(x,y))

# FUNCIONALIDADE PARA MOSTRAR TIRO

def mostrar_tiro(x,y):
    global tiro_estado
    tiro_estado = 'atirando'
    tela.blit(tiroImg,(x+16,y+10))

# FUNCIONALIDADE PARA DETECTAR COLISAO
def colisao(inimigoX, inimigoY,tiroX,tiroY):
    # CALCULCA A DISTANCIA ENTRE O INIMIGO E O TIRO
    # MATH.SQRT = RAIZ QUADRADA
    # MATH.POW = POTENCIA
    # MATH.POW(X,Y) = X ELEVADO A Y
    # ELEVANDO A DISTANCIA AO QUADRADO PARA EVITAR RAIZES NEGATIVAS, POR EXEMPLO SQRT(-16) = 4.0 E SQRT(16)= 4.0
    distancia = math.sqrt(math.pow(inimigoX - tiroX,2)+ (math.pow(inimigoY - tiroY,2)))

    if distancia < 27:
        return True
    else: 
        return False
explosao_som = mixer.Sound('ufo/explosao.wav')
rodando = True

relogio = pygame.time.Clock()

while rodando:

    relogio.tick(60)
    tela.fill(BLACK)
    tela.blit(fundo,(0,0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        rodando = False

# MOVIMENTAÇÃO DO JOGADOR
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogadorX_movimento = -5
    elif teclas[pygame.K_RIGHT]:
        jogadorX_movimento = 5
    else:
        jogadorX_movimento = 0
    # ATIRANDO AO PRESSIONAR ESPAÇO
    if teclas[pygame.K_SPACE]:
        if tiro_estado == 'pronto':
            # PEGA A POSIÇÃO DO JOGADOR
            tiroX = jogadorX
            mostrar_tiro(tiroX,tiroY)
            tiro_som.play()
    jogadorX += jogadorX_movimento
    if jogadorX <= 0:
        jogadorX = 0
    elif jogadorX >= 736:
        jogadorX = 736
        
    # MOVIMENTAÇÃO DO INIMIGO
    for i in range (num_inimigos):
        # GAMEOVER
        # CONTROLA O MOVIMENTO DO INIMIGO NO EIXO Y
        if inimigoY[i] > 440:
            for j in range (num_inimigos):
                # SE COLIDIR OS INIMIGOS DESAPARECEM E O JOGO ACABA
                inimigoY[j] = 2000
            game_over()
            break

        inimigoX[i] += inimigoX_movimento[i]
        # CONTROLA O MOVIMENTO DO INIMIGO
        if inimigoX[i] <=0:
            inimigoX_movimento[i] = 6
            inimigoY[i] += inimigoY_movimento[i]
        elif inimigoX[i] >= 736:
            inimigoX_movimento[i]= -6
            inimigoY[i] += inimigoY_movimento[i]
            
        # DETECTA COLISÃO DO TIRO COM O INIMIGO
        colidiu = colisao(inimigoX[i],inimigoY[i], tiroX, tiroY)
        if colidiu:
            explosao_som.play()
            tiroY = 480
            tiro_estado = 'pronto'
            pontos +=1
            inimigoX[i] = random.randint(0,736)
            inimigoY[i] = random.randint(50,150)

        mostrar_inimigo(inimigoX[i], inimigoY[i],i)
    # MOVIMENTAÇÃO DO TIRO
    if tiroY <=0:
        tiroY = 480
        tiro_estado = 'pronto'

    if tiro_estado =='atirando':
        mostrar_tiro(tiroX,tiroY)
        tiroY -= tiroY_movimento
    mostrar_jogador(jogadorX,jogadorY)
    mostrar_pontos(textoX,textoY)

    pygame.display.update()