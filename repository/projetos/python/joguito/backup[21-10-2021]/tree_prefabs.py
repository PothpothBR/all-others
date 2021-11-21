# bases de construção dos objetos
player_base = {
    'name': str(),
    'level': int(),
    'hp': int(),
    'lucky': int(),
    'defense': int(),
    'velocity': int(),
    'inventory': dict(),
    'passives': list(),
    'info': str()
}
power_base = {
    'power': {
        'mana': int(),
        'energy': int()
    },
    'regeneration': {
        'mana': int(),
        'energy': int(),
        'hp': int()
    }
}
application = {
    'right': int(),  # dano imediato
    'continuum': {  # dano aplicado em turnos
        'tick': int(),  # dano
        'count': int()  # numero de turnos
    }
}
attack_base = {
    'damage': application.copy(),
    'strength': int(),
    'critic': int(),
    'life steal': int()
}
modifier = {
    'xp': int(),
    'lucky': int(),
    'defense': int(),
    'velocity': int()
}
modifier.update(attack_base.copy())
modifier.update(power_base.copy())

mechanic = {
    'heal': {
        'self': application.copy(),
        'friend': application.copy()
    },
    'cc': {
        'stun': int(),
        'slow': int(),
        'weak': modifier.copy()
    },
    'effect': modifier.copy()
}

# player
complete_player = {
    'xp': int(),
    'clothes': {
        'head': str(),
        'body': str(),
        'hands': str(),
        'legs': str(),
        'foots': str()
    },
    'weapons': {
        'left hand': str(),
        'right hand': str()
    },
    'abilities': list(),
    'localization': str(),
    'coins': int()
}
complete_player.update(player_base.copy())
complete_player.update(power_base.copy())
complete_player.update(attack_base.copy())

# pets e seguidores
simple_player = {
    'xp': int(),
    'weapon': str(),
    'ability': mechanic.copy(),
}
simple_player.update(player_base.copy())
simple_player.update(power_base.copy())
simple_player.update(attack_base.copy())

# mobs passivos
passive_mob = player_base.copy()

# mobs agressivos / inimigos
aggressive_mob = {
    'weapon': str(),
    'ability': str(),
}
aggressive_mob.update(player_base.copy())
aggressive_mob.update(attack_base.copy())

# objetos em geral
inanimate_object = {
    'name': str(),
    'level': str(),
    'value': int(),
    'minimum level': int(),
    'weight': float(),
    'trade': bool(),
    'stack': int(),
    'info': int()
}

# equipamentos de combate em geral
equipment = inanimate_object.copy()
equipment.update(mechanic.copy())

local_core = {
    'level': int(),
    'difficulty': str(),
    'infection': str(),
    'history': str(),
    'progress': int()
}

islands = {
    'north island': {
        'source of corruption': local_core.copy()
    },
    'savage lands': {
        'north tribe': local_core.copy(),
        'south tribe': local_core.copy(),
        'akanauans': local_core.copy(),
        'desert plain': local_core.copy()
        },
    'green piece': {
        'corruption': local_core.copy(),
        'land of mad wanderers': local_core.copy(),
        'gentle wind': local_core.copy(),
        'barbarians ruins': local_core.copy(),
        'elven ruins': local_core.copy(),
        'calm down': local_core.copy()
    }
}


def show_tree(tree_dict: dict, tab_len=0):
    for i in tree_dict.items():
        print('\n'+'    '*tab_len+i[0]+': ', end='')
        if type(i[1]) == dict:
            tab_len += 1
            show_tree(i[1], tab_len)
            tab_len -= 1
        elif type(i[1]) == list:
            for e in i[1]:
                print('    '*tab_len+str(i[1][e]))
        else:
            print(i[1], end='')
    print()
