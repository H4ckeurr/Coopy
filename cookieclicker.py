import tkinter as tk 
from random import randint as random
from os import getlogin

gameWindow = tk.Tk()
gameWindow.title("Cookie Clicker")
gameWindow.geometry("1220x720")
gameWindow.resizable(False, False)

totalCookies = 0
gold = 0
randomAmountOfGold = None
moreGold = None
goldUpgradeNumber = 5

goldsForGoldUpgrade = 20

def incr(event):
    global totalCookies, gold, goldUpgradeNumber, randomAmountOfGold
    luck = random(0, 100)
    randomAmountOfGold = random(1, goldUpgradeNumber)
    if(luck > 50):
        gold += randomAmountOfGold
    totalCookies += 1
    counterLabel.config(text=f"Cookies mangés : {totalCookies}")
    goldLabel.config(text=f"Or : {gold}")



def upgradeGold(event):
    global goldUpgradeNumber, moreGold, gold, goldsForGoldUpgrade
    if(gold >= goldsForGoldUpgrade):
        gold-=goldsForGoldUpgrade
        goldUpgradeNumber*=2
        goldsForGoldUpgrade*=3
    moreGold.config(text=f"Plus d'or par clic({goldUpgradeNumber}) demande {goldsForGoldUpgrade}")

def openShop(event):
    global moreGold, goldsForGoldUpgrade

    itemShop = tk.Toplevel()
    itemShop.geometry("300x300")
    itemShop.title("Améliorations")
    itemShop.resizable(False, False)

    moreGold = tk.Button(itemShop, text=f"Plus d'or par clic({goldUpgradeNumber}) demande {goldsForGoldUpgrade}", width=45)
    moreGold.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
    moreGold.bind("<ButtonRelease-1>", upgradeGold)


def setCounter(args):
    counterLabel.config(text=f"Cookies mangés : {totalCookies}")

username = tk.Label(gameWindow, text=f"Bienvenue sur Coopy, {getlogin()}! Si vous atteignez 50.000 cookies mangés, envoyez une preuve à H4ckeur#8711 et gagnez une canette de Coca gratuite du Match!!")
username.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

photo = tk.PhotoImage(file="cookie.png")
incrButton = tk.Button(gameWindow, text="Manger un cookie", image=photo, compound=tk.TOP, width=250, height=250)
incrButton.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
incrButton.bind("<ButtonRelease-1>", incr)

shopButton = tk.Button(gameWindow, text="Améliorations", width=25)
shopButton.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
shopButton.bind("<ButtonRelease-1>", openShop)

counterLabel = tk.Label(gameWindow, text="Cookies mangés : 0")
counterLabel.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

goldLabel = tk.Label(gameWindow, text="Or : 0")
goldLabel.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)



gameWindow.mainloop()
