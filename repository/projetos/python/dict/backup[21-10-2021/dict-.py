#atributos do programa
#
#abre multiplos arquivos com escola de uso do cache padrao
#sistema de limpar tela
#sistema de busca simples
#linguagem de marcacao propria
#sistema de adaptacao para cada sistema operacional
#formato de entrada parecido com o do terminal
#sistema de exibcao de chaves
#mini tutorial de criar biblioteca
#extensao propria .dic
#formato compativel com terminal
#sistema simples para multiplas chaves para uma unica descrisao

import os
import platform as plt
import sys

if plt.system() == 'Windows':
    cleart = 'cls'
elif plt.system() == 'Linux':
    cleart = 'clear'
else:
    cleart = 'clear'

def clearscreen():
    print()
    os.system(cleart) or None
    print()
    return

def start():
    string = input(' (dict:V-1.2.9)---> ')
    print()
    return string


deep = [
    ['''
    !!!!!voce invocou o bibliotecario!!!!!:
    
                          \\___________/
                            O       O
                             _______
                        |_______________|
                            |       |
                            |       |
            
        eu lhe ensinarei a criar uma biblioteca:
            
            a sintaxe basica é:
                key:
                    aqui vao as suas chaves de busca
                desc:
                    aqui vai a referencia sobre a sua chave de busca
                key:
                    ...
                desc:
                    ...
                end:
                    o end serve para marcar o fim do codigo
                
                -> qualquer coisa antes ou depois desse bloco
                 é considerado um comentario
                -> nao use muitas keys para uma unica descrição,
                 isso sobrecarrega a pilha
                -> as palavras reservadas key: desc: esc: sao 
                escritas sozinhas na linha e nao podem ser usadas
                 a outro proposito
                 
            keys padrao:
                -> exit sai
                -> clearon inicia o sistema de limpar tela utomaticamente
                -> clearoff desliga
                -> clear limpa a tela
                -> help ensina como faser uma biblioteca
                -> keys mostra todas as chaves de busca do programa
            
            flag -add:
                se usada adiciona dicionarios alem do padrao
                se nao usada substitui o dicionario padrão
    '''],
    [
            '''
chaves do sys:
     exit     - sai
     clearon  - inicia o sistema de limpar tela utomaticamente
     clearoff - desliga    
     clear    - limpa a tela             
     keys     - mostra todas as chaves de busca do programa
     refresh  - adiciona modificacoes do cache externo ao buffer de leitura
     reload   - reinicia o buffer de leitura
     
chaves de bibliotecas:'''
    ]
        ]

deepcc = {
    'help': deep[0]
}

def opencache(cacheopn:str):
    cache = open(cacheopn, 'r')
    deepcc = {'help': deep[0]}
    key = []
    desc = []
    buffer = cache.readline()
    while True:
        if buffer == 'key:\n':
            key = []
            blank = 0
            while True:
                buffer = cache.readline()[:-1]
                for i in buffer[:]:
                    if i == ' ':
                        blank = blank+1
                    else:
                        break
                if buffer != 'desc:':
                    key.append(buffer[blank:])
                    blank=0
                else:
                    break
        elif buffer == 'desc:':
            desc = []
            dbuffer = ''
            while True:

                buffer = cache.readline()
                if buffer == 'end:':
                    break
                if buffer == 'end:\n':
                    break

                if buffer != 'key:\n':
                    dbuffer = dbuffer + buffer
                else:
                    break
            desc.append(dbuffer)
        else:
            buffer = cache.readline()[:-1]
        for itrt in key[:]:
            ext = {itrt: desc}
            deepcc.update(ext)
        if buffer == 'end:':
            break
        if buffer == 'end:\n':
            break
    cache.close()
    return deepcc


def loadcache():
    global deepcc
    if len(sys.argv) > 1:
        if sys.argv[1] != '-add':
            for i in range(1,len(sys.argv)):
                if sys.argv[i][-4:] == '.dic':
                    deepcc.update(opencache(sys.argv[i]))
        elif sys.argv[1] == '-add':
            for i in range(2,len(sys.argv)):
                if sys.argv[i][-4:] == '.dic':
                    deepcc.update(opencache(sys.argv[i]))
            deepcc.update(opencache('R:\\venv\dict.dic'))
    else:
        pass
        deepcc.update(opencache('R:\\venv\dict.dic'))
    return None

clearauto = False

def search(buff: str = '') -> str:
    global clearauto
    global deepcc
    exit = True
    print()
    if buff == 'keys':
        print('chaves de busca cadastradas:')
        print(deep[1][0])
        for i in deepcc:
            print('    ',i)
    elif buff == 'clear':
        clearscreen()
    elif buff == 'clearon':
        clearauto = True
    elif buff == 'clearoff':
        clearauto = False
    elif buff == 'exit':
        exit = False
    elif buff == 'refresh':
        loadcache()
    elif buff == 'reload':
        deepcc = {}
        loadcache()
    else:
        if buff == '':
            for i in deepcc:
                print(i,':')
                for it in deepcc[i]:
                    print(it)

        elif deepcc.keys().__contains__(buff):
            for i in deepcc.items():
                if i.__contains__(buff):
                    for it in range(len(i[1])):
                        print(i[1][it])
        else:
            print(' \tchave de busa errada!\n\ttente keys para ver as chaves de busca validas.\n')
    if plt.system() == 'Windows':
        if clearauto == True:
            if exit == True:
                print()
                os.system('pause')
                clearscreen()
    elif plt.system() == 'Linux':
        if clearauto == True:
            if exit == True:
                print('\nPressione enter para continuar. . . ')
                input()
                clearscreen()
    print()
    return exit

#aqui ocorre a execusao do codigo

loadcache()
while search(start()):
    pass
