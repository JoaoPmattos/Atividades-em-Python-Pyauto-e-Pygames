import pyautogui
import time

# RECURSOS DO TECLADO
# PRESSIONAR UMA TECLA DO TECLADO
# A LISTA DE TECLAS DISPONIVEIS PODE SER ENCONTRADA NO SITE: https://pyautogui.readthedocs.io/en/latest/keyboard.html
pyautogui.press("enter")


# PRESSIONAR E SOLTAR UMA TECLA DO TECLADO
pyautogui.keyDown("enter")
pyautogui.keyUp("enter")


# ESCREVE UM TEXTO
pyautogui.write('Hello, World!')



# COMBINAÇÃO DE TECLAS

pyautogui.hotkey('ctrl','c') # COPIA TEXTO