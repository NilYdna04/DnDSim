from Character import Character
from tabulate import tabulate

# TODO: code in armor break and armor add

class DnDSim:
    enemyList = []
    charTable = []
    combat = False

    def __init__(self):
        pass

    def invalidCommand(self):
        raise Exception("Invalid Command")
    
    def printCharacters(self):
        self.charTable.clear()
        self.charTable = [["Num", "Name", "HP", "AC", "INIT", "Turn"]]
        index = 0
        for character in self.enemyList:
            name = character.name
            health = character.HP
            armor = character.AC
            initiative = character.INIT
            if character.turn == True:
                turn = 'x'
            else:
                turn = ""
            self.charTable.append([index, name, health, armor, initiative, turn])
            index = index + 1
        print(tabulate(self.charTable, headers='firstrow', tablefmt='fancy_grid'))
    
    def startCombat(self):
        self.enemyList[0].turn = True
        self.combat = True
    
    def nextTurn(self):
        if self.combat == False:
            print("Error: Combat hasn't started yet!")
            return
        index = 0
        for character in self.enemyList:
            if character.turn:
                character.turn = False
                index = index + 1
                if index == len(self.enemyList):
                    index = 0
                self.enemyList[index].turn = True
                break
            index = index + 1

    def addCharacter(self):
        name = input("name? ")
        try:
            hp =int(input("HP? "))
            ac = int(input("AC? "))
            initiative = int(input("initiative? "))
            
            newCharacter = Character(name, hp, ac, initiative)
        except:
            print("Error: expected int value")
            self.addCharacter()

        self.enemyList.append(newCharacter)
        self.enemyList.sort(key=Character.getInit, reverse= True)

    def removeCharacter(self):
        if not self.enemyList:
            print("Error: character list is empty")
            return
        try:
            index = input("which character?")
            index = int(index)
            if self.enemyList[index].turn == True:
                self.nextTurn()
            self.enemyList.pop(index)
            self.enemyList.sort(key=Character.getInit, reverse= True)
        except:
            print("Error: index is not valid")
    
    def hurtCharacter(self):
        if not self.enemyList:
            print("Error: character list is empty")
            return
        try:
            index = input("which character? ")
            index = int(index)
            creature = self.enemyList[index]
        except:
            print("Error: index is not valid")
            self.hurtCharacter()
        try:
            value = input("amount? ")
            value = int(value)
            creature.modHP(-value)
        except:
            print("Error: expected int amount")
            self.hurtCharacter()

    def healCharacter(self):
        if not self.enemyList:
            print("Error: character list is empty")
            return
        try:
            index = input("which character? ")
            index = int(index)
            creature = self.enemyList[index]
        except:
            print("Error: index is not valid")
            self.hurtCharacter()
        try:
            value = input("amount? ")
            value = int(value)
            creature.modHP(value)
        except:
            print("Error: expected int amount")
            self.hurtCharacter()

    def armorBreak(self):
        if not self.enemyList:
            print("Error: character list is empty")
            return
        try:
            index = input("which character? ")
            index = int(index)
            creature = self.enemyList[index]
        except:
            print("Error: index is not valid")
            self.armorBreak()
        try:
            value = input("amount? ")
            value = int(value)
            creature.modAC(-value)
        except:
            print("Error: expected int amount")
            self.armorBreak()

    def armorAdd(self):
        if not self.enemyList:
            print("Error: character list is empty")
            return
        try:
            index = input("which character? ")
            index = int(index)
            creature = self.enemyList[index]
        except:
            print("Error: index is not valid")
            self.armorAdd()
        try:
            value = input("amount? ")
            value = int(value)
            creature.modAC(-value)
        except:
            print("Error: expected int amount")
            self.armorAdd()
        
    def reset(self):
        self.enemyList.clear()

    def processInput(self):
        command = input("Enter your command: ")
        if command == "quit":
            return False
        
        commandDic = {
            "add": self.addCharacter,
            "remove": self.removeCharacter,
            "damage" : self.hurtCharacter,
            "heal" : self.healCharacter,
            "start" : self.startCombat,
            "next" : self.nextTurn,
            "armorb" : self.armorBreak,
            "armora" : self.armorAdd,
            "reset" : self.reset
        }
    
        command = commandDic.get(command, self.invalidCommand)
        command()
        return True
    
   
    

    def run(self):
        print("Welcome to NilYdna's simple DnD battle simulator.")
        print("Commands:")
        print("add: adds a new character to the sim")
        print("remove: removes a character from the sim")
        print("damage: damages a character by an amount")
        print("heal: heals a character an amount")
        print("armora: adds armor to a character")
        print("armorb: removes armor from a character")
        print("start: starts combat and begins turn displaying")
        print("next: moves the marker to the next character's turn")
        print("reset: removes all characters and stops combat")
        print("quit: quits the program\n")
        valid = True
        while valid:
            try:
                self.printCharacters()
                valid = self.processInput()
            except:
                print("Invalid Command")
                print(Exception)
                continue
             
    