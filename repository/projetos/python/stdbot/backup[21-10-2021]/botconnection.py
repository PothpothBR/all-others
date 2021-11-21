# para dados basicos <nome do bot> <porta do servidor> <info de status>
from sys import argv

net_info = {}

if len(argv) > 1:
    for i in range(1, len(argv), 2):
        if argv[i].lower() == "-ip":
            net_info.update({"ip": argv[i+1]})
        elif argv[i].lower() == "-port":
            net_info.update({"port": int(argv[i+1])})
        elif argv[i].lower() == "-type":
            if argv[i+1].lower() == "server":
                net_info.update({"type": 2002})
            elif argv[i+1].lower() == "client":
                net_info.update({"type": 1001})
            else:
                print("    valor inserido invalido",argv[i+1])
        elif argv[i].lower() == "-help":
            print("""
    [-ip] o ip do host
    [-port] a porta a ser hosteada
    [-type] o tipo de conexao: <client | server>
    [-help] exibe essa ajuda
""")
        else:
            print("    tipo inserido invalido:", argv[i])
            print("    tente -help para obter ajuda")


# importa o sistema de conexao
import socket

# macros para definir tipo de conexao
CLIENT = 1001
SERVER = 2002

# classe para criar e gerenciar a conexão
class Network:

    # IP - PORTA - TIPO__DE_CONEXAO
    def __init__(self, ip: str, port: int, type: int):
        if type == CLIENT:
            print("    conectando", ip, port, "...")
            self.socket = socket.create_connection((ip, int(port)))

            print("    testando conexao -> ", end="")
            result = self.recv()
            self.send(1, result[1])
            if result[1] == "1234567890987654321, this is a beautiful and loooong text":
                print("sucesso")
            else:
                print("falha")

        elif type == SERVER:
            self.connect_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            self.connect_socket.bind((ip, int(port)))
            print("    aguardando conexao", ip, port, "...")
            self.connect_socket.listen(1)
            self.socket, self.adrr_info = self.connect_socket.accept()

            print("    testando conexao -> ", end="")
            self.send(0, "1234567890987654321, this is a beautiful and loooong text")
            result = self.recv()
            if result[1] == "1234567890987654321, this is a beautiful and loooong text":
                print("sucesso")
            else:
                print("falha")
        else:
            print("    tipo de conexão invalida")

    # envia dados
    # envia o id
    # recebe um valor de confirmação que o id ja foi enviado
    # envia a data
    def send(self, id: int, data = "None"):
        self.socket.sendall(str(id).encode("ascii"))
        self.socket.recv(1)
        self.socket.sendall(data.encode("ascii"))

    # recebe o id
    # envia um valor de confirmação que a data foi recebida
    # recebe o resto da data
    def recv(self):
        _id = self.socket.recv(7).decode()
        self.socket.send('0'.encode("ascii"))
        data = self.socket.recv(4096).decode()
        return (int(_id), data)

    # ao finalizar encerra o socket
    def __del__(self):
        print("    conexao encerrada")
        self.socket.close()

net = None

if net_info:
    net = Network(net_info['ip'], net_info['port'], net_info['type'])