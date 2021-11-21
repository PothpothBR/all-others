from os import system
from platform import system as version

# de acordo com o sistema operacional cria uma classe para comandos de terminal
if version() == "Windows":
    class shell:
        cd = lambda arg: system("cd \"{}\"".format(arg))
        mkdir = lambda arg: system("mkdir {}".format(arg))
        copy = lambda arg1, arg2: system("xcopy {} {} /E /Q /H /Y".format(arg1, arg2))
        clear = lambda : system("cls") or None
    char = {'/' : '\\'}
elif version() == "Linux":
    class shell:
        cd = lambda arg: system("cd \"{}\"".format(arg)) or None
        mkdir = lambda arg: system("mkdir {}".format(arg)) or None
        copy = lambda arg1, arg2: system("cp -r {} {}".format(arg1, arg2)) or None
        clear = lambda : system("clear") or None
    char = {'/' : '/'}
