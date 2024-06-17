from turtle import clear
from Player_C import *
from random import Random
import array
import numpy as np
import time


def clearScreen():
    print("\n"*50)
    
def scrollPrint(s):
    for ch in s:
        time.sleep(0.03)
        print(ch, end='')
        
    print('')
    
def getInput(options):
    inp = input("Your Choice: ")
    if inp in options:
        return inp

    else:
        print("Invalid Option")
        return getInput(options)

clearScreen()

roomCards = np.array(["Monster", "Treasure", "Merchant", "Rest Area", "Random Event", "Trap"])
# armor, hp, gold, food, xp, rank, spell1, spell2, level, room
player = Player_C(1, 5, 3, 6, 0, 1, "", "", 1, 1)
scrollPrint("Welcome to Mini Rogue! What style of play would you like?")
print("                Armor    HP    Gold    Food")
print("1. Casual         1       5      5       6")
print("2. Normal         0       5      3       6")
print("3. Hard           0       4      2       5")
print("4. Impossible     0       3      1       3")
inp = getInput(["1", "2", "3", "4"])
if inp == "1":
    player.setArmor(1)
    player.setHP(5)
    player.setGold(5)
    player.setFood(6)
elif inp == "2":
    player.setArmor(0)
    player.setHP(5)
    player.setGold(3)
    player.setFood(6)
elif inp == "3":
    player.setArmor(0)
    player.setHP(4)
    player.setGold(2)
    player.setFood(5)
elif inp == "4":
    player.setArmor(0)
    player.setHP(3)
    player.setGold(1)
    player.setFood(3)

#scrollPrint(player)
#player.enterRoom("Monster")
while player.getHP() > 0:
    scrollPrint(f"You are now entering area {player.room}")
    input("Press Enter to enter the first room...")
    clearScreen()
    #Phases of Play
    #-------------------#
    #shuffle roomCards
    np.random.shuffle(roomCards)

    #If at end of level, add boss monster
    endOfLevel = False
    endRooms = [2, 4, 7, 10, 14]
    if player.room in endRooms:
        endOfLevel = True

    #Reveal and Resolve First Room
    print(player)
    player.enterRoom(roomCards[0])
    if player.getHP() <= 0:
        break
    clearScreen()

    #Reveal next 2 Cards and pick 1
    print(player)
    scrollPrint("Two Rooms Lie Before You. Which would you like to enter?")
    scrollPrint(f"1. {roomCards[1]} 2. {roomCards[2]}")
    inp = getInput(["1", "2"])
    if inp == "1":
        player.enterRoom(roomCards[1])
    else:
        player.enterRoom(roomCards[2])
    
    if player.getHP() <= 0:
        break
    clearScreen()
    print(player)
    input("Press Enter to Continue To the next Room...")
    clearScreen()

    #Enter Next Room and resolve
    player.enterRoom(roomCards[3])
    if player.getHP() <= 0:
        break

    clearScreen()

    #Reveal next 2 and pick 1
    print(player)
    scrollPrint("Two Rooms Lie Before You. Which would you like to enter?")
    scrollPrint(f"1. {roomCards[4]} 2. {roomCards[5]}")
    inp = getInput(["1", "2"])
    if inp == "1":
        player.enterRoom(roomCards[4])
    else:
        player.enterRoom(roomCards[5])
    
    if player.getHP() <= 0:
        break

    clearScreen()
    print(player)
    #input("Press Enter to Continue To the next Room...")
    clearScreen()

    if endOfLevel:
        scrollPrint("The Guardian of this floor lies ahead. Press Enter to begin the Fight!")
        player.bossRoom = True
        player.enterRoom("Monster")
        
    player.bossRoom = False
    #increase room value
    player.nextRoom()
    if player.getHP() <= 0:
        print("You have failed your quest. Good Bye")
        break
    scrollPrint("You've Reached the end of this Area. Well done")