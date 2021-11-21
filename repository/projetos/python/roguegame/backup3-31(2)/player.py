
class Player:

    def __init__(self,name:str, character_class):
        self.CHARACTER = character_class
        self.ID = name
        self.VALUES = {"coins": 1, "gold": 2, "diamonds": 3}
        self.RESOURCES = {"wood": 4, "iron": 5, "herbs": 6, "milk": 7}
        self.BAG = {"sword": 0}
        self.LEVEL = 0
        self.XP = 0
        self.MASTERY = 0
