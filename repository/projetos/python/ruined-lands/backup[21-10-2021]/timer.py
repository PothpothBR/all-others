# para pegar a date formatada
from time import localtime


# data atual formatada
def strdate():
    return "[{}/{}/{} - {}:{}:{}]".format(localtime().tm_mday, localtime().tm_mon,
                                          localtime().tm_year, localtime().tm_hour,
                                          localtime().tm_min, localtime().tm_sec)


# cria um sistema de contagem de horas-minutos-segundos
# pode-se definir o id do relogio, o passo de contagem e se existe um tempo expecifico para o relogio reiniciar
# o reset deve ser um vetor contendo as horas-minutos-segundos a ser reiniciado
# ex: [4,55,12] 4h 55min 12 seg
class Timer:

    # cria o timer
    def __init__(self,  _id, step=1, reset=None):
        self.clock = [0, 0, 0]
        self.step = step
        self.id = _id
        self.reset = reset

    # gera a execução do timer, avança a contagem
    def tick(self):
        self.clock[2] += self.step
        if self.clock[2] >= 60:
            self.clock[2] = 0
            self.clock[1] += 1
            if self.clock[1] >= 60:
                self.clock[1] = 0
                self.clock[0] += 1
        if self.reset:
            if self.clock[0] >= self.reset[0] and self.clock[1] >= self.reset[1] and self.clock[2] >= self.reset[2]:
                self.clock = self.reset

    # mostra o tempo atual
    def show(self):
        return "[{}:{}:{}]".format(self.clock[0], self.clock[1], self.clock[2])

    # retorna o vetor de tempo
    def get_time(self):
        return self.clock
