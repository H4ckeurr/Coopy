#Importing needed stuff
import tkinter as tk
from tkinter import messagebox
from random import randint as random
from os import getlogin
from time import time, sleep

#Main window declaration and configuration
gameWindow = tk.Tk()
gameWindow.title("Coopy Clicker")
gameWindow.geometry("500x430")
gameWindow.resizable(False, False)


startTime = time()

#Declaring main logic variables
mainFrame = tk.Frame(gameWindow, borderwidth=2, relief=tk.GROOVE)
mainFrame.grid(column=1, row=0, sticky=tk.N, padx=5)

itemShop = tk.Frame(gameWindow, borderwidth=2, relief=tk.GROOVE)
itemShop.grid(column=1, row=0, sticky=tk.W, padx=5)
itemShop.grid_remove()

infosFrame = tk.Frame(gameWindow, borderwidth=2, relief=tk.GROOVE)
infosFrame.grid(column=1, row=0, sticky=tk.S, padx=5, pady=30)

settingsFrame = tk.Frame(gameWindow, borderwidth=2, relief=tk.GROOVE)
settingsFrame.grid(column=1, row=0, sticky=tk.S, padx=5, pady=30)
settingsFrame.grid_remove()

cheatLabel = tk.Label(settingsFrame, text=f"Activer code de triche")
cheatLabel.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

cheatCode = tk.StringVar()
cheatEntry = tk.Entry(settingsFrame, textvariable=cheatCode)
cheatEntry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

def activateCheatCode():
    global cheatCode, gold
    if(cheatCode.get() == "iamrich"):
        gold = 1000000
        messagebox.showinfo("Succès", "Code de triche activé")
    else:
        messagebox.showerror("Erreur", "Code inconnu")

cheatButton = tk.Button(settingsFrame, text=f"Activer", command=activateCheatCode)
cheatButton.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)


gold = 0

shopGoldLabel = tk.Label(itemShop, text=f"Or : {gold}")
shopGoldLabel.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

totalCookies = 0
randomAmountOfGold = None
moreGold = None
moreGoldInfoLabel = None
moreAutoclickerInfoLabel = None
moreAutoClicker = None
goldUpgradeNumber = 5

#Declaring upgrade prices variables
goldsForGoldUpgrade = 10
goldsForAutoClicker = 50

autoClickerAmount = 0

"""
Begin side menu
"""
#Declaring variables for side menu
min_w = 35
max_w = 100
cur_width = min_w # Increasing width of the frame
expanded = False

#Expand the side menu, increasing the width by 10 every 5ms, once fully expanded set expanded to true
def expand():
    global cur_width, expanded
    cur_width += 10
    rep = gameWindow.after(5,expand) #Repeat every 5ms
    sideMenu.config(width=cur_width)
    if cur_width >= max_w: 
        expanded = True
        gameWindow.after_cancel(rep) #Stop repeating
        fill()

#Close the side menu, decreasing the width by 10 every 5ms, once fully closed set expanded to false
def contract():
    global cur_width, expanded
    cur_width -= 10
    rep = gameWindow.after(5,contract) #Repeat every 5ms
    sideMenu.config(width=cur_width)
    if cur_width <= min_w:
        expanded = False
        gameWindow.after_cancel(rep) #Stop repeating
        fill()

def fill():
    if expanded:
        # Show a text and remove the image
        homeButton.config(text="Accueil", image="", width = 14)
        shopButton.config(text="Améliorations", image="", width = 14)
        settingsButton.config(text="Paramètres", image="", width = 14)
        username.config(text=f"Coopy Clicker\n\nDéveloppé par\nBrayan\nAlex\nYassine")
        
    else:
        # Bring the image back
        homeButton.config(image=homeImage, width = 25)
        shopButton.config(image=shopImage, width = 25)
        settingsButton.config(image=settingsImage, width = 25)
        username.config(text=f"")
        
# Define the icons to be shown
homeImage = tk.PhotoImage(file="home.png")
shopImage = tk.PhotoImage(file="shop.png")
settingsImage = tk.PhotoImage(file="settings.png")

gameWindow.update() #for the width to get updated
sideMenu = tk.Frame(gameWindow,bg="orange",width=35,height=gameWindow.winfo_height())
sideMenu.grid(column=0, row=0) 

# Bind to the frame, if entered or left
sideMenu.bind('<Enter>',lambda e: expand())
sideMenu.bind('<Leave>',lambda e: contract())

# So that it does not depend on the widgets inside the frame
sideMenu.grid_propagate(False)


"""
End side menu
"""

"""
Depending on if you have enough gold or not the button will change to red or green when hovered, seems to only work on Windows tho so I did not implement it
Also I'm sure there is a better way to do it.
"""
def enterGreen(item):
  item.widget['background'] = "green"

def enterRed(item):
  item.widget['background'] = "red"

#Using #D4D6D6 color code instead of SystemButtonFace as it is Windows only
def leave(item):
  item.widget['background'] = "#D4D6D6"

"""
Using grid_remove() instead of grid_forget() allows us to keep all the settings, so using grid() will show it back without the need of specifying all the options again
"""
def showMainFrame():
    global mainFrame, itemShop, infosFrame, settingsFrame
    mainFrame.grid()
    infosFrame.grid()
    itemShop.grid_remove()
    settingsFrame.grid_remove()

