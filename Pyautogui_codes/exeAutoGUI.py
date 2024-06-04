import pyautogui
import time

# CAPTURA A POSIÇÃO DO MOUSE
posicao_mouse = pyautogui.position()
print(posicao_mouse)


pyautogui.FAILSAFE = False


# PRIMEIRO METODO
pyautogui.click(0,1079,3,button="left")
time.sleep(1)
pyautogui.click(22,965,5,button="left")

# SEGUNDO METODO
pyautogui.moveTo(x=0,y=1079)
pyautogui.click()
pyautogui.moveTo(x=22,y=965)
pyautogui.click()
