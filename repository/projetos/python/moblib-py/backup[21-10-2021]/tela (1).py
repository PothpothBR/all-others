
from os import system as sy
from data_padrao import ps
from format_strings import add_spaces
from random import randint
from time import sleep
clear = lambda: sy('clear')

def titl_criacao():
    clear()
    print(r'''
               \,                                         ,/
             __ \\___    _________________________    ___// __
              \\_\   \__/                         \__/   /_//
               \, \    \   Criacao de personagem   /    / ,/
                 \_\____\_________________________/____/_/
''')
    sleep(1)

def tela_ficha():
    titl_criacao()
    
#       |             34                   |           25           |
    print(r'''
   _______________________________________________________________
 //````\___________________________________________________________\
//      \                                  |                        \
||      /    NOME: '''+ps.i20[0]+r'''    |      ID..: '''+ps.i6[0]+r'''      /
 \______\__________________________________|________________________\
   `````/                                  |                        /
       `\         CARACTERISTICAS          |  CLASSE: '''+ps.i12[0]+r'''  \
       ´/__________________________________|________________________/
       `\                                  |                        \
       ´/  VIDA...: '''+ps.i20[1][0]+r'''   |       ABILIDADES       /
       `\  DANO...: '''+ps.i20[1][1]+r'''   |________________________\
       ´/  ENERGIA: '''+ps.i20[1][2]+r'''   |                        /
       `\  ESQUIVA: '''+ps.i20[1][3]+r'''   |  '''+ps,i20[3][0]+r'''  \
       ´/  ESCUDO.: '''+ps.i20[1][4]+r'''   |  '''+ps,i20[3][1]+r'''  /
       `\  RECUPERACAO DE VIDA...: '''+ps.i6[1]+r'''  |  '''+ps.i20[3][2]+r'''  \
       ´/  RECUPERACAO DE ENERGIA: '''+ps.i6[2]+r'''  |  '''+ps.i20[4][0]+r'''  /
       `\__________________________________|  '''+ps.i20[4][1]+r'''  \
       ´/                                  |  '''+ps.i20[4][2]+r'''  /
       `\      ESCALAMENTO POR NIVEL       |  '''+psi20[5][0]+r'''  \
       ´/__________________________________|  '''+ps.i20[5][1]+r'''  /
       `\                                  |  '''+ps.i20[5][2]+r'''  \
       ´/  VIDA...: '''+ps.i20[2][0]+r'''   |  '''+ps.i20[6][0]+r'''  /
       `\  DANO...: '''+ps.i20[2][1]+r'''   |  '''+ps.i20[6][1]+r'''  \
       ´/  ENERGIA: '''+ps.i20[2][2]+r'''   |  '''+ps.i20[6][2]+r'''  /
       `\  ESQUIVA: '''+ps.i20[2][3]+r'''   |  '''+ps.i20[7][0]+r'''  \
       ´/  ESCUDO.: '''+ps.i20[2][4]+r'''   |  '''+ps.i20[7][1]+r'''  /
       `\  RECUPERACAO DE VIDA...: '''+ps.i6[3]+r'''  |  '''+ps.i20[7][2]+r'''  \
       ´/  RECUPERACAO DE ENERGIA: '''+ps.i6[4]+r'''  |________________________/
       `\__________________________________|                        \
       ´/                                  |        PASSIVA         /
       `\         CLASSE DE ITENS          |________________________\
       ´/__________________________________|                        /
       `\                |                 |  '''+ps.i20[8][0]+r'''  \
       ´/   SUPERIORES   |   INFERIORES    |  '''+ps.i20[8][1]+r'''  /
       `\________________|_________________|  '''+ps.i20[8][2]+r'''  \
       ´/  '''+ps.i12[1]+r'''  |  '''+ps.i12[7]+r'''   |  '''+ps.i20[8][3]+r'''  /
       `\  '''+ps.i12[2]+r'''  |  '''+ps.i12[8]+r'''   |  '''+ps.i20[8][4]+r'''  \
       ´/  '''+ps.i12[3]+r'''  |  '''+ps.i12[9]+r'''   |  '''+ps.i20[8][5]+r'''  /
   _____\  '''+ps.i12[4]+r'''  |  '''+ps.i12[10]+r'''   |  '''+ps.i20[8][6]+r'''  \
 /´´´´´´/  '''+ps.i12[5]+r'''  |  '''+ps.i12[11]+r'''   |  '''+ps.i20[8][7]+r'''  /
||      \  '''+ps.i12[6]+r'''  |  '''+ps.i12[12]+r'''   |  '''+ps.i20[8][7]+r'''  \
\\      /________________|_________________|________________________/
 \\____/___________________________________________________________/
   ```´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´
''')