def showShopFrame():
    global mainFrame, infosFrame, settingsFrame, moreGold, itemShop, goldsForGoldUpgrade, moreAutoClicker, goldsForAutoClicker, moreGoldInfoLabel, autoClickerAmount, moreAutoclickerInfoLabel, gold

    mainFrame.grid_remove()
    infosFrame.grid_remove()
    settingsFrame.grid_remove()
    itemShop.grid()

    moreGoldUpgrade = tk.Frame(itemShop, borderwidth=2, relief=tk.GROOVE)
    moreGoldUpgrade.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

    moreAutoclickerUpgrade = tk.Frame(itemShop, borderwidth=2, relief=tk.GROOVE)
    moreAutoclickerUpgrade.grid(column=1, row=1, sticky=tk.E, padx=40, pady=5)

    moreGoldInfoLabel = tk.Label(moreGoldUpgrade, text=f"Augemente l'or par clic\nActuel : {goldUpgradeNumber} or par clic\nCoûte : {goldsForGoldUpgrade} or")
    moreGoldInfoLabel.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
    moreGold = tk.Button(moreGoldUpgrade, text=f"Améliorer", width=15)
    moreGold.grid(column=1, row=1, sticky=tk.S, padx=5, pady=5)
    moreGold.bind("<ButtonRelease-1>", upgradeGold)
    moreGold.bind("<Leave>", leave)

    moreAutoclickerInfoLabel = tk.Label(moreAutoclickerUpgrade, text=f"Un ouvrier qui génère 1 d'or/s\nActuel : {autoClickerAmount} or/s\nCoûte : {goldsForAutoClicker} or")
    moreAutoclickerInfoLabel.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
    moreAutoClicker = tk.Button(moreAutoclickerUpgrade, text=f"Améliorer", width=20)
    moreAutoClicker.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
    moreAutoClicker.bind("<ButtonRelease-1>", upgradeAutoClicker)
    moreAutoClicker.bind("<Leave>", leave)
    

def showSettingsFrame():
    global mainFrame, itemShop, infosFrame, settingsFrame
    settingsFrame.grid()
    mainFrame.grid_remove()
    infosFrame.grid_remove()
    itemShop.grid_remove()

#This is used to add gold, you have 50% chance to get between 1 and the upgrade number(default is 5), if you're unlucky you get 0
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
    global goldUpgradeNumber, moreGold, gold, goldsForAutoClicker, autoClickerAmount, moreAutoclickerInfoLabel
    if(gold >= goldsForAutoClicker):
        gold-=goldsForAutoClicker
        goldsForAutoClicker*=1.15
        goldsForAutoClicker=int(goldsForAutoClicker)
        autoClickerAmount+=1
    moreAutoclickerInfoLabel.config(text=f"Un ouvrier qui génère 1 d'or/s\nActuel : {autoClickerAmount} or/s\nCoûte : {goldsForAutoClicker} or")
    autoclickerLabel.config(text=f"Ouvriers : {autoClickerAmount}")

def autoClicker(event):
    global totalCookies, goldUpgradeNumber, moreGold, gold, goldsForAutoClicker, autoClickerAmount, startTime, shopGoldLabel
    if((time() - startTime) > 1):
        startTime = time()
        print(f"{gold}")
        totalCookies += autoClickerAmount
        gold += autoClickerAmount
        counterLabel.config(text=f"Cookies mangés : {totalCookies}")
        goldLabel.config(text=f"Or : {gold}")
        shopGoldLabel.config(text=f"Or : {gold}")

#This upgrades the max amount of gold that can be generated
def upgradeGold(event):
    global goldUpgradeNumber, moreGold, gold, goldsForGoldUpgrade, moreGoldInfoLabel
    if(gold >= goldsForGoldUpgrade):
        gold-=goldsForGoldUpgrade
        goldUpgradeNumber*=2
        goldsForGoldUpgrade*=2.5
        goldsForGoldUpgrade=int(goldsForGoldUpgrade)
    moreGoldInfoLabel.config(text=f"Augemente l'or par clic\nActuel : {goldUpgradeNumber} or par clic\nCoûte : {goldsForGoldUpgrade} or")
    counterLabel.config(text=f"Cookies mangés : {totalCookies}")
    goldLabel.config(text=f"Or : {gold}")

#This creates the shop window and all its UI
def openShop():
    showShopFrame()


#This updates the cookies counter on the main window
def setCounter(args):
    counterLabel.config(text=f"Cookies mangés : {totalCookies}")

#Theses are all the variables for the main UI
username = tk.Label(sideMenu, text=f"", bg="orange")
username.grid(column=0, row=3, padx=10, pady=200)

photo = tk.PhotoImage(file="cookie.png")

incrButton = tk.Button(mainFrame, image=photo, relief=tk.FLAT, compound=tk.TOP, width=256, height=266)
incrButton.grid(column=1, row=1, sticky=tk.W, padx=15, pady=5)
incrButton.bind("<ButtonRelease-1>", incr)

# Make the buttons with the icons to be shown
homeButton = tk.Button(sideMenu, image=homeImage, bg="orange", relief=tk.FLAT, command=showMainFrame)
homeButton.grid(column=0, row=0, pady=10)

shopButton = tk.Button(sideMenu, image=shopImage, bg="orange", relief=tk.FLAT, command=openShop)
shopButton.grid(column=0, row=1)

settingsButton = tk.Button(sideMenu, image=settingsImage, bg="orange", relief=tk.FLAT, command=showSettingsFrame)
settingsButton.grid(column=0, row=2, pady=10)


counterLabel = tk.Label(infosFrame, text="Cookies mangés : 0")
counterLabel.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

goldLabel = tk.Label(infosFrame, text="Or : 0")
goldLabel.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

autoclickerLabel = tk.Label(infosFrame, text="Ouvriers : 0")
autoclickerLabel.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)


#changed from gameWindow.gameloop to this because allows to make our own game loop
while 1:
    autoClicker(gameWindow)
    gameWindow.update_idletasks()
    gameWindow.update()
    sleep(0.01)
