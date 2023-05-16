


class Character:
    name = ""
    HP = -1
    AC = -1
    INIT = -1
    turn = False

    def __init__(self, newName, initHealth, armor, speed):
            self.name =  newName
            self.HP = int(initHealth)
            self.AC = int(armor)
            self.INIT = int(speed)
    
    def modHP(self, value):
          self.HP = self.HP + value

    def modAC(self, value):
          self.AC = self.AC + value

    def modInit(self, value):
          self.INIT = self.INIT + value

    def getInit(self):
            return self.INIT  
