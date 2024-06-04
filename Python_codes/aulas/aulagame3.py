import time
import pygame

# INICIAMOS NOSSO PROGRAMA DEFININDO OS VALORES DE CORES PARA SEREM USADOS;
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()

tela = pygame.display.set_mode((640,480))

# PYGAME.FONT.SYSFONT() É UMA FUNÇÃO QUE PERMITE CRIAR UMA INSTANCIA DE FONTE UTILIZANDO AS FONTES DO SISTEMA. ESTA FUNÇÃO RETORNA UM OJBETO FONT QUE PODE SER USADO PARA RENDERIZAR TEXTO NA TELA.
# O PRIMEIRO RGUMENTO DA FUNÇÃO É O NOME DA FONTE E O SEGUNDO ARGUMENTO E O TAMANHO DA FONTE
font = pygame.font.SysFont('impact',55 )

pygame.display.set_caption('Olá Mundo')

# PREENCHENDO O FUNDO COM PRETO
tela.fill(BLACK)

# PYGAME.DRAW É UMA BIBLIOTECA QUE PERMITE DESENHAR NA TELA.
# LINE() É UMA FUNÇÃO QUE PERMITE DESENHAR UMA LINHA NA TELA. RECEBENDO COMO PARAMETROS A SUPERFICIE SEGUIDA DA COR E OS PONTOS:INICIAL (X1,Y1) E FINAL (X2,Y2). O TERCEIRO ARGUMENTO FA FUNÇÃO DEFINE A ESPESSURA DA LINHA EM PIXELS.
pygame.draw.line(tela,WHITE,[10,100],[630,100],5)

# REACT() É UMA FUNÇÃO QUE PERMITE DESENHAR UM RETANGULO NA TELA, RECEBENDO COMO PARAMETROS A SUPERFICIE SEGUIDA DA COR E UMA LISTA COM A POSIÇÃO INICIAL EM , POSIÇÃO INICIAL EM Y, LARGURA, ALTURA.
pygame.draw.rect(tela,BLUE,[200,210,40,20])

# ELIPSE() É UMA FUNÇÃO QUE PERMITE DESENHAR UM ELIPSE NA TELA, RECEBENDO COMO PARAMETROS A SUPERFICIEI SEGUIDA DA COR E UMA LISTA COM AS COORDENADAS DA ELIPSE(X,Y,LARGURA,ALTURA).
pygame.draw.ellipse(tela,RED,[300,200,40,40])

# POLYGON() É UMA FUNÇÃO QUE PERMITE DESENHAR UM POLIGONO NA TELA, RECEBENDO COMO PARÂMETROS A SUPERFICIE SEGUIDA DA COR E UMA LISTA COM OS PONTOS DO POLIGONO.
pygame.draw.polygon(tela,GREEN,[[420,200],[440,240],[400,240]])

# ATUALIZANDO A TELA
pygame.display.flip()

time.sleep(5)

# PREENCHENDO O FUNDO COM PRETO
tela.fill(BLACK)

# DEFININDO O TEXTO
# FONT.RENDER() RENDERIZA UM TEXTO NA SUPERFICIE. RECEBE COMO PARAMETRO O TEXTO, O VALOR TRUE PARA O ANTIALIASING E A COR.

text = font.render('Joao',True,WHITE)

# COPIANDO O TEXTO PARA A SUPERFICIE
# BLIT() COPIA O CONTEUDO DE UMA SUPERFICIE PARA OUTRA. RECEBE COMO PARAMETROS A SUPERFICIE SEGUIDA DA SUPERFICIE DE DESTINO, EM X E EM Y.
tela.blit(text,[250,200])

# ATUALIZANDO A TELA
pygame.display.flip()

time.sleep(5)

