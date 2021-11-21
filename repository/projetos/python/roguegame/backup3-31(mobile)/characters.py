from secrets import randbelow

# probabilidade de ocorrencia
def prob_fo(val:int):
    return int(randbelow(100) < val)

class Character:

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

        self.ALLATRIBUTES = [
            self.HP,
            self.MP,
            self.HP_REGEN,
            self.MP_REGEN,
            self.DAMAGE,
            self.CRITICAL_DAMAGE,
            self.CRITICAL_RATE,
            self.ARMOR,
            self.DODGE,
            self.VELOCITY
        ]

        # fila de modificadores de dano e vida
        self.HP_MOD = [

        ]
        self.DAMAGE_MOD = [

        ]

def charater_info(atr:list):

    print("\n\n    --"+atr[0]
     +"--\n\n\n    <HP - "+str(atr[1])+" | REGEN - "+str(atr[3])
          +"pc>\n    <MP - "+str(atr[2])+" | REGEN - "+str(atr[4])
          +"pc>\n    <DAMAGE - "+str(atr[5])
          +">\n    <CRIT DAMAGE - "+str(atr[6])+" | RATE - "+str(atr[7])
          +"%>\n    <ARMOR - "+str(atr[8])
          +">\n    <DODGE - "+str(atr[9])
          +"%>\n    <VEL - "+str(atr[10])+"c>\n")

def necromancer():
    charater_info(["Necromancer", 400,1000,2,10,120,0,0,0,5,10])

    print("    #---------------------------------------------------------------#\n"
          "    |     Desde o inicio dos tempos a força do submundo se espande, |\n"
          "    | mas  á um  ponto na  historia em  que esse  poder se  revolta |\n"
          "    | violentamente. Tomando forma, surge o  necromante, um ser que |\n"
          "    | pode  controlar  os  vivos  e  fazer  os  mortos  retornarem. |\n"
          "    #---------------------------------------------------------------#\n")
    return ["Necromancer",400,1000,10,30,120,0,0,0,5,10]

def runicwizard():
    charater_info(["Runic Wizard", 600,600,20,80,240,20,30,20,0,4])

    print("    #---------------------------------------------------------------#\n"
          "    |     Escritas runicas, as gravuras mais primitivas e poderosas |\n"
          "    | do  mundo,  que  podem  manipular  tudo  a  sua volta,  Mas é |\n"
          "    | necessario  uma vida  de estudos  para dominar  o seu  poder. |\n"
          "    | O mago runico usa-as para criar magias altamente destrutivas. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Runic Wizard", 600,600,20,80,240,20,30,20,0,4]

def divinemagican():
    charater_info(["Divine Magican", 1200, 500, 60, 10, 90, 0, 0, 30, 5, 4])

    print("    #---------------------------------------------------------------#\n"
          "    |     Cultos  antigos que adoravam  um  deus  supremo,  o  qual |\n"
          "    | concebia  poderes  ao  seu seguidor mais apto  uma  vez entre |\n"
          "    | milenios. o mago divino teve o  nessesario para aderir a este |\n"
          "    | poder, podendo conceber quase imortalidade a quem nessecitar. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Divine Magican", 1200, 500, 60, 10, 90, 0, 0, 30, 5, 4]


def elementalsummoner():
    charater_info(["Elemental Summoner", 400, 600, 20, 40, 100, 120, 40, 0, 10, 50])

    print("    #---------------------------------------------------------------#\n"
          "    |     As forcas elementais  do mundo se condensaram ao longo do |\n"
          "    | tempo, formando violentas catastrofes, e em um desses eventos |\n"
          "    | surgiu o invocador elemental,  podendo manipular todo o meio  |\n"
          "    | natural,  gerando catastrofes  e seres elementais  colossais. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Elemental Summoner", 400, 600, 20, 40, 100, 120, 40, 0, 10, 50]

def barbarian():
    charater_info(["Barbarian", 1500, 200, 100, 10, 140, 80, 10, 50, 0, 60])

    print("    #---------------------------------------------------------------#\n"
          "    |     As forcas elementais  do mundo se condensaram ao longo do |\n"
          "    | tempo, formando violentas catastrofes, e em um desses eventos |\n"
          "    | surgiu o invocador elemental,  podendo manipular todo o meio  |\n"
          "    | natural,  gerando catastrofes  e seres elementais  colossais. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Barbarian", 1500, 200, 100, 10, 140, 80, 10, 50, 0, 60]

def samurai():
    charater_info(["Samurai", 1200, 80, 40, 20, 90, 20, 80, 80, 20, 30])

    print("    #---------------------------------------------------------------#\n"
          "    |     As forcas elementais  do mundo se condensaram ao longo do |\n"
          "    | tempo, formando violentas catastrofes, e em um desses eventos |\n"
          "    | surgiu o invocador elemental,  podendo manipular todo o meio  |\n"
          "    | natural,  gerando catastrofes  e seres elementais  colossais. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Samurai", 1200, 80, 40, 20, 90, 20, 80, 80, 20, 30]

def tanker():
    charater_info(["Tanker", 2400, 600, 20, 40, 30, 0, 0, 50, 30, 5])

    print("    #---------------------------------------------------------------#\n"
          "    |     As forcas elementais  do mundo se condensaram ao longo do |\n"
          "    | tempo, formando violentas catastrofes, e em um desses eventos |\n"
          "    | surgiu o invocador elemental,  podendo manipular todo o meio  |\n"
          "    | natural,  gerando catastrofes  e seres elementais  colossais. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Tanker", 2400, 600, 20, 40, 30, 0, 0, 50, 30, 5]

def wildhunter():
    charater_info(["Wild Hunter", 1100, 700, 40, 20, 120, 100, 50, 20, 20, 30])

    print("    #---------------------------------------------------------------#\n"
          "    |     As forcas elementais  do mundo se condensaram ao longo do |\n"
          "    | tempo, formando violentas catastrofes, e em um desses eventos |\n"
          "    | surgiu o invocador elemental,  podendo manipular todo o meio  |\n"
          "    | natural,  gerando catastrofes  e seres elementais  colossais. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Wild Hunter", 1100, 700, 40, 20, 120, 100, 50, 20, 20, 30]