def tela_clases():
    clear()
    print(r'''
   _______________________________________________________________
 //````\___________________________________________________________\
//      \                                                           \
||      /                          CLASSES                          /
 \______\___________________________________________________________\
   `````/                                                           /
       `\                                                           \
       ´/  \___\___\___\___\___\___\    \___\___\___\___\___\___\   /
       `\  |                        |   |                        |  \
       ´/ \|          TANK          |  \|          XAMA          |  /
       `\  |  forca........: **     |   |  forca........: *      |  \
       ´/ \|  alcance......: *      |  \|  alcance......: ***    |  /
       `\  |  abilidades...: ***    |   |  abilidades...: ****   |  \
       ´/ \|  sobrevivencia: ****   |  \|  sobrevivencia: **     |  /
       `\  |________________________|   |________________________|  \
       ´/ \|                        |  \|                        |  /
       `\  |  PALADINO   GUERREIRO  |   |  MAGO      CURANDEIRO  |  \
       ´/ \|________________________|  \|________________________|  /
       `\  ´´´´´´´´´´´´´´´´´´´´´´´´´    ´´´´´´´´´´´´´´´´´´´´´´´´´   \
       ´/  \___\___\___\___\___\___\    \___\___\___\___\___\___\   /
       `\  |                        |   |                        |  \
       ´/ \|       PISTOLEIRO       |  \|          NINJA         |  /
       `\  |  forca........: ***    |   |  forca........: ****   |  \
       ´/ \|  alcance......: ****   |  \|  alcance......: *      |  /
       `\  |  abilidades...: **     |   |  abilidades...: **     |  \
       ´/ \|  sobrevivencia: *      |  \|  sobrevivencia: ***    |  /
       `\  |________________________|   |________________________|  \
       ´/ \|                        |  \|                        |  /
       `\  |  SNIPER      ARQUEIRO  |   |  LADINO      ASSASINO  |  \
       ´/ \|________________________|  \|________________________|  /
       `\  ´´´´´´´´´´´´´´´´´´´´´´´´´    ´´´´´´´´´´´´´´´´´´´´´´´´´   \
       ´/___________________________________________________________/
       `\                                                           \
       ´/  # Para ver as informacoes detalhadas de cada classe      /
       `\    digite: info 'nome da classe'                          \
       ´/___________________________________________________________/
   _____\                                                           \
 /´´´´´´/  # Cada classe tem 2 classes secundarias,                 /
||      \    que disponibilizam acesso a outras classes primarias   \
\\      /___________________________________________________________/
 \\____/___________________________________________________________/
   ```´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´
''')



def cx_texto(texto: str):

    buffer = ''
    print(r'''  ________________________________________________________________
 //````\___________________________________________________________\
//      \                                                           \
||      /  '''+add_spaces(texto,55)+r'''  /
 \______\___________________________________________________________\
   `````/                                                           /
   _____\                                                           \
 /´´´´´´/  ''',end='')
    buffer = input()
    print(r'''||      \                                                           \
\\      /___________________________________________________________/
 \\____/___________________________________________________________/
   ```´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´
''')
    input()
    return buffer

def opc_criacao():

    titl_criacao()
    ps.i20[0] = add_spaces(cx_texto('             Digite seu nome (20 letras): '),20)
    ps.i6[0] = add_spaces(str(randint(100000,999999)),6)
    
#'guerreiro','tank','paladino','curandeiro','chama','mago','arqueiro','pistoleiro','sniper','fuzileiro','ladino','assasino','ninja','espadachin'
    tela_clases()
    ps.i12[0] = add_spaces(cx_texto('                  Escolha sua classe: '),12)
    titl_criacao()
    tela_ficha()
opc_criacao()