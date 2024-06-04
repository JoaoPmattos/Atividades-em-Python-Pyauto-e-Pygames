# IMPORTAÇÃO DA BIBLIOTECA
import pyautogui

pyautogui.FAILSAFE = False
# CAPTURA A LARGURA E ALTURA DA SUA TELA
telaLarguraX,TelaAlturaY = pyautogui.size()
# MOVE O MOUSE PARA A POSIÇÃO INDICADA NO PARAMETRO X E Y
pyautogui.moveTo(telaLarguraX,0)

# ACIONA O CLIQUE DO MOUSE
pyautogui.click()