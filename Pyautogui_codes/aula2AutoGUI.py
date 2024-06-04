import pyautogui
import time

# CAPTURA DE DADOS DA TELA
# CAPTURA DA LARGURA E ALTURA DA SUA TELA
telaLarguraX,TelaAlturaY = pyautogui.size()
print(telaLarguraX,TelaAlturaY)

# CAPTURA A POSIÇÃO DO MOUSE
time.sleep(3)
posicao_mouse = pyautogui.position()
print(posicao_mouse)

# VERIICA SE O MOUSE ESTÁ A TELA E RETOMA TRUE OU FALSE
# PARAMETROS (X,Y)
print(pyautogui.onScreen(0,0))

# FAILSAFE SERVE PARA QUE O PROGRAMA PARA QYABDI I NIYSE ESTIVER FORA DA TELA
pyautogui.FAILSAFE = False


# RECURSOS DO MOUSE
# MOVER O MOUSE PARA A POSIÇÃO INDICADA NO PARAMETRO Y E X
# PARAMETROS (X,Y,YEMPO DE ESPERA
pyautogui.moveTo(x=500,y=1000)



# MOVER O MOUSE PARA UMA POSIÇÃO RELATIVA AO MOUSE
# PARAMETROS: (X,Y,TEMPO DE ESPERA)
pyautogui.moveRel(0,TelaAlturaY,0.5)





# CLIQUE DO MOUSE
# PARAMETROS: (X,Y,TEMPO DE ESPERA, BOTÃO DO MOUSE)
# POR PADRÃO ELE IRÁ CLICAR COM O BOTÃO ESQUERDO
pyautogui.click()
# CLIQUE DO MOUSE NA POSIÇÃO INDICADA NO PARAMETRO X E Y
pyautogui.click(100,100,3,button="left")





# CLIQUE DO BOTÃO ESQUERDO DO MOUSE
pyautogui.leftClick()
# CLIQUE DO BOTÃO DIREITO DO MOUSE
pyautogui.rightClick()
# CLIQUE DO BOTÃO DO MEIO DO MOUSE
pyautogui.middleClick()
# CLIQUE DUPLO DO BOTÃO DO MOUSE
pyautogui.doubleClick()
# CLIQUE TRIPLO DO BOTÃO DO MOUSE
pyautogui.tripleClick()




# PRESSIONAR E SOLTAR O BOTÃO DO MOUSE
# PARAMETROS (X,Y,TEMPO DE ESPERA, BOTÃO DO MOUSE)
pyautogui.mouseDown(x=1435,y=18,button="left")
# SOLTA O BOTÃO DO MOUSE
pyautogui.mouseUp()



# ARRASTAR O MOUSE
pyautogui.drag()
# PARAMETROS: (X,Y,TEMPO DE ESPERA)
pyautogui.dragTo(x=1435,y=18)
# ARRASTAR O MOUSE PARA UMA POSIÇÃO RELATIVA AO MOUSE
pyautogui.dragRel(0,TelaAlturaY,0.5)



# SCROLL DO MOUSE
# PARAMETROS: (QUANTIDADE DE SCROLL)
pyautogui.scroll(100)


