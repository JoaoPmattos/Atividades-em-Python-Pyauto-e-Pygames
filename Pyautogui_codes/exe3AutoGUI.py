import pyautogui
import time

pyautogui.press("win")
time.sleep(1)

pyautogui.write('google')
pyautogui.press("enter")

time.sleep(1)
pyautogui.write('youtube.com')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)

time.sleep(3)
pyautogui.click(868,110,3,button='left')

time.sleep(3)
pyautogui.write('deftones change')
pyautogui.press('enter')


time.sleep(3)
pyautogui.click(868,400,3,button='left')

# posicao_mouse = pyautogui.position()
# print(posicao_mouse)


