import pyautogui
import time

comments = ["Hi","Just commenting for fun","Checking my python comment bot","Just for fun","I am just checking my python skill","python is awesome","I am a messy programmer", "Nera na hoiya jaiben koi!", "python lagay disi", "beshi fast korte partesina", "FB block marbe"]

time.sleep(5)

for i in range(30000):


    pyautogui.typewrite(comments[i%11])
    pyautogui.typewrite("\n")
    time.sleep(2)