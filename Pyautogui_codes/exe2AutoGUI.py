import pyautogui
import time


pyautogui.hotkey("win","r")
pyautogui.write('notepad')
pyautogui.press("enter")

time.sleep(1)
pyautogui.write('Hello World')
time.sleep(1)

pyautogui.hotkey("ctrl","shift","s")
pyautogui.write("enternotepad2")

pyautogui.press("enter")

pyautogui.click(500,500,3,button="left")
time.sleep(1)
pyautogui.hotkey("alt","f4")