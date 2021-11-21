from os import system as sys
from characters import Player, Atributes
from platform import system
from data import setdata, getdata
clear_by_system = system()

if clear_by_system == "Windows":
    clear_by_system = "cls"
elif clear_by_system == "Linux":
    clear_by_system = "clear"


# limpa a tela
def cls():
    sys(clear_by_system) or None