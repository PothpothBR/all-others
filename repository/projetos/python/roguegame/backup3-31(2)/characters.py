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
          "    |     Com sangue  nos olhos,  força brutal  e dois  machados  o |\n"
          "    | barbáro causa destruicao a  sua volta, ficando cada  vez mais |\n"
          "    | frenetico ao  ponto que fica  mais ferido,  quando tombar  em |\n"
          "    | batalha todos  tombarao juntos, só  nao o deixe mais furioso. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Barbarian", 1500, 200, 100, 10, 140, 80, 10, 50, 0, 60]

def samurai():
    charater_info(["Samurai", 1200, 80, 40, 20, 90, 20, 80, 80, 20, 30])

    print("    #---------------------------------------------------------------#\n"
          "    |     Tecnicas de arte com  espada que  foram  aperfeicoadas de |\n"
          "    | geracao  em  geracao.   O  samurai,   uma  muralha  altamente |\n"
          "    | destrutiva que  aniquila qualquer  um  que  atrapalhar  a sua |\n"
          "    | marcha,  com golpes  da sua  katana. É melhor nao o desafiar. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Samurai", 1200, 80, 40, 20, 90, 20, 80, 80, 20, 30]

def tanker():
    charater_info(["Tanker", 2400, 600, 20, 40, 30, 0, 0, 50, 30, 5])

    print("    #---------------------------------------------------------------#\n"
          "    |     É uma montanha?, é muralha?, é o tanker! Desde pequeno ja |\n"
          "    | demonstrava aptidao a batalha, sua marcha lenta e resistencia |\n"
          "    | incomparavel, sendo praticamente imparavel,  ele soterra seus |\n"
          "    | inimigos  sob seus pes,  e defende seus aliados  até a morte. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Tanker", 2400, 600, 20, 40, 30, 0, 0, 50, 30, 5]

def wildhunter():
    charater_info(["Wild Hunter", 1100, 700, 40, 20, 120, 100, 50, 20, 20, 30])

    print("    #---------------------------------------------------------------#\n"
          "    |     Abandonado  recem  nascido  em  uma  densa  floresta,  ao |\n"
          "    | meio de animais selvagens,  sobreviveu por pura sorte  ou por |\n"
          "    | destino? Só o que se sabe é que, por uma vida de experiencia, |\n"
          "    | ele  caça com armadilhas e  com o seus animais  de estimacao. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Wild Hunter", 1100, 700, 40, 20, 120, 100, 50, 20, 20, 30]

def mechanical():
    charater_info(["Mechanical", 800, 400, 240, 80, 60, 20, 10, 180, 10, 40])

    print("    #---------------------------------------------------------------#\n"
          "    |     Conhecimento  e  tecnologia  de  ponta é o que o mecanico |\n"
          "    | presisa, montando armas absurdamente  poderosas e destritivas |\n"
          "    | ele  passa o  seu  tempo  livre. Seu poder  de  fogo  é  quse |\n"
          "    | ilimitado, so nao se pode deixar faltar esplosivos e minução. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Mechanical", 800, 400, 240, 80, 60, 20, 10, 180, 10, 40]

def sniper():
    charater_info(["Sniper", 300, 100, 10, 80, 200, 600, 20, 0, 30, 4])

    print("    #---------------------------------------------------------------#\n"
          "    |     A sombra da morte, esguio o sniper somente se revela para |\n"
          "    | executar seu alvo,  com incrivel precisao,  nao qeira ser seu |\n"
          "    | alvo, pois sua investida é lenta,  mas sua arma pode executar |\n"
          "    | qualquer um com apenas um tiro.  Ele nao precisa mais que um. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Sniper", 300, 100, 10, 80, 200, 600, 20, 0, 30, 4]

def eletricboomber():
    charater_info(["Eletric Boomber", 800, 600, 50, 50, 320, 0, 0, 50, 0, 30])

    print("    #---------------------------------------------------------------#\n"
          "    |     Esplodir é sua especialidade, o bombardeiro elétrico é um |\n"
          "    | cyborg que manipula livremente  um quantidade inmensuravel de |\n"
          "    | armamento  esplosivo,  desde  minas eletricas,  até morteiros |\n"
          "    | termo nucleares, o seu  unco problema é a demora para atacar. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Eletric Boomber", 800, 600, 50, 50, 320, 0, 0, 50, 0, 30]

def digitalslayer():
    charater_info(["Digital Slayer", 300, 1000, 40, 120, 400, 20, 10, 0, 70, 70])

    print("    #---------------------------------------------------------------#\n"
          "    |     Mais maquina do  que  humano,  esse ser  ja perdeu  a sua |\n"
          "    | conciencia a muito tempo. O digital slayer leva a morte aonde |\n"
          "    | vai, com sua velocidade beirando a da luz,  ele nao esconde a |\n"
          "    | sua presenca,  ele nao tem medo  e nao responde por si mesmo. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Digital Slayer", 300, 1000, 40, 120, 400, 20, 10, 0, 70, 70]

def ninja():
    charater_info(["Ninja", 500, 500, 100, 50, 320, 30, 30, 0, 12, 60])

    print("    #---------------------------------------------------------------#\n"
          "    |     Sombra, fantasma, vulto, existem varias descricoes para o |\n"
          "    | ninja,  mas  todas  remetem  a  um  mesmo  proposito,  alguem |\n"
          "    | indetectavel que usa de todo tipo  de arma  e abilidade  para |\n"
          "    | derrotar o inimigo, ele entra, e le sai, e voce nunca sabera. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Ninja", 500, 500, 100, 50, 320, 30, 30, 0, 12, 60]

def wiseelder():
    charater_info(["Wise Elder", 300, 1200, 10, 110, 20, 500, 40, 40, 50, 8])

    print("    #---------------------------------------------------------------#\n"
          "    |     Antes do surgimento das  grandes civilizacoes ele  estava |\n"
          "    | lá observando, medindo, estudando.  O sábio ancião usa de seu |\n"
          "    | intelecto e experiencia para manipular os inimigos, e fazerem |\n"
          "    | o que ele deseja,  mas por cima,  parece  apenas um  velinho. |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Wise Elder", 300, 1200, 10, 110, 20, 500, 40, 40, 50, 8]

def stealthyarcher():
    charater_info(["Stealthy Archer", 400, 100, 20, 20, 100, 220, 20, 0, 40, 40])

    print("    #---------------------------------------------------------------#\n"
          "    |     |\n"
          "    |  |\n"
          "    |  |\n"
          "    |  |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Stealthy Archer", 400, 100, 20, 20, 100, 220, 20, 0, 40, 40]

def fieldstrategist():
    charater_info(["Field Strategist", 400, 700, 40, 20, 40, 200, 80, 0, 40, 4])

    print("    #---------------------------------------------------------------#\n"
          "    |     |\n"
          "    |  |\n"
          "    |  |\n"
          "    |  |\n"
          "    #---------------------------------------------------------------#\n")

    return ["Field Strategist", 400, 700, 40, 20, 40, 200, 80, 0, 40, 4]
