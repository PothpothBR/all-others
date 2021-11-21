from characters import Character as c
from player import Player as p

def setdata(player):
    file = open("cache.dt", "w")
    file.write('<<<<>>>>\n')
    file.write('class:'+player.CHARACTER.CLASS+'\nname:'+player.ID+'\n')
    for v in list(player.VALUES.items()):
        file.write(v[0]+':'+str(v[1])+'\n')

    for v in list(player.RESOURCES.items()):
        file.write(v[0]+':'+str(v[1])+'\n')

    for v in list(player.BAG.items()):
        file.write(v[0]+':'+str(v[1])+'\n')

    file.write('level:'+str(player.LEVEL)+'\nxp:'+str(player.XP)+'\nmaestry:'+str(player.MASTERY))
    file.write('\n>>>><<<<')


def getdata():
    file = open("cache.dt","r")
    data = file.readlines()
    file.close()

    buffer = []
    i=0
    while(i < len(data)):
        sbuffer = []
        data[i] = data[i][:-1]
        if data[i] == '<<<<>>>>':
            while (i < len(data)):
                i += 1
                if data[i] == '>>>><<<<\n' or data[i] == '>>>><<<<': break
                bffr = ''
                sbffr = ''
                c = 0
                while(c < len(data[i])):
                    if data[i][c] == '\n': break
                    bffr += data[i][c]
                    if data[i][c] == ':':
                        sbffr = bffr
                        bffr = ''
                    c+=1
                sbuffer.append((sbffr,bffr))
        buffer.append(tuple(sbuffer))
        i+=1


    return buffer


cc=c(['classname',00,11,22,33,44,55,66,77,88,99])

pp=p('playername',cc)

setdata(pp)

dataf = getdata()

for i in dataf:
    print(i)