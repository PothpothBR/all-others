from tree_prefabs import *
from display_beauties import *


def create_player():
    data = complete_player.copy()
    data['localization'] = 'gentle wind'
    simple_box('criação de jogador', '\t')
    data['name'] = simple_input('nome')
    option = simple_input_list(['ataque', 'defesa', 'suporte', 'controle'], 'proeficiência', '', 'opção inválida!')

    if option == 'ataque':
        data['hp'] = 200
        data['strength'] = 20
        data['lucky'] = 0.02
        data['defense'] = 5
        data['velocity'] = 20
        data['power']['mana'] = 50
        data['power']['energy'] = 200
        data['regeneration']['mana'] = 5
        data['regeneration']['energy'] = 80
        data['regeneration']['hp'] = 5
        data['damage']['right'] = 80
        data['damage']['continuum']['tick'] = 2
        data['damage']['continuum']['count'] = 2
        data['critic'] = 0.5
        data['life steal'] = 0.02

    elif option == 'defesa':
        data['hp'] = 800
        data['strength'] = 20
        data['lucky'] = 0.02
        data['defense'] = 20
        data['velocity'] = 5
        data['power']['mana'] = 50
        data['power']['energy'] = 80
        data['regeneration']['mana'] = 5
        data['regeneration']['energy'] = 20
        data['regeneration']['hp'] = 20
        data['damage']['right'] = 5
        data['damage']['continuum']['tick'] = 0
        data['damage']['continuum']['count'] = 0
        data['critic'] = 0.08
        data['life steal'] = 0.08

    elif option == 'suporte':
        data['hp'] = 500
        data['strength'] = 20
        data['lucky'] = 0.2
        data['defense'] = 5
        data['velocity'] = 20
        data['power']['mana'] = 500
        data['power']['energy'] = 20
        data['regeneration']['mana'] = 20
        data['regeneration']['energy'] = 2
        data['regeneration']['hp'] = 5
        data['damage']['right'] = 5
        data['damage']['continuum']['tick'] = 2
        data['damage']['continuum']['count'] = 8
        data['critic'] = 0.08
        data['life steal'] = 0.2

    elif option == 'controle':
        data['hp'] = 200
        data['strength'] = 50
        data['lucky'] = 0.5
        data['defense'] = 20
        data['velocity'] = 8
        data['power']['mana'] = 200
        data['power']['energy'] = 80
        data['regeneration']['mana'] = 20
        data['regeneration']['energy'] = 8
        data['regeneration']['hp'] = 2
        data['damage']['right'] = 8
        data['damage']['continuum']['tick'] = 5
        data['damage']['continuum']['count'] = 2
        data['critic'] = 0.2
        data['life steal'] = 0.2

    data['info'] = simple_input('your history')

    simple_box(data['name'], '\t')
    simple_dict_list_box(['hp', 'damage:right', 'critic', 'defense', 'velocity', 'lucky'], data, '\t')
    return data
