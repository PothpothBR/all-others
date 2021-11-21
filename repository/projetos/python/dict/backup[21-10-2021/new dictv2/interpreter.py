from data_manager import file
from format_strings import format_spaces
from format_strings import clear_spaces

class interpreter(file):
    in_cache = False
    in_data = False
    in_document = False
    in_config = False
    in_key = False
    in_masterkey = False
    in_author = False
    in_description = False

    def __init__(self):
        pass

    def get_tag(self, cache: str, start):  # acha uma tag
        if start == str:
            tag = ''
            for i in range(len(cache)):
                if cache[i] == '<':
                    for it in cache[i + 1:]:
                        if it == '>':
                            if tag != start:
                                return [clear_spaces(tag), '>', i + 1]
                        elif it == ':':
                            if tag != start:
                                return [clear_spaces(tag), ':', i + 1]
                        elif it == ' ':
                            continue
                        tag += it
        elif start == int:
            tag = ''
            cache = cache[start:]
            for i in range(len(cache)):
                if cache[i] == '<':
                    for it in cache[i + 1:]:
                        if it == '>':
                            return [clear_spaces(tag), '>', i + 1]
                        elif it == ':':
                            return [clear_spaces(tag), ':', i + 1]
                        elif it == ' ':
                            continue
                        tag += it

    def get_value(self, cache: str, start):  # pega o valor da tag
        if start == str:
            value = ''
            cache = cache[start:]
            for i in range(len(cache)):
                if cache[i] == '<':
                    for it in cache[i + 1:]:
                        if it == '>':
                            return [format_spaces(value)]

                        elif it == ' ':
                            continue
                        value += it
        elif start == int:
            value = ''
            cache = cache[start:]
            for i in range(len(cache)):
                if cache[i] == '<':
                    for it in cache[i + 1:]:
                        if it == '>':
                            return [format_spaces(value)]
                        elif it == ' ':
                            continue
                        value += it

    def processing_tag(self, tag: str, end: str):  # processa a tag que foi passada como argumento
        if end == '>':
            if tag == 'cache':
                if self.in_data or self.in_document or self.in_config or self.in_key or self.in_masterkey or self.in_author or self.in_description:  # verifica se cache esta dentro de outra tag
                    self.report_debug('<cache> nao deve estar contido em outra tag')
                self.in_cache = True

            elif tag == 'data':
                if self.in_document or self.in_config or self.in_key or self.in_masterkey or self.in_author or self.in_description:  # verifica se data esta contido por outra tag senao cache
                    self.report_debug('<data> deve estar contido somente por <cache>')

                if not self.in_cache:
                    self.report_debug('<data> nao esta contido por <cache>')  # verifica se data esta contida por cache
                self.in_data = True


            elif tag == 'document':
                if self.in_config or self.in_key or self.in_masterkey or self.in_author or self.in_description:
                    self.report_debug('<document> deve estar contido somente por <cache> e <data>')

                if not self.in_data and self.in_cache:
                    self.report_debug('<document> nao esta contido por <cache> e <data>')  # verifica se data esta contida por cache

                self.in_document = True


            elif tag == 'configuration':
                if self.in_document or self.in_key or self.in_masterkey or self.in_author or self.in_description:
                    self.report_debug('<configuration> deve estar contido somente por <cache> e <data>')

                if not self.in_data and not self.in_cache:
                    self.report_debug('<configuration> nao esta contido por <cache> e <data>')  # verifica se data esta contida por cache

                self.in_config = True

            elif tag == '/cache':
                self.in_cache = False

            elif tag == '/data':
                self.in_data = False

            elif tag == '/document':
                self.in_document = False

            elif tag == '/configuration':
                self.in_config = False

            elif tag == '/key':
                self.in_key = False

            elif tag == '/masterkey':
                self.in_masterkey = False

            elif tag == '/author':
                self.in_author = False

            elif tag == '/description':
                self.in_description = False
        elif end == ':':
            if tag == 'key':
                if self.in_document or self.in_config or self.in_masterkey or self.in_author or self.in_description:
                    self.report_debug('<key> deve estar contido somente por <cache> e <data>')

                if not self.in_data and not self.in_cache:
                    self.report_debug('<key> nao esta contido por <cache> e <data>')  # verifica se data esta contida por cache

                self.in_key = True

            elif tag == 'masterkey':
                if self.in_document or self.in_key or self.in_config or self.in_author or self.in_description:
                    self.report_debug('<masterkey> deve estar contido somente por <cache> e <data>')

                if not self.in_data and not self.in_cache:
                    self.report_debug('<masterkey> nao esta contido por <cache> e <data>')  # verifica se data esta contida por cache

                self.in_masterkey = True

            elif tag == 'author':
                if self.in_document or self.in_key or self.in_masterkey or self.in_config or self.in_description:
                    self.report_debug('<author> deve estar contido somente por <cache> e <data>')

                if not self.in_data and not self.in_cache:
                    self.report_debug('<author> nao esta contido por <cache> e <data>')  # verifica se data esta contida por cache

                self.in_author = True

            elif tag == 'description':
                if self.in_document or self.in_key or self.in_masterkey or self.in_author or self.in_config:
                    self.report_debug('<description> deve estar contido somente por <cache> e <data>')

                if not self.in_data and not self.in_cache:
                    self.report_debug('<description> nao esta contido por <cache> e <data>')  # verifica se data esta contida por cache

                self.in_description = True

            elif tag == 'version':
                if self.in_document or self.in_key or self.in_masterkey or self.in_author or self.in_config:
                    self.report_debug('<description> deve estar contido somente por <cache>, <data> e <document>')

                if not self.in_data or not self.in_cache or not self.in_document:
                    self.report_debug('<version> nao esta contido por <cache>, <data> e <document>')  # verifica se data esta contida por cache



            elif tag == 'language':
                pass

            elif tag == 'type':
                pass

            elif tag == 'cryptography':
                pass

            elif tag == 'lines':
                pass

            elif tag == 'debug':
                pass

            elif tag == 'format':  # program visual / inline
                pass
