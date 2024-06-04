# IMPORTANDO AS BIBLIOTECAAS
# TIME É UMA BIBLIOTECA PARA CRIAÇÃO DE JOGOS
import time
# PYGAME É UMA BIBLIOTECA PARA CRIAÇÃO DE JOGOS
import pygame
# O COMANDO PYGAME .INIT() INICIALIZA TODOS OS MODULOS QUE NECESSITAM DE INICIALIZAÇÃO DENTRO DO PYGAME.
pygame.init()
# EM PYGAMES.DISPLAY.SET_MODE CRIAMOS UMA SUPERFICIE PARA A NOSSA JANELA DE TAMANHO (640X480)
tela = pygame.display.set_mode((1440,900))

# PYGAME.DISPLAY.SET_CAPTION ONDE ATRIBUIMOS O TEXTO "OLÁ MUNDO " PARA O TITULO DA JANELA
pygame.display.set_caption('Ola Mundo')

# COM A JANELA CRIADA, UTILIZAMOS O COMANDO FILL DA JANELA SCREEN PARA PREENCHE-LA COM A COR PRETA. A COR É PASSADA EM FORMATO DE LISTA DE TRES ELEMEMENTOS QUE CONSISTEM DOS VALORES DO RGB, QUE VARIAM DE 0 A 255. TROQUE OS VALORES DEST LISTA E RODE NOVAMENTE O PROGRAMAR PARA VER QUE A COR DA JANELA MUDAR.
tela.fill([255,25,50])

# QUANDO USAMOS COMANDOS PARA DESENHAR NA TELA, NA VERDADE ESTAMOS DESENHANDO NA SUPERFICIE CRIADA DENTRO DA MEMORIA QUE REPRESENTA UMA PORÇÃO DA NOSSA TELA. PARA COPIAR O CONTEUDO DELA E MOSTRA-LO NA TELA É PRECISO UTILIZAR O FLIP QUE É ANALOGO A VOCE FAZER O DESENHO PARA UMA PESSOA E AO TERMINAR VIRAR (FLIP) A SUPERFICIE EM QUE VOCE ESTAVA DESENHANDO PARA QUE ELA VEJA. O FLIP ATUALIZA A TELA COM O CONTEUDO DESENHADO NA SUPERFICIE SCREEN.

pygame.display.flip()
# PARA FINALIZAR O COMANDO SLEEP DA BIBLIOTECA TIME FAZ O PROGRAMA ESPERAR 5 SEGUNDOS ANTES DE FINALIZAR. CASO CONTRARIO O PROGRAMA FECHARIA ANTES QUE VOCE POSSA VER O RESULTADO.
time.sleep(5)