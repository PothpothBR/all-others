from time import strftime, localtime

# retorna o ultimo diretorio de um caminho de diretorios
def get_last_dir(file):
    tmp = ''
    for i in file[::-1]:
        if i != '/' and i != '\\':
            tmp += i
        else:
            break
    return tmp[::-1]

# coleta uma string com pequena armonizacao grafica
inputf = lambda string: input(" [{}]> ".format(string))

# printa uma mensagem com pequena armonizacao grafica
printmsgf = lambda string, value = '': print(" [{}]: {}".format(string, value))

# printa uma informacao com pequena armonizacao grafica e ierarquia
printinfof = lambda string, value = '', ierarchy = 0: print("{} <{}> {}".format(ierarchy * "   +", string, value))
# string com a data atual separada por '-' e a hora separada por ':'
date, time = strftime("%Y-%m-%d %H:%M:%S", localtime()).split()

# coleta os dados para faser o backup:
#   + caminho da pasta de backup
#   + complemento para o nome da pasta de backup
get_data = lambda : [inputf("caminho"), "backup[{}]{}".format(date, (lambda x: "("+x+")" if x != "" else "")(inputf("complemento")))]
