from display_beauties import *
from datalog import DataManager
from creation import *

# carrega o banco de dados referente ao jogador
db_player = DataManager('player.data', 'data.log')


# menu principal
def menu():
    simple_box('Bem vindo '+db_player.data['name']+'!')
    simple_dict_list_box(['level', 'coins', 'localization', 'info'], db_player.data, 'status')


# rotinas de inicialização
def start():
    if not db_player.data:
        db_player.data = create_player()
        db_player.update_data()

    menu()


start()
db_player.shutdown()
