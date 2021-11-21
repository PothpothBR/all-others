from secrets import randbelow

# probabilidade de ocorrencia
def prob_fo(val:int):
    return int(randbelow(100) < val)

class Atributes:

    def __init__(self, args:list):
        # nome da classe
        self.CLASS = args[0]
        # vida e mana
        self.HP = args[1]
        self.MP = args[2]
        # regeneracao de vida e mana(por ciclo)
        self.HP_REGEN = args[3]
        self.MP_REGEN = args[4]
        # dano base
        self.DAMAGE = args[5]
        # cance de critico e dano critico [%]
        self.CRITICAL_DAMAGE = args[6]
        self.CRITICAL_RATE = args[7]
        # armadura e escudo
        self.ARMOR = args[8]
        # chance de esquiva [%]
        self.DODGE = args[9]
        # velocidade relativa aos ciclos[%]
        self.VELOCITY = args[10]

        # fila de modificadores de dano e vida
        self.HP_MOD = []
        self.DAMAGE_MOD = []

        self.HP_MOD_PLVL = 0
        self.MP_MOD_PLVL = 0

class Player(Atributes):

    def __init__(self, name: str, vals_chr: list):
        Atributes.__init__(self,vals_chr)
        self.ID = name
        self.LEVEL = 0
        self.XP = 0
        self.MASTERY = 0
        self.EQUIPAMENTTYPE = ""
        self.RANGE = 0
        self.RANGETYPE = ""
        self.VALUES = {}
        self.RESOURCES = {}
        self.BAG = {}
