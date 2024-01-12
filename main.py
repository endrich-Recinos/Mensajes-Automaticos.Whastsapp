
import pyautogui, webbrowser
from time import sleep
import numero
import mensaje

webbrowser.open('https://web.whatsapp.com/')
sleep(10)

for num in numero.numeros_telefono:
    
    webbrowser.open('https://web.whatsapp.com/send?phone=' + num)
    sleep(25)  
    pyautogui.typewrite(mensaje.texto)
    pyautogui.press('enter')
    sleep(10)  


  