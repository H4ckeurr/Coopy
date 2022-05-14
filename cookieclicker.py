import tkinter as tk 
from random import randint as random
from os import getlogin
from time import time, sleep

gameWindow = tk.Tk()
gameWindow.title("Cookie Clicker")
gameWindow.geometry("1220x720")
gameWindow.resizable(False, False)

startTime = time()

totalCookies = 0
gold = 0
randomAmountOfGold = None
moreGold = None
moreAutoClicker = None
goldUpgradeNumber = 5

goldsForGoldUpgrade = 20
goldsForAutoClicker = 50

autoClickerAmount = 0

def incr(event):
    global totalCookies, gold, goldUpgradeNumber, randomAmountOfGold
    luck = random(0, 100)
    randomAmountOfGold = random(1, goldUpgradeNumber)
    if(luck > 50):
        gold += randomAmountOfGold
    totalCookies += 1
    counterLabel.config(text=f"Cookies mangés : {totalCookies}")
    goldLabel.config(text=f"Or : {gold}")

def upgradeAutoClicker(event):
    global goldUpgradeNumber, moreGold, gold, goldsForAutoClicker, autoClickerAmount
    if(gold >= goldsForAutoClicker):
        gold-=goldsForAutoClicker
        goldsForAutoClicker*=3
        autoClickerAmount+=1
    moreAutoClicker.config(text=f"Autoclickeur demande {goldsForAutoClicker}")
    autoclickerLabel.config(text=f"AutoClickeur : {autoClickerAmount}")

def autoClicker(event):
    global totalCookies, goldUpgradeNumber, moreGold, gold, goldsForAutoClicker, autoClickerAmount, startTime
    if((time() - startTime) > 1):
        startTime = time()
        print(f"{gold}")
        totalCookies += autoClickerAmount
        gold += autoClickerAmount
        counterLabel.config(text=f"Cookies mangés : {totalCookies}")
        goldLabel.config(text=f"Or : {gold}")

def upgradeGold(event):
    global goldUpgradeNumber, moreGold, gold, goldsForGoldUpgrade
    if(gold >= goldsForGoldUpgrade):
        gold-=goldsForGoldUpgrade
        goldUpgradeNumber*=2
        goldsForGoldUpgrade*=3
    moreGold.config(text=f"Plus d'or par clic({goldUpgradeNumber}) demande {goldsForGoldUpgrade}")
    counterLabel.config(text=f"Cookies mangés : {totalCookies}")
    goldLabel.config(text=f"Or : {gold}")

def openShop(event):
    global moreGold, goldsForGoldUpgrade, moreAutoClicker, goldsForAutoClicker

    itemShop = tk.Toplevel()
    itemShop.geometry("300x300")
    itemShop.title("Améliorations")
    itemShop.resizable(False, False)

    moreGold = tk.Button(itemShop, text=f"Plus d'or par clic({goldUpgradeNumber}) demande {goldsForGoldUpgrade}", width=45)
    moreGold.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
    moreGold.bind("<ButtonRelease-1>", upgradeGold)

    moreAutoClicker = tk.Button(itemShop, text=f"Autoclickeur demande {goldsForAutoClicker}", width=45)
    moreAutoClicker.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
    moreAutoClicker.bind("<ButtonRelease-1>", upgradeAutoClicker)


def setCounter(args):
    counterLabel.config(text=f"Cookies mangés : {totalCookies}")

username = tk.Label(gameWindow, text=f"Bienvenue sur Coopy, {getlogin()}! Si vous atteignez 50.000 cookies mangés, envoyez une preuve à H4ckeur#8711 et gagnez une canette de Coca gratuite du Match!!")
username.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

photo = tk.PhotoImage(file="cookie.png")
incrButton = tk.Button(gameWindow, text="Manger un cookie", image=photo, compound=tk.TOP, width=256, height=266)
incrButton.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
incrButton.bind("<ButtonRelease-1>", incr)

shopButton = tk.Button(gameWindow, text="Améliorations", width=25)
shopButton.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)
shopButton.bind("<ButtonRelease-1>", openShop)

counterLabel = tk.Label(gameWindow, text="Cookies mangés : 0")
counterLabel.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

goldLabel = tk.Label(gameWindow, text="Or : 0")
goldLabel.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

autoclickerLabel = tk.Label(gameWindow, text="Autoclickeur : 0")
autoclickerLabel.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

#changed from gameWindow.gameloop to this because allows to make our own game loop
while 1:
    autoClicker(gameWindow)
    gameWindow.update_idletasks()
    gameWindow.update()
    sleep(0.01)
