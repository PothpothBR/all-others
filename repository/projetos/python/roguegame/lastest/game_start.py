from header_module import cls, Player, Atributes, getdata, setdata

# aramazena a ultima entrada coletada
last_input = ''

def isequal(chr:str):
    return (last_input == chr.upper() or last_input == chr.lower())

# coletor de entrada formatando-a e com variavel de buffer para ultima entrada coletada
def input_mod():
    global last_input
    last_input = input("    ~~#")
    if last_input == "": last_input = "none"

def atributes_info(atr:list):

    print(      "\n    <PERICIA - "+atr[0]
              +">\n    <HP - "+str(atr[1])+" | REGEN - "+str(atr[3])
            +"pc>\n    <MP - "+str(atr[2])+" | REGEN - "+str(atr[4])
            +"pc>\n    <DANO - "+str(atr[5])
              +">\n    <DANO CRIT - "+str(atr[6])+" | CHANCE - "+str(atr[7])
             +"%>\n    <ARMADURA - "+str(atr[8])
              +">\n    <ESQUIVA - "+str(atr[9])
             +"%>\n    <VEL - "+str(atr[10])+"c>\n")


def player_info(atr:list):

    print("    <NOME - "+atr[0]
       + ">\n    <EQUIPAMENTO - "+atr[1]
       + ">\n    <ALCANCE - " + atr[2] +'>\n'
          )


# cria um menu - options<opcoes para escolha> title<titulo(opicional, passar como parametro 'none', para ignorar o titulo, se deixar vazio sera formatado)>
def menu(options:list = [], title:str = '', display:str = "line", _input:str = "default"):
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

    if _input != "none":
        input_mod()
        cls()


print(r"""
                               Void Steam
    
            [created by Bruno Dall'agnol 6_3_2020 v0.0 (alpha)]



                           press ENTER to play





""")

input_mod()
cls()
# inicia um novo jogo
def new_game():

    player_sts = ["none", "none", "none"]
                   #  0    1   2   3   4   5   6   7   8   9
                   # hp   mp  rhp rmp dmg dmc ccr arm esq vel
    atributes_mod = [100, 100, 5,  5,  2,  2,  0.5,  1,  0.5,  0.5]
    atributes = ["",0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    atribute_points = 100

    def addatributes(atr_point: int,points: int, index: int):

        if points > atr_point:
            points += atr_point - points
            atr_point = 0
        else:
            atr_point = atr_point - points

        atributes[index] = atributes_mod[index] * points


    def name():
        global player_name
        menu(title="Escolha o seu nome[16]")
        if last_input == "none": name()
        if len(last_input) > 16: name()
        player_sts[0] = last_input
        first_chose()

    def first_chose():

        menu(["Inteligencia", "Força", "Resistencia", "Abilidade", "Voltar"], "perícia")

        if isequal('i'):
            addatributes(atribute_points, 50, 3)
            atributes[0] = "Inteligencia"
        elif isequal('f'):
            addatributes(atribute_points, 50, 5)
            atributes[0] = "Força"
        elif isequal('r'):
            addatributes(atribute_points, 50, 1)
            atributes[0] = "Resistencia"
        elif isequal('a'):
            addatributes(atribute_points, 25, 9)
            addatributes(atribute_points, 25, 7)
            atributes[0] = "Abilidade"
        elif isequal('v'):
            home()
        else:
            first_chose()
        second_chose()


    def second_chose():
        menu(["Leves", "Pesados", "Voltar"], "Tipo de equipamentos")

        if isequal('l'):
            player_sts[1] = "leves"
        elif isequal('p'):
            player_sts[1] = "pesados"
        elif isequal('v'):
            first_chose()
        else: second_chose()
        third_chose()


    def third_chose():
        menu(["Corpo-a-corpo", "A distancia", "Voltar"], "Mecanica de jogo")
        if isequal('c'):
            player_sts[2] = "corpo-a-corpo"
        elif isequal('a'):
            player_sts[2] = "a-distancia"
        elif isequal('v'):
            second_chose()
        else: third_chose()
        fourth_chose()


    def fourth_chose():
        menu(title="info",_input="none")
        atributes_info(atributes)
        player_info(player_sts)
        menu(["Continuar", "Voltar"], "none", "column")
        if isequal('v'):
            third_chose()
        elif isequal('c'):
            player = Player(player_sts[0],atributes)
            player.EQUIPAMENTTYPE = player_sts[1]
            player.RANGETYPE = player_sts[2]
            setdata(player,"a")
        else: fourth_chose()

    name()
    
# da sequencia ao jogo, podendo esclolher entre os saves
def continue_game():
    cls()
    
# configuracoes do jogo
def setings():
    cls()
    
# permite apagar, modificar os jogos salvos
def gerency():
    menu(["Deletar todos", "Remover", "Mudar nome"],"none")

    if isequal('d'):
        setdata()

# funcao inicial, menu
def home():
    menu(["Novo jogo","Continue(Not Implemented)","Definicoes(Not Implemented)","Jogos salvos(Not Implemented)"])
    if isequal('n'):
        new_game()
    elif isequal('c'):
        continue_game()
    elif isequal('d'):
        setings()
    elif isequal('J'):
        gerency()
    else:
        home()
        
home()