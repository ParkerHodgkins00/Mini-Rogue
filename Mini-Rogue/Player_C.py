import random


class Player_C(object):
    def __init__(self, armor, hp, gold, food, xp, rank, spell1, spell2, level, room):
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

    def __str__(self):
        return f"Armor: {self.armor}    HP: {self.hp}   Gold: {self.gold}   Food: {self.food}   XP: {self.xp}   Rank: {self.rank} \n" \
            f"Spell1: {self.spell1} Spell2: {self.spell2} \n" \
            f"Floor: {self.level}   Room: {self.room} \n"

    def printSelf(self):
        print(f"Armor: {self.armor}    HP: {self.hp}   Gold: {self.gold}   Food: {self.food}   XP: {self.xp}   Rank: {self.rank} \n" \
            f"Spell1: {self.spell1} Spell2: {self.spell2} \n" \
            f"Floor: {self.level}   Room: {self.room} \n")

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
            inp = input(f"Remove Spell? 1. {self.spell1}    2. {self.spell2}    3. No")
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
        print("Rolling Skill Check...")
        r = random.randint(1, 6)

        if r <= self.rank:
            print("Skill Check Succeeded")
            return True

        else:
            print("Skill Check Failed")
            return False

    def treasureRoom(self):
        self.clearScreen()
        self.printSelf()
        print("You've stumbled upon an old treasure room")
        #If you have beaten a monster, you gain 2 gold, otherwise you gain 1
        if self.beatenMonster:
            print("You Found 2 Gold!")
            self.addGold(2)

        else:
            print("You Found 1 Gold!")
            self.addGold(1)

        #Roll a die, on a 5-6 you get an additional treasure
        r = random.randint(1, 6)
        if r >= 5:
            print("Wait... There appears to be more!")
            treasure = random.randint(1,6)
            if treasure == 1:
                print("You've found a better shield! (+1 Armor)")
                self.addArmor(1)
            elif treasure == 2:
                print("You've found a better sword! (+2 XP)")
                self.addXP(2)
            elif treasure == 3:
                print("You've found a scroll of Fireball!")
                self.addSpell("Fireball")
            elif treasure == 4:
                print("You've found a scroll of Ice!")
                self.addSpell("Ice")
            elif treasure == 5:
                print("You've found a scroll of Poison!")
                self.addSpell("Poison")
            elif treasure == 6:
                print("You've found a scroll of Healing!")
                self.addSpell("Healing")

        input("Press Enter to Continue... ")


    def merchantRoom(self):        
        
        while True:
            self.clearScreen()
            self.printSelf()
            print("You've stumbled upon a merchant down here... how odd...")
            print("What would you like to buy? \n")
            print("1. Ration / 1 Gold (Gain 1 Food)")
            print("2. Health Potion / 1 Gold (Gain 1 HP)")
            print("3. Big Health Potion / 3 Gold (Gain 4 HP)")
            print("4. Armor Piece / 6 Gold (Gain 1 Armor)")
            print("5. Any Spell / 8 Gold")
            print("6. Leave")
        
            inp = input("Your Choice: ")
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
                    print("Which spell? 1. Fireball  2. Ice  3. Poison   4. Healing")
                    inp2 = input("Your Choice: ")
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
        print("Finally... a moment for rest. What would you like to do? \n")
        print("1. Sharpen Your Weapons (+1 XP)")
        print("2. Search for Rations (+1 Food)")
        print("3. Heal (+2 HP)")
        inp = input("Your Choice: ")

        if inp == "1":
            self.addXP(1)
        elif inp == "2":
            self.addFood(1)
        elif inp == "3":
            self.addHP(2)
        else:
            self.restingRoom()

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
        events = ["Found a Ration (+1 Food)", "Found a Health Potion (+2 HP)", "Found some Loot (+2 Gold)", "Found a Better Sword (+2 XP)", "Founda  Shield (+1 Armor)", " Encountered a monster!!!"]
        rolledEvent = random.randint(0, 5)
        print(f"You {events[rolledEvent]}")
        print("You have a chance to change fate. Would you like to try?")
        optionA = self.eventAdjustment(rolledEvent - 1)
        optionB = self.eventAdjustment(rolledEvent + 1)
        inp = input(f"1. {events[optionA]} 2. {events[optionB]} 3. {events[rolledEvent]} \n")
        
        if inp == "1":
            if self.skillCheck():
                rolledEvent = optionA

        elif inp == "2":
            if self.skillCheck():
                rolledEvent = optionB

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
            self.enterRoom("Monster")
        
        input("Press Enter to Continue... ")
        return

    def trapRoom(self):
        print("Oh no! It's a trap!!!")
        rolledTrap = random.randint(1, 6)
        escapedTrap = self.skillCheck()

        if rolledTrap == 1:
            if not escapedTrap:
                print("Mold Spores explode making some of your food inedible (-1 food)")
                self.addFood(-1)
        elif rolledTrap == 2:
            if not escapedTrap:
                print("A wire trap makes you trip and drop some of your gold (-1 Gold)")
                self.addGold(-1)
        elif rolledTrap == 3:
            if not escapedTrap:
                print("Acid spews from the walls, forcing the sacrifice of your shield (-1 Armor)")
                self.addArmor(-1)
        elif rolledTrap == 4:
            if not escapedTrap:
                print("Some spikes emerge from the walls and impale your shoulder (-1 HP)")
                self.addHP(-1)
        elif rolledTrap == 5:
            if not escapedTrap:
                print("The walls begin to close in forcing you to sacrifice your sword (-1 XP)")
                self.addXP(-1)
        elif rolledTrap == 6:
            if not escapedTrap:
                print("Pit Fall!")
                print("Work in progress")

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
        print("You encountered a monster! It's time to fight!!!!")
        monsterPoisoned = 0
        mHealth = monsterHealth
        while(mHealth > 0 and self.hp > 0):
            
            self.printSelf()
            print(f"Monster Health: {mHealth}")
            monsterFrozen = False
            rolledDice = []
            #Roll all unlocked dice
            for i in range(0, self.rank):
                currentDie = []
                diceRoll = random.randint(1, 6)
                currentDie.append(diceRoll)
                rolledDice.append(currentDie)
        
            print(f"Die Results: {rolledDice}")
        
            #Reroll anycrits
            while self.critCheck(rolledDice):
                for i in range(0, len(rolledDice)):
                    if rolledDice[i][len(rolledDice[i]) - 1] == 6:
                        print(f"Die {i+1} is a crit. Would you like to roll again?")
                        print("1. Yes   2. No")
                        inp = input("Your Choice: ")
                        if inp == "1":
                            diceRoll = random.randint(1, 6)
                            rolledDice[i].append(diceRoll)
                            i = 0

                        else:
                            rolledDice[i].append(0)

                        print(rolledDice)

            #Add Values Together
            sumDamage = 0
            for i in range(0, len(rolledDice)):
                sumDamage += self.arrayToSum(rolledDice[i])

            print(f"You Dealt {sumDamage + (5 * monsterPoisoned)} Damage")
            mHealth -= sumDamage + (5 * monsterPoisoned)
            #input("Press Enter to Continue: ")

            #Cast a Spell
            if self.spell1 != "" or self.spell2 != "":
                print("Would you like to cast a spell?")
                print(f"1. {self.spell1}    2.{self.spell2} 3. No Spell")
                inp = input("Your Choice: ")
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
                print("The monster counterattacks!")
                print(f"It deals {damage - self.armor} damage")

            input("Press Enter to Continue... ")

            self.clearScreen()

        
        if self.hp > 0:
            if self.level == 1:
                self.addXP(1)
            elif self.level == 2:
                self.addXP(1)
            elif self.level == 3:
                self.addXP(2)
            elif self.level == 4:
                self.addXP(2)
            elif self.level == 5:
                self.addXP(3)

            self.beatenMonster = True
        return


    def enterRoom(self, roomName):
        if roomName == "Monster":
            r = random.randint(1, 6)
            mhp = self.room + r
            mdmg = self.level * 2
            self.monsterRoom(mhp, mdmg)
            input("Press Enter to Continue... ")

        elif roomName == "Treasure":
            self.treasureRoom()

        elif roomName == "Merchant":
            self.merchantRoom()

        elif roomName == "Resting":
            self.restingRoom()

        elif roomName == "Event":
            self.eventRoom()

        elif roomName == "Trap":
            self.trapRoom()




