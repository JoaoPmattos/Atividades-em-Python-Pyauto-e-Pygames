import pygame
import random
from pygame import mixer

# INICIALIZAÇÃO DO PYGAME
pygame.init()

# CONFIGURAÇÃO DA TELA
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela,altura_tela)) 
pygame.display.set_caption('Duck Hunt')

# CORES

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


# CARREGANDO IMAGEM
fundo_ceu = pygame.image.load('pato1/ceu.jpg')
fundo_ceu = pygame.transform.scale(fundo_ceu, (800,600))

mira = pygame.image.load('pato1/mira.png')
mira = pygame.transform.scale(mira,(60,60))

cachorro = pygame.image.load('pato1/cachorro.png')
cachorro = pygame.transform.scale(cachorro,(150,200))

# CARREGANDO IMAGEM DO PATO (ANIMAÇÃO)
imagens_pato = [
    pygame.image.load('pato1/pato1.png'),
    pygame.image.load('pato1/pato2.png'),
    pygame.image.load('pato1/pato3.png')
]
pato_atual = 0

imagens_patoV = [
    pygame.image.load('pato1/patov1.png'),
    pygame.image.load('pato1/patov2.png'),
    pygame.image.load('pato1/patov3.png')
]
# CARREGANDO SOM
som_pato = mixer.Sound('pato1/som_pato.ogg')
som_tiro = mixer.Sound('pato1/tiro.mp3')

# VARIAVEIS DO PATO
pato_x = -110
pato_y = random.randint(0,300)
pato_velocidade = 5
pato_acertado = False

patoV_x = 910
patoV_y = random.randint(0,300)
patoV_velocidade = -10
patoV_acertado = False

# VARIAVEIS DO JOGO
vidasJogador = 3
pontuacao = 0
fonte = pygame.font.Font(None,36)

relogio = pygame.time.Clock()

# CONTADOR DE QUADROS PARA CONTROLAR A VELOCIDADE DA ANIMAÇÃO
contador_quadros = 0
taxa_animacao = 30 # AJUSTA ISSO PARA CONTROLAR A VALOCIDADE DA ANIMAÇÃO

# LOOP PRINCIPAL DO JOGO
jogando = True


while jogando:
    if pato_acertado:
        pato_acertado = False
        
    relogio.tick(60)
    # DESENHAR
    tela.fill(BLACK)
    tela.blit(fundo_ceu,(0,0))
    tela.blit(imagens_pato[pato_atual], (pato_x, pato_y))
    tela.blit(imagens_patoV[pato_atual], (patoV_x,patoV_y))

    # DESENHAR O PATO
    # ATUALIZAR ANIMAÇÃO DO PATO
    # CONTROLE DA VELOCIDADE DA ANIMAÇÃO
    contador_quadros += 1
    if contador_quadros >= taxa_animacao:
        # PATO ATUAL
        pato_atual = (pato_atual + 1) % len(imagens_pato)
        pato_atual = (pato_atual + 1) % len(imagens_patoV)
        contador_quadros = 0
        som_pato.play()
    
    evento = pygame.event.poll()
    if evento.type == pygame.QUIT:
        jogando = False

    if evento.type == pygame.MOUSEBUTTONDOWN:
        mouse_x,mouse_y = pygame.mouse.get_pos()
        # VERIFICA SE O CLIQUE DO MOUSE ACERTOU O PATO.
        # SE O MOUSE ESTÁ DENTRO DA LARGURA DO PATO QUE VAI DE 0 A 110.
        if pato_x<= mouse_x <= pato_x +70 and pato_y <= mouse_y <= pato_y+70:
            pontuacao += 1
            pato_x = largura_tela
            pato_y = random.randint(0,300)
            som_tiro.play()
            pato_acertado = True

        if patoV_x<= mouse_x <= patoV_x +70 and patoV_y <= mouse_y <= patoV_y+70:
            pontuacao += 5
            patoV_x = 0
            patoV_y = random.randint(0,300)
            som_tiro.play()
            patoV_acertado = True

        # O CACHORRO IRÁ APARECER A CADA 5 QUADROS GANHOS E SUMIR LOGO EM SEGUIDA
    if pontuacao % 5 == 0 and pontuacao != 0:
        tela.blit(cachorro,(300,400))

    # MOVIMENTAÇÃO DO PATO
    pato_x += pato_velocidade
    if pato_x >= largura_tela:
        pato_x = -110
        pato_y = random.randint(0,300)
        pato_atual = 0
        if not pato_acertado:  # APLICA PENALIDADE APENAS SE O PATO NÃO FOR ACERTADO
            vidasJogador -=1


    patoV_x += patoV_velocidade
    if patoV_x <= 0:
        patoV_x = largura_tela
        patoV_y = random.randint(0,300)
        pato_atual = 0
    
    if pontuacao < 0:
        pontuacao = 0
    
    if vidasJogador <=0:
        break
    # DESENHAR MIRA NA POSIÇÃO DO MOUSE
    mira_x, mira_y = pygame.mouse.get_pos()
    tela.blit(mira,(mira_x-30,mira_y-30))


    # DESENHAR PONTUAÇÃO
    texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, WHITE)
    tela.blit(texto_pontuacao, (10,10))

    Vida = fonte.render(f'Vidas: {vidasJogador}', True, RED)
    tela.blit(Vida, (690,10))

    # ATUALIZAR TELA
    pygame.display.flip()