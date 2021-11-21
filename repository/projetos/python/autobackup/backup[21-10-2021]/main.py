# automatizador de backup por BRUNO DALLAGNOL
# criado: 6/11/2020
# ultima modificacao: 6/11/2020

# sistema de ierarquia de pastas nessesario:
# 
# ["sua pasta"]
#    +[backup"mes"-"dia"("seu complemento")]
#    +[lastest]
#        +"seu arquivo"

from sysconfig import shell
from format import inputf, printmsgf, printinfof
from backup import backup
from sys import argv as options
from logdata import get_name_value

def menu():
    command = inputf("Comando")
    if command == "clear":
        shell.clear()
    elif command == "help":
        printinfof("auto", "automatiza uma operacao")
        printinfof("clear init", "limpa a tela ao iniciar", 1)
        printinfof("clear exit", "limpa a tela ao sair", 1)
        printinfof("help", "mostra esta tela de ajuda")
        printinfof("exit", "sai do programa")
        printinfof("clear", "limpa a tela")
    elif command == "exit":
        return
    elif command:
        pass


    menu()
    
def init():
    if len(options) <= 1:
        printmsgf("Aviso", "Suas acoes estao sendo gravadas!")
        menu()
    elif len(options) > 2:
        printinfof("Erro","Somente 1 comando é permitido! rode \"autobackup help\" para uma lista de comandos.")
    else:
        pass

