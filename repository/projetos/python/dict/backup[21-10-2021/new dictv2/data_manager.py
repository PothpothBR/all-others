
import format_strings

class file(object):
    
    file = 0
    lines = 0
    type = ''
    cript = ''
    errors = []
    debug = []

    keys = []
    descriptions = []
    masterkey = []
    subjectkeys = []

    def __init__(self,file):
        self.file = open(file)

    def report_debug(self,message: str):
        size_message = ''
        for i in message:
            size_message += '-'
        self.debug.append(
'''    # -------------- # -'''+size_message+'- #'+'''
    | SISTEM MESSAGE | <'''+message+'''> |
    # -------------- # -'''+size_message+'- #')

    def get_debug_log(self):
        print(
'''    # --------------------------------------------------------------------- #
    | Reportando mensagens de debug ocorridas durante a execussao do codigo |
    # --------------------------------------------------------------------- #''')
        for i in self.debug:
            print(i)

    def get_line_nblank(self): #retorna a linha, ao caso de linha em branco sera ignorada
        while(True):
            cache = self.file.readline()
            if cache == '\n':
                self.lines += 1
            else:
                self.lines += 1
                return cache

    def get_line(self): #retorna a linha
        self.lines += 1
        return self.file.readline()

    def set_key(self,key: str):
        key = format_spaces(key)
        if key in keys:
            report_debug('chave '+key+' repetida')
            self.keys.append(key)

    def set_description(self,key: str):
        self.description.append(key)

    def set_masterkey(self,key: str):
        key = format_spaces(key)
        if key in masterkey:
            report_debug('chave mestra'+key+' repetida')
        self.masterkey.append(key)

    def set_subjectkeys(self,key: str):
        key = format_spaces(key)
        self.subjectkeys.append(key)

    def get_description_by_key(self,key: str):
        pass

    def get_subjectkeys_by_masterkey(self,masterkey: str):
        pass

    def intense_search(self): #acha palavras parecidas a da buscada
        pass


test = file('dict.htdl')