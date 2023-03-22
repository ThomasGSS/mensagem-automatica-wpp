import pyautogui
import time


# codigo para saber a localização do mouse, isso pode variar de acordo com o monitor
#time.sleep(5)
#print(pyautogui.position())

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(0.6)
pyautogui.write("https://web.whatsapp.com/")
pyautogui.press ("enter")
time.sleep (5.8)
pyautogui.click (x=515, y=165)
pyautogui.write ("NOME DO CONTATO AQUI")
time.sleep(0.3)
pyautogui.click (527, y=297)
pyautogui.write ("SUA MENSAGEM AQUI")
pyautogui.press ("enter")
