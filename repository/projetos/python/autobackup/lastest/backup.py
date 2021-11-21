from format import printmsgf
from sysconfig import shell
from logdata import logf
from os import path

# realiza o backup de um diretorio
def backup(directory, backup_dir):
    if path.exists(directory):
        # faser verificacao se  ja existe outro arquivo com o mesmo nome
        shell.cd(directory)
        shell.mkdir(backup_dir)
        shell.copy("lastest", backup_dir)
        logf()
        printmsgf("backup", backup_dir)
    else :
        printmsgf("inexistente", directory)

