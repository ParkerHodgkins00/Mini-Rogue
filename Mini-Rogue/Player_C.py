import random
import time

class Player_C(object):
    def __init__(self, armor, hp, gold, food, xp, rank, spell1, spell2, level, room):
        self.stallTime = 0.5
        self.armor = armor
        self.hp = hp
        self.gold = gold
        self.food = food
        self.xp = xp
        self.rank = rank
        self.spell1 = spell1
        self.spell2 = spell2
        self.level = level
        self.room = room
        self.beatenMonster = False
        self.bossRoom = False
        self.levelToXPBase = {
            1: 1,
            2: 1,
            3: 2,
            4: 2,
            5: 3
        }
        self.levelToDamageBoss = {
            1: 3,
            2: 5,
            3: 7,
            4: 9,
            5: 12
        }
        self.levelToXPBoss = {
            1: 2,
            2: 3,
            3: 4,
            4: 5
        }
        self.levelToCoinBoss = {
            1: 2,
            2: 2,
            3: 3,
            4: 3
        }
        self.roomBelow = {
            1: 3,
            2: 4,
            3: 5,
            4: 6,
            5: 8,
            6: 9,
            7: 10,
            8: 11,
            9: 12,
            10: 13,
            11: 11,
            12: 12,
            13: 13,
            14: 14
        }

    def __str__(self):
        return f"Armor: {self.armor}    HP: {self.hp}   Gold: {self.gold}   Food: {self.food}   XP: {self.xp}   Rank: {self.rank} \n" \
            f"Spell1: {self.spell1} Spell2: {self.spell2} \n" \
            f"Floor: {self.level}   Area: {self.room} \n"

    def scrollPrint(self, s):
        for ch in s:
            time.sleep(0.02)
            print(ch, end='')
            
        print("")
    
    def getInput(self, options):
        inp = input("Your Choice: ")
        if inp in options:
            return inp

        else:
            print("Invalid Option")
            return self.getInput(options)

    def printSelf(self):
        print(f"Armor: {self.armor}    HP: {self.hp}   Gold: {self.gold}   Food: {self.food}   XP: {self.xp}   Rank: {self.rank} \n" \
            f"Spell1: {self.spell1} Spell2: {self.spell2} \n" \
            f"Floor: {self.level}   Area: {self.room} \n")

    def clearScreen(self):
        print("\n"*50)

    def addGold(self, g):
        self.gold += g
        if self.gold < 0:
            self.gold = 0

    def nextRoom(self):
        self.room += 1
        if self.food > 0:
            self.addFood(-1)
        else:
            self.addHP(-2)
        self.beatenMonster = False
        if self.room == 3:
            self.level = 2
        elif self.room == 5:
            self.level = 3
        elif self.room == 8:
            self.level = 4
        elif self.room == 11:
            self.level = 5
        

    def addArmor(self, a):
        self.armor += a
        if self.armor < 0:
            self.armor = 0

    def setArmor(self, a):
        self.armor = a
    
    def setFood(self, f):
        self.food = f

    def setGold(self, g):
        self.gold = g

    def setHP(self, h):
        self.hp = h

    def addXP(self, x):
        self.xp += x
        if self.xp < 0:
            self.xp = 0

        if self.xp < 7:
            self.rank = 1
        elif self.xp >= 7 and self.xp <= 18:
            self.rank = 2
        elif self.xp >= 19 and self.xp <= 36:
            self.rank = 3
        elif self.xp > 36:
            self.rank = 4
        

    def addFood(self, f):
        self.food += f

        if self.food < 0:
            self.food = 0

    def addHP(self, h):
        self.hp += h

    def getHP(self):
        return self.hp

    def getFood(self):
        return self.food

    def addSpell(self, s):
        if self.spell1 == "":
            self.spell1 = s
        elif self.spell2 =="":
            self.spell2 = s
        else:
            print(f"Remove Spell? 1. {self.spell1}    2. {self.spell2}    3. No")
            inp = self.getInput(["1", "2", "3"])
            if inp == "1":
                self.spell1=""
                self.addSpell(s)
            elif inp == "2":
                self.spell2=""
                self.addSpell(s)
            elif inp == "3":
                return
            else:
                self.addSpell(s)
        return

    def skillCheck(self):
        #Roll a die, if the roll is less than or equal to your rank, you pass, otherwise you fail
        self.scrollPrint("Rolling Skill Check...")
        time.sleep(self.stallTime)
        r = random.randint(1, 6)

        if r <= self.rank:
            self.scrollPrint("Skill Check Succeeded")
            time.sleep(self.stallTime)
            return True

        else:
            self.scrollPrint("Skill Check Failed")
            time.sleep(self.stallTime)
            return False

    def treasureRoom(self):
        self.clearScreen()
        self.printSelf()
        self.scrollPrint("You've stumbled upon an old treasure room")
        time.sleep(self.stallTime)
        #If you have beaten a monster, you gain 2 gold, otherwise you gain 1
        if self.beatenMonster:
            self.scrollPrint("You Found 2 Gold!")
            self.addGold(2)

        else:
            self.scrollPrint("You Found 1 Gold!")
            self.addGold(1)
            
        time.sleep(self.stallTime)

        #Roll a die, on a 5-6 you get an additional treasure
        r = random.randint(1, 6)
        if r >= 5:
            self.scrollPrint("Wait... There appears to be more!")
            time.sleep(self.stallTime)
            treasure = random.randint(1,6)
            if treasure == 1:
                self.scrollPrint("You've found a better shield! (+1 Armor)")
                self.addArmor(1)
            elif treasure == 2:
                self.scrollPrint("You've found a better sword! (+2 XP)")
                self.addXP(2)
            elif treasure == 3:
                self.scrollPrint("You've found a scroll of Fireball!")
                self.addSpell("Fireball")
            elif treasure == 4:
                self.scrollPrint("You've found a scroll of Ice!")
                self.addSpell("Ice")
            elif treasure == 5:
                self.scrollPrint("You've found a scroll of Poison!")
                self.addSpell("Poison")
            elif treasure == 6:
                self.scrollPrint("You've found a scroll of Healing!")
                self.addSpell("Healing")

        time.sleep(self.stallTime)
        input("Press Enter to Continue... ")


    def merchantRoom(self):        
        
        while True:
            self.clearScreen()
            self.printSelf()
            self.scrollPrint("You've stumbled upon a merchant down here... how odd...")
            time.sleep(self.stallTime)
            self.scrollPrint("What would you like to buy? \n")
            time.sleep(self.stallTime)
            print("1. Ration / 1 Gold (Gain 1 Food)")
            print("2. Health Potion / 1 Gold (Gain 1 HP)")
            print("3. Big Health Potion / 3 Gold (Gain 4 HP)")
            print("4. Armor Piece / 6 Gold (Gain 1 Armor)")
            print("5. Any Spell / 8 Gold")
            print("6. Leave")
        
            inp = self.getInput(["1", "2", "3", "4", "5", "6"])
            if inp == "1":
                if self.gold >= 1:
                    self.addFood(1)
                    self.addGold(-1)

            elif inp == "2":
                if self.gold >= 1:
                    self.addHP(1)
                    self.addGold(-1)

            elif inp == "3":
                if self.gold >= 3:
                    self.addHP(4)
                    self.addGold(-3)

            elif inp == "4":
                if self.gold >= 6:
                    self.addArmor(1)
                    self.addGold(-6)

            elif inp == "5":
                if self.gold >= 8:
                    self.scrollPrint("Which spell? 1. Fireball  2. Ice  3. Poison   4. Healing")
                    inp2 = self.getInput(["1","2","3","4"])
                    if inp2 == "1":
                        self.addSpell("Fireball")
                    elif inp2 == "2":
                        self.addSpell("Ice")
                    elif inp2 == "3":
                        self.addSpell("Poison")
                    elif inp2 == "4":
                        self.addSpell("Healing")
                    else:
                        self.addGold(8)

                    self.addGold(-8)

            elif inp == "6":
                break

        return

    def restingRoom(self):
        self.clearScreen()
        self.printSelf()
        self.scrollPrint("Finally... a moment for rest. What would you like to do? \n")
        time.sleep(self.stallTime)
        self.scrollPrint("1. Sharpen Your Weapons (+1 XP)")
        self.scrollPrint("2. Search for Rations (+1 Food)")
        self.scrollPrint("3. Heal (+2 HP)")
        inp = self.getInput(["1", "2", "3"])

        if inp == "1":
            self.scrollPrint("You've made your weapon even more deadly!")
            self.addXP(1)
        elif inp == "2":
            self.scrollPrint("Yum! A questionable piece of meat! How lucky!")
            self.addFood(1)
        elif inp == "3":
            self.scrollPrint("You wrap your wounds. Now there's a little less blood!")
            self.addHP(2)
        else:
            self.restingRoom()
        
        input("Press Enter to Continue... ")
        return

    def eventAdjustment(self, x):
        if x > 5:
            return 0
        elif x < 0:
            return 5
        else:
            return x

    def eventRoom(self):
        self.clearScreen()
        self.printSelf()
        events = ["Find a Ration (+1 Food)", "Find a Health Potion (+2 HP)", "Find some Loot (+2 Gold)", "Find a Better Sword (+2 XP)", "Find a  Shield (+1 Armor)", " Encounter a monster!!!"]
        rolledEvent = random.randint(0, 5)
        self.scrollPrint(f"You {events[rolledEvent]}")
        time.sleep(self.stallTime)
        self.scrollPrint("You have a chance to change fate. Would you like to try?")
        time.sleep(self.stallTime)
        optionA = self.eventAdjustment(rolledEvent - 1)
        optionB = self.eventAdjustment(rolledEvent + 1)
        print(f"1. Try to {events[optionA]} 2. Try to {events[optionB]} 3. {events[rolledEvent]} \n")
        inp = self.getInput(["1", "2", "3"])
        
        if inp == "1":
            if self.skillCheck():
                rolledEvent = optionA

        elif inp == "2":
            if self.skillCheck():
                rolledEvent = optionB
        
        self.scrollPrint("You" + " " + events[rolledEvent])
        if rolledEvent == 0:
            self.addFood(1)
        elif rolledEvent == 1:
            self.addHP(2)
        elif rolledEvent == 2:
            self.addGold(2)
        elif rolledEvent == 3:
            self.addXP(2)
        elif rolledEvent == 4:
            self.addArmor(1)
        elif rolledEvent == 5:
            time.sleep(self.stallTime + 1)
            self.enterRoom("Monster")
            
            
        
        if rolledEvent != 5:
            input("Press Enter to Continue... ")
        return

    def trapRoom(self):
        self.scrollPrint("Oh no! It's a trap!!!")
        time.sleep(self.stallTime)
        rolledTrap = random.randint(1, 6)
        escapedTrap = self.skillCheck()

        if rolledTrap == 1:
            if not escapedTrap:
                self.scrollPrint("Mold Spores explode making some of your food inedible (-1 food)")
                self.addFood(-1)
        elif rolledTrap == 2:
            if not escapedTrap:
                self.scrollPrint("A wire trap makes you trip and drop some of your gold (-1 Gold)")
                self.addGold(-1)
        elif rolledTrap == 3:
            if not escapedTrap:
                self.scrollPrint("Acid spews from the walls, forcing the sacrifice of your shield (-1 Armor)")
                self.addArmor(-1)
        elif rolledTrap == 4:
            if not escapedTrap:
                self.scrollPrint("Some spikes emerge from the walls and impale your shoulder (-1 HP)")
                self.addHP(-1)
        elif rolledTrap == 5:
            if not escapedTrap:
                self.scrollPrint("The walls begin to close in forcing you to sacrifice your sword (-1 XP)")
                self.addXP(-1)
        elif rolledTrap == 6:
            if not escapedTrap:
                self.scrollPrint("Pit Fall!")
                self.scrollPrint("The floor opens up beneath you and you fall to the floor below (-2 HP & +1 Floor)")
                if self.level == 5:
                    self.scrollPrint("Oh Wait... there are no floors below you...")
                    time.sleep(self.stallTime)
                time.sleep(self.stallTime)
                self.scrollPrint("Hope you're ready for it!")
                self.addHP(-2)
                self.level = self.roomBelow[self.room]
          
        if escapedTrap:
            self.scrollPrint("You Avoided the Trap!!!")

        time.sleep(self.stallTime)
        input("Press Enter to Continue... ")
        return

    def critCheck(self, dice):
        for i in range(0, len(dice)):
            if dice[i][len(dice[i]) - 1] == 6:
                return True

        return False

    def arrayToSum(self, a):
        if a[len(a)-1] == 1:
            return 0
        
        _sum = 0
        for i in a:
            _sum += i

        return _sum


    def monsterRoom(self, monsterHealth, damage):
        self.clearScreen()
        self.scrollPrint("You encountered a monster! It's time to fight!!!!")
        time.sleep(self.stallTime)
        monsterPoisoned = 0
        mHealth = monsterHealth
        while(mHealth > 0 and self.hp > 0):
            
            self.printSelf()
            print(f"Monster Health: {mHealth}")
            time.sleep(self.stallTime)
            monsterFrozen = False
            rolledDice = []
            #Roll all unlocked dice
            self.scrollPrint("Rolling Dice...")
            time.sleep(self.stallTime)
            for i in range(0, self.rank):
                currentDie = []
                diceRoll = random.randint(1, 6)
                currentDie.append(diceRoll)
                rolledDice.append(currentDie)
        
            print(f"Die Results: {rolledDice}")
            time.sleep(self.stallTime)
        
            #Reroll anycrits
            while self.critCheck(rolledDice):
                for i in range(0, len(rolledDice)):
                    if rolledDice[i][len(rolledDice[i]) - 1] == 6:
                        self.scrollPrint(f"Die {i+1} is a crit. Would you like to roll again?")
                        self.scrollPrint("1. Yes   2. No")
                        inp = self.getInput(["1", "2"])
                        if inp == "1":
                            diceRoll = random.randint(1, 6)
                            rolledDice[i].append(diceRoll)
                            i = 0

                        else:
                            rolledDice[i].append(0)

                        self.scrollPrint(rolledDice)

            #Add Values Together
            sumDamage = 0
            for i in range(0, len(rolledDice)):
                sumDamage += self.arrayToSum(rolledDice[i])

            self.scrollPrint(f"You Dealt {sumDamage + (5 * monsterPoisoned)} Damage")
            time.sleep(self.stallTime)
            mHealth -= sumDamage + (5 * monsterPoisoned)
            #input("Press Enter to Continue: ")

            #Cast a Spell
            if self.spell1 != "" or self.spell2 != "":
                self.scrollPrint("Would you like to cast a spell?")
                self.scrollPrint(f"1. {self.spell1}    2.{self.spell2} 3. No Spell")
                inp = self.getInput(["1", "2", "3"])
                spellCast = ""
                if inp == "1":
                    spellCast = self.spell1
                    self.spell1 = ""

                elif inp == "2":
                    spellCast = self.spell2
                    self.spell2 = ""

                else:
                    spellCast = ""

                if spellCast == "Fireball":
                    mHealth -= 8
                elif spellCast == "Ice":
                    monsterFrozen = True
                elif spellCast == "Poison":
                    monsterPoisoned += 1
                elif spellCast == "Healing":
                    self.addHP(8)

            if mHealth > 0 and monsterFrozen == False:
                self.scrollPrint("The monster counterattacks!")
                time.sleep(self.stallTime)
                totalDamage = damage - self.armor
                if totalDamage < 0:
                    totalDamage = 0
                self.scrollPrint(f"It deals {totalDamage} damage")
                self.addHP(totalDamage * -1)
                time.sleep(self.stallTime)

            time.sleep(self.stallTime)

            if mHealth > 0:
                self.clearScreen()

        
        if self.hp > 0:
            self.scrollPrint("YOU'VE WON!!!!")
            time.sleep(self.stallTime)
            if self.bossRoom == False:
                self.addXP(self.levelToXPBase[self.level])
                self.scrollPrint(f"You Receive {self.levelToXPBase[self.level]} XP")
                
                
            else:
                self.addXP(self.levelToXPBase[self.level])
                self.addGold(self.levelToCoinBoss[self.level])
                treasure = random.randint(1,6)
                if treasure == 1:
                    self.scrollPrint("It dropped a better shield! (+1 Armor)")
                    self.addArmor(1)
                elif treasure == 2:
                    self.scrollPrint("It dropped a better sword! (+2 XP)")
                    self.addXP(2)
                elif treasure == 3:
                    self.scrollPrint("It dropped a scroll of Fireball!")
                    self.addSpell("Fireball")
                elif treasure == 4:
                    self.scrollPrint("It dropped a scroll of Ice!")
                    self.addSpell("Ice")
                elif treasure == 5:
                    self.scrollPrint("It dropped a scroll of Poison!")
                    self.addSpell("Poison")
                elif treasure == 6:
                    self.scrollPrint("It dropped a scroll of Healing!")
                    self.addSpell("Healing")
                    
                time.sleep(self.stallTime)
            

            self.beatenMonster = True
        return


    def enterRoom(self, roomName):
        if roomName == "Monster":
            if self.bossRoom == False:
                r = random.randint(1, 6)
                mhp = self.room + r
                mdmg = self.level * 2
                self.monsterRoom(mhp, mdmg)
                
            else:
                mdmg = self.levelToDamageBoss[self.level]
                mhp = (self.level + 1) * 5
                self.monsterRoom(mhp, mdmg)
                    
            input("Press Enter to Continue... ")

        elif roomName == "Treasure":
            self.treasureRoom()

        elif roomName == "Merchant":
            self.merchantRoom()

        elif roomName == "Rest Area":
            self.restingRoom()

        elif roomName == "Random Event":
            self.eventRoom()

        elif roomName == "Trap":
            self.trapRoom()




