from sys import exit

# extai um valor da linha cortada
def extract_value(line):
    i = 0
    for c1 in line:
        if c1.isnumeric():
            e = 0
            isfloat = False
            for c2 in line[i:]:
                if not c2.isnumeric():
                    if c2 == '.' and not isfloat:
                        isfloat = True
                    else:
                        if isfloat:
                            return float(line[i:i+e])
                        else:
                            return int(line[i:i+e])
                elif i+e+1 == len(line):
                    if isfloat:
                        return float(line[i:])
                    else:
                        return int(line[i:])
                e += 1

        i += 1
        if c1 == '\'':
            e = 0
            for c2 in line[i:]:
                if c2 == '\'' and e > 1:
                    if line[i:i+e].lower() == 'false':
                        return False
                    elif line[i:i+e].lower() == 'true':
                        return True
                    return line[i:i+e]
                elif c2 == '\'':
                    return ''
                e += 1

        elif c1 == '[':
            e = 0
            items = list()
            for c2 in line[i:]:
                if c2 == ']':
                    for val in line[i:i+e].split(','):
                        extr = extract_value(val)
                        if extr:
                            items.append(extr)
                    return items
                e += 1


    return None

# extrai uma linha do arquivo e separa a chave e o valor
def extract_line(line: str):

    if not line:
        return None

    line = line.split(":")

    line[0] = extract_value(line[0])
    line[1] = extract_value(line[1])

    return line

# recebe um arquivo e extrai toda a sua data
# retorna um dicionario com os conjuntos de chave: valor
# valores podem ser dicionarios
def extract_data(data, index = 0, keyword=None):
    temp_data = {}
    i = index
    while i < len(data):
        pair = extract_line(data[i])

        if not pair:
            if(len(data) == 1):
                print("A data referida esta em branco, nada sera carregado!")
                break
            i += 1
            continue

        if keyword == pair[1] and not pair[0]:
            return temp_data, i

        if pair[1] is None:
            upfloor, i = extract_data(data, i+1, pair[0])

            temp_data.update({pair[0]: upfloor})
        else:
            temp_data.update({pair[0]: pair[1]})

        i += 1

    return temp_data

# recebe um data alocada e a monta e insere no arquivo de data
# o arquivo de data é sobrescrevido com a nova data
def mount_data(data, file, tabs = 0):

    # transforma a data em um par chave-valor por posicao
    data = tuple(data.items())

    index = 0

    # itera sobre os pares
    while(index < len(data)):
        file.write("{}'{}': ".format("    "*tabs, data[index][0]))

        if type(data[index][1]) == dict:
            tabs += 1
            file.write('\n')
            mount_data(data[index][1], file, tabs)
            tabs -= 1
            file.write("{}:'{}'\n".format("    "*tabs, data[index][0]))

        elif type(data[index][1]) == str:
            file.write("'{}'\n".format(data[index][1]))

        elif type(data[index][1]) == int or type(data[index][1]) == float:
            file.write("{}\n".format(str(data[index][1])))

        elif type(data[index][1]) == bool:
            if data[index][1]:
                file.write("'true'\n")
            else:
                file.write("'false'\n")

        elif type(data[index][1]) == list or type(data[index][1]) == tuple:
            file.write('[')
            i = 0
            data_len = len(data[index][1])
            while i < data_len:
                if type(data[index][1][i]) == str:
                    file.write("'{}'".format(data[index][1][i]))
                elif type(data[index][1][i]) == int or type(data[index][1][i]) == float:
                    file.write("{}".format(str(data[index][1][i])))
                elif type(data[index][1][i]) == bool:
                    if data[index][1][i]:
                        file.write("'true'")
                    else:
                        file.write("'false'")
                else:
                    file.write("'errortype'")
                    print("data corrompida, valor perdido...\nvalor: ", data[index][1][i])

                if i != data_len-1:
                    file.write(', ')
                i += 1
            file.write(']\n')
        else:
            file.write("'errortype'\n")
            print("data corrompida, valor perdido...\nvalor: ", data[index][1])

        index += 1


