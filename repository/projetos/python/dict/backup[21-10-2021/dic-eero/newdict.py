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
    string = input('(V-2.0.1)> ')
    print()
    return string


class Deepcc:  # classe ainda nao implementada
    deepD = []
    deepK = []
    deepKM = []

    def setK(self, key: str):
        if key in self.deepK:
            pass
        else:
            self.deepK.append(key)
        return self.deepK

    def setD(self, desc: str):
        if desc in self.deepD:
            pass
        else:
            self.deepD.append(desc)
        return self.deepD

    def setKM(self,KeyMaster: str,referencekeys: str):
        #for i
        pass

    def verifyK(self, key: str):
        if key in self.deepK:
            for i in self.deepK:
                if i == key:
                    return True
        else:
            for i in self.deepK:
                if type(i) == list:
                    if key in i:
                        return True
        return False

    def searchK(self, key: str):
        '''retorna a posicao da chave no vetor, se nao houver chave retorna -1'''
        count = 0
        if key in self.deepK:
            for i in self.deepK:
                if i == key:
                    break;
                count += 1
        else:
            for i in self.deepK:
                if key in i:
                    break
                count +=1

        return count

    def searchD(self, key: str):
        '''retorna a posicao da descricao no vetor, se nao houver descricao retorna -1'''
        count = 0
        if key in self.deepD:
            for i in self.deepD:
                count += 1
                if i == key:
                    break;
        else:
            count = -1
        return count

    def getDbyK(self, key, keyM = 0):
        if type(key) == int:
            return self.deepD[key][keyM]
        elif type(key) == str:
            return self.deepD[self.searchK(key)]
        else:
            return -1

    def getKbyK(self, key: str):

        return -1


tdeepcc = Deepcc()

deep = ['''
            ----------------------------------------------------
            |               Programa feito por                 |
            |  [Bruno Dalagnol] [15 09 2019] [versao:2.0.1]    |
            ----------------------------------------------------

                    !!!!!voce invocou o bibliotecario!!!!!:

                          /\\         /\\       ___ 
                         /--\\_______/--\\     / __| 
                         |  O       O  |    / /   eu lhe ensinarei
                         |    __Y__    |   / /         a criar uma biblioteca:
                         \_____________/  / /
                            |  _____   \ / /
                            |           \ /
                            |  |--|  |\  |
                            |__||_|__||__|


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
    ''',
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

def opencache(cacheopn: str):
    print('            Carregando dicionario, ', end='')
    cache = open(cacheopn, 'r')
    tdeepcc.setK('help')
    tdeepcc.setD(deep[0])
    keys = []
    keysM = []
    desc = ''
    buffer = cache.readline()
    line = 1
    while True:
        add = True
        def coment(buffer: str):
            blank = 0
            stop = False
            for i in buffer[:]:
                if i == ' ':
                    blank = blank + 1
                else:
                    break
            blankbf = buffer[blank:]
            if blankbf[0:2] == '!#':
                stop = True
            return stop

        if coment(buffer): buffer = cache.readline(); line += 1; continue
        
        if buffer == 'key:\n':

            blank = 0
            while True:
                buffer = cache.readline()[:-1]
                line += 1;
                if buffer == '': continue
                if coment(buffer): buffer = cache.readline(); line += 1; continue

                for i in buffer[:]:
                    if i == ' ':
                        blank = blank + 1
                    else:
                        break
                    
                if len(buffer) == blank:
                     blank = 0
                elif buffer != 'desc:':
                    keys.append(buffer[blank:])
                    blank = 0
                else:
                    break


        elif buffer == 'desc:':
            dbuffer = ''
            while True:
                buffer = cache.readline()
                line += 1;
                if coment(buffer): buffer = cache.readline(); line += 1; continue

                if buffer == 'end:':
                    break
                if buffer == 'end:\n':
                    break

                if buffer == 'master:\n':
                    break

                if buffer != 'key:\n':

                    dbuffer = dbuffer + buffer
                else:
                    break
            desc = dbuffer

        elif buffer == 'master:\n':
            blank = 0
            while True:
                buffer = cache.readline()[:-1]
                line += 1;
                if buffer == '': continue
                if coment(buffer): buffer = cache.readline(); line += 1; continue

                for i in buffer[:]:
                    if i == ' ':
                        blank = blank + 1
                    else:
                        break

                if len(buffer) == blank:
                    blank = 0
                elif buffer != 'keys:':
                    keys.append(buffer[blank:])
                    blank = 0
                else:
                    break

        elif buffer == 'keys:\n':

            blank = 0
            while True:
                buffer = cache.readline()[:-1]
                line += 1;
                if buffer == '': continue
                if coment(buffer): buffer = cache.readline(); line += 1; continue

                for i in buffer[:]:
                    if i == ' ':
                        blank = blank + 1
                    else:
                        break

                if len(buffer) == blank:
                    blank = 0
                elif buffer != 'end':
                    if buffer != 'end:':
                        keysM.append(buffer[blank:]) # terminar aqki
                        blank = 0
                else:
                    break

            if buffer == 'end':
                break
            if buffer == 'end:':
                break

        else:
            buffer = cache.readline()
            line += 1;
            add = False

        if len(keys) == 1:
            keys = keys[0]

        if add:
            if desc != '':
                tdeepcc.setK(keys)
                tdeepcc.setD(desc)
                keys = []
                desc = ''
            #elif keyM != []:
                #tdeepcc.setKM(keys)
        if buffer == 'end':
            break
        if buffer == 'end:':
            break
        if buffer == 'end:\n':
            break

    cache.close()
    print(line, 'Linhas lidas...')
    return #implement future

def loadcache():
    if len(sys.argv) > 1:
        if sys.argv[1] != '-add':
            for i in range(1, len(sys.argv)):
                if sys.argv[i][-4:] == '.dic':
                    opencache(sys.argv[i])
        elif sys.argv[1] == '-add':
            for i in range(2, len(sys.argv)):
                if sys.argv[i][-4:] == '.dic':
                    opencache(sys.argv[i])
                else:
                    print('            Formato do dicionario "%s" invalido...' % (sys.argv[i]))
            opencache('C:/hd-extra-[salvo]/venv/dict.dic')
    else:
        pass
        opencache('C:/hd-extra-[salvo]/venv/dict.dic')
    return None

clearauto = False

def newsearch(buff: str = '') -> str:
    global clearauto
    exit = True
    print()
    if buff == 'keys':
        print('chaves de busca cadastradas:')
        print(deep[1])
        for i in tdeepcc.deepK:
            if type(i) == str:
                print('    ', i)
            else:
                for it in i:
                    print('     |%s' %(it))
        print()

    elif buff == 'clear':
        clearscreen()
    elif buff == 'clearon':
        clearauto = True
    elif buff == 'clearoff':
        clearauto = False
    elif buff == 'exit':
        exit = False

    else:
        if buff == '':
            for i in range(len(tdeepcc.deepK)):
                print(tdeepcc.deepK[i], ':')
                print(tdeepcc.deepD[i])

        elif tdeepcc.verifyK(buff):
            print(tdeepcc.getDbyK(buff))

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

# aqui ocorre a execusao do codigo

print('''\n
            ----------------------------------------------------
            |               Programa feito por                 |
            |  [Bruno Dalagnol] [15 09 2019] [versao:2.0.1]    |
            ----------------------------------------------------

            !!!!!voce invocou o bibliotecario!!!!!:

                          /\\         /\\       ___
                         /--\\_______/--\\     /  _| 
                         |  Y       Y  |    / /
                         |    ==T==    |   / /
                         \_____________/  / /
                            |  _____   \ / /
                            |           \ /
                            |  |--|  |\  |
                            |__||_|__||__|
            ----------------------------------------------------
            ''')

loadcache()
print('            Iniciando programa...')
print('            ----------------------------------------------------')
while newsearch(start()):
    pass
