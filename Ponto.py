#Automatização para bater o ponto
#Importar biblotecas necessarias
import pyautogui
import time
#1 seg de pausa a cada comando
pyautogui.PAUSE = 1
#Abrir site do ponto
pyautogui.press(["Win"])
pyautogui.write("chrome")
pyautogui.press(["enter"])
time.sleep(1)
pyautogui.write("http://meurh.iesb.br:8081/01/#/login")
pyautogui.press(["enter"])
time.sleep(1)
#Colocar login
pyautogui.write("01585241105")
pyautogui.press(["Tab"])
#Colocar senha
pyautogui.write("8501")
time.sleep(1)
pyautogui.press(["enter"])
time.sleep(6)
#Trafegar pelo site e procurar opção "bater ponto"
pyautogui.doubleClick("botao2.PNG")
time.sleep(6)
#Bater o ponto
pyautogui.doubleClick("botaox.PNG")
#pyautogui.dragTo(100,200,2, button="left")