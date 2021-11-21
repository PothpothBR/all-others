from characters import Player

def deldata(comand="all",name=""):
    if comand == "all":
        delete = open("cache.dt", "w")
        delete.write("")
        delete.close()
        return
    elif comand == "one":
        read = open("cache.dt", "r")
        buffer = read.readlines()
        read.close()
        cuted_buffer = []
        atual_line = 0
        while atual_line < len(buffer):

            if buffer[atual_line][4:] == name+'\n':
                print("nome econtrado",buffer[atual_line][4:])
                cuted_buffer = buffer[:atual_line-4]
                print("buffer apos corte",cuted_buffer)
                name = "none\n"
            elif buffer[atual_line] == ">>>><<<<\n":
                cuted_buffer += buffer[atual_line+1:]
                break

            atual_line+=1
        file = open("cache.dt","w")
        for i in cuted_buffer:
            file.write(i)
        return


def setdata(player):



    file = open("cache.dt", mode)
    file.write('\n<<<<>>>>\n')
    file.write('classe:' + player.CLASS + '\n')

    file.write('\nnome:' + player.ID +
               '\nnivel:' + str(player.LEVEL) +
               '\nxp:' + str(player.XP) +
               '\nmaestria:' + str(player.MASTERY) +
               '\nequipamento:' + str(player.EQUIPAMENTTYPE)+
               '\nmecanica:' + str(player.RANGETYPE)+
               '\nalcance:' + str(player.RANGE) +
               '\n')
    file.write("[valores\n")
    for v in list(player.VALUES.items()):
        file.write(v[0] + ':' + str(v[1]) + '\n')
    file.write("]\n")
    file.write("[recursos\n")
    for v in list(player.RESOURCES.items()):
        file.write(v[0] + ':' + str(v[1]) + '\n')
    file.write("]\n")
    file.write("[bolsa\n")
    for v in list(player.BAG.items()):
        file.write(v[0] + ':' + str(v[1]) + '\n')
    file.write("]\n")
    file.write('>>>><<<<')
    file.close()


def getvals(data: str):
    buffer = ''
    sec_buffer = ''
    c = 0
    while c < len(data):
        if data[c] == '\n': break
        buffer += data[c]
        if data[c] == ':':
            sec_buffer = buffer
            buffer = ''
        c += 1
    return tuple((sec_buffer, buffer))


def getdata():
    file = open("cache.dt", "r")
    data = file.readlines()
    file.close()

    buffer = []
    i = 0
    while i < len(data):
        sbuffer = []
        if data[i] == '\n': i+=1; continue
        data[i] = data[i][:-1]
        if data[i] == '<<<<>>>>':
            while i < len(data):
                i += 1
                if data[i][0:8] == '>>>><<<<': break
                if data[i][0] == '[':
                    conjunt = []
                    conjunt.append(data[i][1:-1])
                    while i < len(data):
                        i+=1
                        if data[i][0] == ']': break
                        conjunt.append(getvals(data[i]))
                    sbuffer.append(conjunt)
                else : sbuffer.append(getvals(data[i]))
        buffer.append(tuple(sbuffer))
        i += 1

    return buffer

def fomdata(data:list):
    pass
