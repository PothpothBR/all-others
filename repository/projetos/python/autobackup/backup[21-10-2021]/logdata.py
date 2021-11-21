from os import path
from sysconfig import shell

# vetor para armazenar os logs
logs = []
# funcao para inserir um log com pequena armonizacao grafica e data
logf = lambda log: logs.append(" [{} {}] {}".format(date, time, log))
# igual logf, so que insere no inico do vetor
logf_first = lambda log: logs.insert(0, " [{} {}] {}".format(date, time, log))

# gera um arquivo de log com informacoes sobre o backup na pasta do backup
def backup_log(directory):
    logf_first("logs of backup")
    if not path.exists("{}{}backup_logs".format(directory, char['/'])):
        shell.mkdir(directory+"\\backup_logs")
        logf_first("log directory created")
        
    log_file = open("{}{}backup_logs{}backup[{}].log".format(directory,char['/'],char['/'],date),'w')
    for i in logs:
        log_file.write("{}{}".format(i,'\n'))
    log_file.close()

def get_name_value(line):
    name = ""
    value = ""
    for i in range(len(line)):
        if line[i] != ':':
            name += line[i]
        else:
            for e in range(i + 2, len(line)):
                if line[e] != '\n':
                    value += line[e]
                else:
                    break
            break
    return [name, value]


#manipula os dados de backup
class data:
    if not path.exists("data"):
        shell.mkdir("data")
    if not path.isfile("data/backup.data"):
        open("data/backup.data", 'x').close()
    
    def new_data(directory):
        data_file = open("data/backup.data","w")
        data_file.write('\n')
        data_file.write("@data\n")
        data_file.write("name: {}\n".format(get_last_dir(directory)))
        data_file.write("directory:{} \n".format(directory))
        data_file.write("created: {} {}\n".format(date, time))
        data_file.write("backups: 0\n")
        data_file.write("last: {} {}\n".format(date, time))
        data_file.close()

    def mod_data(vals):
        pass

    def get_data(name):
        data_file = open("data/backup.data","r")
        buffer = data_file.readlines()
        data_val = []
        for i in range(len(buffer)):
            if buffer[i] == "@data\n":
                for e in range(1, 6):
                    val = get_name_value(buffer[i+e])
                    data_val.append({val[0]: val[1]})
        return data_val
                


    