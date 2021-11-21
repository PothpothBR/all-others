from os import system as sys
import characters

# aramazena a ultima entrada coletada
last_input = ''

# coletor de entrada formatando-a e com variavel de buffer para ultima entrada coletada
def input_mod():
    global last_input
    last_input = input("    ~~#")

# limpa a tela
def cls():
    sys('cls') or None

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

input()

# inicia um novo jogo
def new_game():
    cls()
    menu(["Magic","Phisic(Not Implemented)","Technological(Not Implemented)","intelligence(Not Implemented)"],"Select your way")
    
    cls()
    menu(title="select your character fitness")

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

        menu(["Acept", "Return"], "none", "column")

    elif last_input == 'P' or last_input == 'p':

        menu(["Barbarian","Samurai","Tanker","Wild Hunter"],"none")

    elif last_input == 'T' or last_input == 't':

        menu(["Mechanical","Sniper","Eletric Boomber","Digital Slayer"],"none")

    elif last_input == 'I' or last_input == 'i':

        menu(["Ninja","Wise Elder","Stealthy Archer","Field Strategist"],"none")

    else:
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