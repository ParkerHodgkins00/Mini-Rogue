from Player_C import *
from random import Random
import array
import numpy as np


def clearScreen():
    print("\n"*50)


clearScreen()

roomCards = np.array(["Monster", "Treasure", "Merchant", "Resting", "Event", "Trap"])
# armor, hp, gold, food, xp, rank, spell1, spell2, level, room
player = Player_C(1, 5, 10, 6, 0, 1, "", "", 1, 1)

#print(player)
#player.enterRoom("Monster")
while player.getHP() > 0:
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
    print("A choice of rooms")
    print(f"1. {roomCards[1]} 2. {roomCards[2]}")
    inp = input("Your Choice: ")
    if inp == "1":
        player.enterRoom(roomCards[1])
    else:
        player.enterRoom(roomCards[2])
    
    if player.getHP() <= 0:
        break

    clearScreen()

    #Enter Next Room and resolve
    player.enterRoom(roomCards[3])
    if player.getHP() <= 0:
        break

    clearScreen()

    #Reveal next 2 and pick 1
    print(player)
    print("A choice of rooms")
    print(f"1. {roomCards[4]} 2. {roomCards[5]}")
    inp = input("Your Choice: ")
    if inp == "1":
        player.enterRoom(roomCards[4])
    else:
        player.enterRoom(roomCards[5])
    
    if player.getHP() <= 0:
        break

    clearScreen()

    #increase room value
    player.nextRoom()
    print("You've Reached the end of this room. Well done")