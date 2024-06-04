import pyautogui as a

a.hotkey('win','r')
a.write('notepad')
a.press('enter')
a.write('bem vindo ao meu computador')
a.hotkey('ctrl','s')
a.write('joao.txt')
a.press('enter')