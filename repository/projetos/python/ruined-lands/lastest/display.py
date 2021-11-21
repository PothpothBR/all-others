import status


# classe para encapsulamento de funcoes para manipular imagens, e para gerenciar o desenho no console
class Display:

    # gera o buffer que sera desenhado no console e todos os assets padrao
    def __init__(self, size):
        self.buffer = self.buffer_to_bitmap(
            ['*' * size for i in range(int(size / 2))], 'p')
        self.buffer_len = size
        self.assets = {
            'house': {
                'bitmap': self.buffer_to_bitmap(r'''
/¨¨\
|_H|
                ''', 'v'),
                'type': 'v',
                'domination': 1,
                'time': 3,
                'life': 25
            },
            'abitant': {
                'bitmap': self.buffer_to_bitmap('@', 'p'),
                'type': 'p',
                'coins': 1,
                'time': 2,
                'life': 10,
                'reproduce': 8
            },
            'dominated': {
                'bitmap': self.buffer_to_bitmap(r'~', 'p'),
                'type': 'p'
            },
            'losted': {
                'bitmap': self.buffer_to_bitmap(r'-', 'p'),
                'type': 'p'
            }
        }

    # transforma uma imagem em estado de buffer em um bitmap editavel
    @staticmethod
    def buffer_to_bitmap(buffer, flag) -> list:
        '''
            v - visualizer type
            p - primary type
            e - encurted type
        '''

        if flag.lower() == 'v':
            buffer = buffer.split('\n')[1:-1]
        elif flag.lower() == 'e':
            buffer = buffer.split('\n')

        return [list(i) for i in buffer]

    # transforma uma imagem em estado de bitmap em um buffer
    # essa conversao é agradavel pelo fato de ser facilmente
    # imprimivel no console e gardada em erquivos para facil visualização
    @staticmethod
    def bitmap_to_buffer(bitmap) -> str:
        buffer = ''
        for line in bitmap:
            for i in line:
                buffer += i
            buffer += '\n'
        return buffer

    # desenha um bitmap em outro, em determinado local
    # se parte for exedida, a mesma sera perdida
    @staticmethod
    def draw_in(x, y, origin, bitmap) -> list:
        max_y = len(bitmap)
        max_x = len(bitmap[0])

        for line in origin:
            if y >= max_y:
                status.report(1, 'Display.draw_in()')
                break
            _x = x
            for bit in line:
                if _x >= max_x:
                    status.report(1, 'Display.draw_in()')
                    break
                bitmap[y][_x] = bit
                _x += 1
            y += 1
        return bitmap

    # desenha um bitmap no buffer de desenho do console
    # pode ser dado uma referencia a um asset
    def draw(self, x, y, origin):
        if type(origin) == str:
            origin = self.assets[origin]['bitmap']

        self.buffer = self.draw_in(x, y, origin, self.buffer)

    # faz a atualizacao do buffer no console
    def flip(self):
        print(self.bitmap_to_buffer(self.buffer))


class Console:

    # saida de caracteres formatada
    @staticmethod
    def inp(val=''):
        if val:
            for l in val.split('\n'):
                print('|' + l)

        tmp = input("|> ").lower()
        print(f"---{len(tmp) * '-'}\n")
        return tmp

    # entrada de dados formatada
    @staticmethod
    def pri(val, end='\n'):
        max_len = 0
        for line in val.split('\n'):
            print('|' + line)
            if len(line) > max_len:
                max_len = len(line)
        print(f"-{max_len * '-'}{end}")
