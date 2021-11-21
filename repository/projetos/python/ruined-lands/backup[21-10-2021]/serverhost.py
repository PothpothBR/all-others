from network import ServerHost
from datalog import DataManager

# gera os recursos da data
dm = DataManager('config.dtm', 'server.log')

host = ServerHost(dm.data['network']['ip'], dm.data['network']['port'])
host.listen()

dm.shutdown()
