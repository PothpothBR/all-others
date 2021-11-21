from timer import strdate
from dataformat import extract_data, mount_data
import status

# classe para o gerenciamento de dados
# tem um log que registra os acessos e modificações a data
class DataManager:

    # o nome da data deve seguir o padrao unix de caminho '/'
    # todas as ações sao arquivadas no arquivo de log
    # o dev pode acressentar logs com o metodo log_write()
    def __init__(self, data_file, log_file):
        print("\n    Iniciando gerenciamento de dados em {}...".format(strdate()))
        self.data = {}
        self.dataFile = data_file
        self.logFile = log_file
        self.strId = data_file.split('/')[-1]
        print("    realizando check-in...")
        self.log_write("realizando check-in")
        print("    carregando data...")
        self.load_data()

    # encerra o gerenciamento de dados
    def shutdown(self):
        print("    Encerrando gerenciamento de dados em {}...".format(strdate()))
        print("    atualizando data...")
        self.update_data()
        print("    realizando check-out...")
        self.log_write("realizando check-out")

    # escreve um registro no arquivo de log
    # o id e a data sao incluidos automaticamente
    def log_write(self, log, endl = False):
        # abre o arquivo de log e informa algo
        try:
            file = open(self.logFile, "a")

        except:
            print("    arquivo de log nao encontrado, criando novo log...")
            file = open(self.logFile, "w")
            file.write("<{}> criou o log em {}\n".format(self.strId, strdate()))

        file.write("<{}> {} em {}\n".format(self.strId, log, strdate()))
        file.close()

    # carrega a data, se nao houver uma, crie-a
    def load_data(self):
        self.log_write("carregando data")
        # carrega os dados do programa
        try:
            file = open(self.dataFile, "r")

        except:
            print("    arquivo de dados nao encontrado, criando nova data...")
            self.log_write("nao encontrou a data, criando nova data")
            file = open(self.dataFile, "w+")

        temp_data = file.read().split('\n')
        file.close()

        self.data = extract_data(temp_data)

    # recarrega a data
    def reload_data(self):
        self.log_write("recarregando data")
        # carrega os dados do programa
        self.load_data()

    # aumenta a data com um novo arquivo
    # nunca testei, agora o porque? preguica...
    def plus_data(self, data_file):
        self.log_write("acressentando {} a data".format(data_file))

        # carrega os dados do programa
        try:
            file = open(data_file, "r")

        except:
            print("    arquivo de dados nao encontrado, criando nova data...")
            self.log_write("nao encontrou a data, criando nova data")
            file = open(data_file, "w+")

        temp_data = file.read().split('\n')
        file.close()

        self.data.update(extract_data(temp_data))

    # salva a data ja carregada
    # cuidado! isso sobrescreve a data
    def update_data(self):
        self.log_write("atualizando data")

        # salva os dados no arquivo
        try:
            file = open(self.dataFile, "w+t")

        except:
            print("    arquivo de dados nao encontrado, criando nova data...")
            self.log_write("nao encontrou a data, criando nova data")
            file = open(self.dataFile, "w+t")

        mount_data(self.data, file)
        if status.status():
            status.report(1, 'DataManager.update_data()')
            self.log_write("data corrompida, nada sera salvo")
            print("    data corrompida, nada sera salvo...")
