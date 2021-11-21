import socket


# classe para conexao servidor - cliente, sendo esse o lado do cliente
class ClientHost:
    # tenta uma conexao com o servidor
    def __init__(self, ip: chr, port: int):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    # libera os sockets apos termino de uso
    def __del__(self):
        self.connection.close()

    # envia dados para a conexao
    def send(self, data):
        self.connection.send(data.encode())

    # recebe dados da conexao
    def recv(self):
        return self.connection.recv(4096).decode()


# classe para conexao servidor - cliente, sendo esse o lado do servidor
class ServerHost:
    # linka o socket
    def __init__(self, ip: chr, port: int):
        print('    iniciando servidor...')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip, port))
        self.socket.listen()
        self.connection = list()
        self.conn_addr = list()
        self.conn_len = 0

    # libera os sockets apos termino de uso
    def __del__(self):
        self.socket.close()

    # aguarda ate haver uma conexao, e retorna o id da mesma
    def listen(self) -> int:
        print('    aguardando pedido de conexao...')
        (connection, conn_addr) = self.socket.accept()
        self.connection.append(connection)
        self.conn_addr.append(conn_addr)
        self.conn_len += 1

        return self.conn_len-1

    # envia dados para a conexao especifica
    def send(self, index, data):
        self.connection[index].send(data.encode())

    # recebe dados da conexao especifica
    def recv(self, index):
        return self.connection[index].recv(4096).decode()
