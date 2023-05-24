import pyautogui as auto
import time


#Comando paara visualizar teclado
auto.KEYBOARD_KEYS

#Abrir o google drive no meu computador

#Mostrando mensagem de alerta
auto.alert("O programa vai começar. Não use nada no seu computador enquanto o programa estiver rodando! ")

#Esperando intervalo para ação de cada comando
auto.PAUSE = 1

#Usando as teclas automaticamente
auto.press('win')
auto.write("edge")
time.sleep(0.80)
auto.press('enter')
time.sleep(0.75)
auto.write('https://drive.google.com/drive/my-drive')
auto.press('enter')
time.sleep(2.5)
auto.hotkey('win', 'd')
auto.press('win')
auto.write('excel projetos')
auto.press('enter')
auto.hotkey('win', 'up')
auto.hotkey('win', 'down')
auto.hotkey('win', 'up')



#auto.rightClick




#Usando mouse automaticamente
#auto.moveTo(x=1533, y=192)
#auto.click()
auto.moveTo(x=271, y=220)
auto.mouseDown()
auto.moveTo(x=987, y=870)
auto.hotkey('alt', 'tab')
auto.mouseUp()



time.sleep(3)
auto.alert("Programa finalizado com sucesso!")