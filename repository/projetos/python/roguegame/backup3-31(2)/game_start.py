from os import system as sys
import characters
from platform import system
clear_by_system = system()

if clear_by_system == "Windows":
    clear_by_system = "cls"
elif clear_by_system == "Linux":
    clear_by_system = "clear"
# aramazena a ultima entrada coletada
last_input = ''

# coletor de entrada formatando-a e com variavel de buffer para ultima entrada coletada
def input_mod():
    global last_input
    last_input = input("    ~~#")

# file type:player_name class_name #[money -] $[atributes -] &[itens -]

def getdata():
    file = open("cache.dt","r")
    data = file.readlines()
    file.close()

    buffer = []
    i=0
    while(i < len(data)):
        sbuffer = []
        data[i] = data[i][:-1]
        if data[i] == '<<<<>>>>':
            while (i < len(data)):
                i += 1
                if data[i] == '>>>><<<<': break
                bffr = ''
                sbffr = ''
                c = 0
                while(c < len(data[i])):
                    if data[i][c] == '\n': break
                    bffr += data[i][c]
                    if data[i][c] == ':':
                        sbffr = bffr
                        bffr = ''
                    c+=1
                sbuffer.append((sbffr,bffr))
            print(sbuffer)
            buffer.append(tuple(sbuffer))
        i+=1


    return buffer

def setdata(player,character):
    file = open("cache.dt", "w")
    file.write('<<<<>>>>\n')
    file.write('class:'+character.CLASS+'\nname:'+player.ID+'\n')
    for v in list(player.VALUES.items()):
        file.write(v[0]+':'+str(v[1])+'\n')

    for v in list(player.RESOURCES.items()):
        file.write(v[0]+':'+str(v[1])+'\n')

    for v in list(player.BAG.items()):
        file.write(v[0]+':'+str(v[1])+'\n')

    file.write('level:'+str(player.LEVEL)+'\nxp:'+str(player.XP)+'\nmaestry:'+str(player.MASTERY))
    file.write('\n>>>><<<<')


# limpa a tela
def cls():
    sys(clear_by_system) or None


# cria um menu - options<opcoes para escolha> title<titulo(opicional, passar como parametro 'none', para ignorar o titulo, se deixar vazio sera formatado)>
def menu(options:list = [], title:str = '', display:str = "line"):

    if title != '' and title != "none": print("\n\n    --"+title+"--",end="\n\n\n")
    elif title == '': print("\n\n\n\n")

    if len(options) != 0:

        if display == "column":
            print("    ",end='')
            for i in options:
                print("["+i[0]+']'+i[1:],end='  ')
            print("\n\n")
        else:
            for i in options:
                print("    ["+i[0]+']'+i[1:],end='\n\n')
            print()

        input_mod()
        cls()


print(r"""
                               Void Steam
    
            [created by Bruno Dall'agnol 6_3_2020 v0.0 (alpha)]



                           press ENTER to play





""")

input_mod()

# inicia um novo jogo
def new_game():
    cls()
    menu(["Magic","Phisic(Semi Implemented)","Technological(Not Implemented)","intelligence(Not Implemented)"],"Select your way")

    cls()
    menu(title="select your character")

    if last_input == 'M' or last_input == 'm':
        
        menu(["Necromancer","Runic Wizard","Divine Magican","Elemental Summoner"],"none")

        if last_input == 'N' or last_input == 'n':
            player = characters.Character(characters.necromancer())

        if last_input == 'R' or last_input == 'r':
            player = characters.Character(characters.runicwizard())

        if last_input == 'D' or last_input == 'd':
            player = characters.Character(characters.divinemagican())

        if last_input == 'E' or last_input == 'e':
            player = characters.Character(characters.elementalsummoner())

    elif last_input == 'P' or last_input == 'p':

        menu(["Barbarian","Samurai","Tanker","Wild Hunter"],"none")
        
        if last_input == 'B' or last_input == 'b':
            player = characters.Character(characters.barbarian())

        if last_input == 'S' or last_input == 's':
            player = characters.Character(characters.samurai())

        if last_input == 'T' or last_input == 't':
            player = characters.Character(characters.tanker())

        if last_input == 'W' or last_input == 'w':
            player = characters.Character(characters.wildhunter())


    elif last_input == 'T' or last_input == 't':

        menu(["Mechanical","Sniper","Eletric Boomber","Digital Slayer"],"none")
        
        if last_input == 'M' or last_input == 'm':
            player = characters.Character(characters.mechanical())

        if last_input == 'S' or last_input == 's':
            player = characters.Character(characters.sniper())

        if last_input == 'E' or last_input == 'e':
            player = characters.Character(characters.eletricboomber())

        if last_input == 'D' or last_input == 'd':
            player = characters.Character(characters.digitalslayer())


    elif last_input == 'I' or last_input == 'i':

        menu(["Ninja","Wise Elder","Stealthy Archer","Field Strategist"],"none")

        if last_input == 'N' or last_input == 'n':
            player = characters.Character(characters.ninja())

        if last_input == 'W' or last_input == 'w':
            player = characters.Character(characters.wiseelder())

        if last_input == 'S' or last_input == 's':
            player = characters.Character(characters.stealthyarcher())

        if last_input == 'F' or last_input == 'f':
            player = characters.Character(characters.fieldstrategist())

    else:
        new_game()
        
    menu(["Acept", "Return"], "none", "column")
        
    if last_input == 'R' or last_input == 'r':
        new_game()
    
# da sequencia ao jogo, podendo esclolher entre os saves
def continue_game():
    cls()
    print("\n\n    --select saves--")
    
# configuracoes do jogo
def setings():
    cls()
    
# permite apagar, modificar os jogos salvos
def gerency():
    cls()
    
# funcao inicial, menu
def home():
    cls()
    menu(["New game","Continue(Not Implemented)","Setings(Not Implemented)","Gerency saves(Not Implemented)"])
    
    if last_input == 'N' or last_input == 'n':
        new_game()
    elif last_input == 'C' or last_input == 'c':
        continue_game()
    elif last_input == 'S' or last_input == 's':
        setings()
    elif last_input == 'G' or last_input == 'g':
        gerency()
    else:
        home()
        
home()