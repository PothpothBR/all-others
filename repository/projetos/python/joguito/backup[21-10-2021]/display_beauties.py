def simple_input(value, tab=''):
    return input('\n'+tab+'['+value+']> ')


def simple_input_list(values: list(), header='', tab='', error=''):
    option = ''
    print('\n' + tab + '[', end='')
    if header:
        print(header + ':')
    else:
        print()
    for i in values:
        print(tab + '    +' + i)
    while True:
        option = input(tab+']> ')
        if option not in values:
            if error:
                print(tab+' '+error)
        else:
            break

    return option


def simple_box(value, tab=''):
    print(tab+'+-', end='')
    for i in value:
        print('-', end='')
    print('-+')
    print(tab+'| '+value+' |')
    print(tab + '+-', end='')
    for i in value:
        print('-', end='')
    print('-+')


def simple_list_box(values, header='', tab=''):
    max_size = int()
    for i in values:
        if max_size < len(i):
            max_size = len(i)
    if header:
        if max_size < len(header):
            max_size = len(header)
        else:
            header += ' '*(max_size-len(header))
        simple_box(header, tab)
    else:
        print(tab+'+-', end='')
        for i in range(max_size):
            print('-', end='')
        print('-+')
    for i in values:
        print(tab+'| '+i+((max_size-len(i))*' ')+' |')
    print(tab + '+-', end='')
    for i in range(max_size):
        print('-', end='')
    print('-+')


def simple_dict_list_box(values, data, header='', tab=''):
    mod_values = list()
    for i in values:
        if ':' in i:
            i = i.split(':')
            if len(i) == 2:
                mod_values.append(i[0]+' '+i[1]+': '+str(data[i[0]][i[1]]))
            elif len(i) == 3:
                mod_values.append(i[0]+' '+i[1]+' '+i[2]+': '+str(data[i[0]][i[1]][i[2]]))
            elif len(i) == 4:
                mod_values.append(i[0]+' '+i[1]+' '+i[2]+' '+i[3]+': '+str(data[i[0]][i[1]][i[2]][i[3]]))
            else:
                mod_values.append('not supported tree depth length')
        else:
            mod_values.append(i+': '+str(data[i]))

    simple_list_box(mod_values, header, tab)
