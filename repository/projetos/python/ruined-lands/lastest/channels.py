import status


# classe para encapsular um objeto/entidade que pode ser manipulado em um canal de execussao
class Entity:
    def __init__(self, id, entity, lifetime, mechanic=[None, None, None]):
        self.id = id
        self.entity = entity
        self.lifetime = lifetime
        self.next = None
        self.spawn = mechanic[0]
        self.flow = mechanic[1]
        self.destroy = mechanic[2]


# classe para suportar e gerenciar entidades, gerando um fluxo de execussao manipulavel
class Channel:

    # flag que possibilita a execussao de um loop infinito
    INFINITY = -1

    # inicia a classe
    def __init__(self, max_len: int):

        self.lenght = 1
        self.head = Entity(-1, self.lenght, -1)
        self.anchor = self.head
        self.anchor.next = self.head
        self.max_lenght = max_len

    # adiciona ao topo da cadeia de entidades, se nao atingir o limite da fila
    def add(self, entity: Entity):
        """ [head = system entity] -> [all entities] -> [anchor = last added entity]"""
        if self.lenght < self.max_lenght:
            if entity.spawn:
                entity.spawn(entity)
            self.anchor.next = entity
            self.anchor = entity
            entity.next = self.head
            self.lenght += 1
        else:
            status.report(1, 'Channel.add()')

    # adiciona multiplas entidades ao topo da cadeia de entidades, se nao atingir o limite da fila
    def add_multi(self, entities: tuple):
        for ent in entities:
            self.add(ent)
        if status.status():
            status.report(1, 'Channel.add_multi()')
            return

    # cria e adiciona ao topo da cadeia de entidades, se nao atingir o limite da fila
    def spawn(self, id, entity, lifetime, mechanic=[None, None, None]):
        self.add(Entity(id, entity, lifetime, mechanic))
        if status.status():
            status.report(1, 'Channel.spawn()')

    # cria e adiciona multiplas entidades ao topo da cadeia de entidades, se nao atingir o limite da fila
    def spawn_multi(self, entities: tuple):
        """ ((id, entity, lifetime, mechanic),
        (id, entity, lifetime, mechanic)) """
        for i in entities:
            if len(i) == 4:
                self.add(Entity(i[0], i[1], i[2], i[3]))
            else:
                self.add(Entity(i[0], i[1], i[2]))
            if status.status():
                status.report(1, 'Channel.spawn_multi()')

    # destroi a entidade
    #  argument
    #     |
    # [a.d(a.e)]
    def destroy(self, id):
        back_point = self.head

        while back_point.next.id != id:
            if back_point.next.id == -1:
                status.report(1, 'Channel.destroy()')
                return
            back_point = back_point.next

        entity = back_point.next
        if entity.destroy:
            entity.destroy(entity)
        back_point.next = entity.next

        self.lenght -= 1

    # destroi a entidade apos a entidade informada
    # argument
    #    |
    #   [a]-> [b.d(b.e)]
    def destroy_after(self, back_point: Entity):

        entity = back_point.next

        if entity.id == -1:
            status.report(1, 'Channel.destroy()')
            return

        if entity.destroy:
            entity.destroy(entity)
        back_point.next = entity.next

        self.lenght -= 1

    # manipula as entidades conforme o tempo estipulado
    # times = [ciclos, entidades] / times = entidades
    #    time
    #     |
    #   (time != 0)-> [a.f(a.e)]-> [b.f(b.e)] -> [...]
    def flow(self, times):
        if self.lenght == 1:
            status.report(1, 'Channel.flow()')
            return
        if type(times) == list:
            if times[1] >= self.lenght:
                status.report(1, 'Channel.flow()')
                return
            times = times[0]*self.lenght + times[1]
        else:
            times += int(times / (self.lenght - 1))
        ent = self.head.next
        back_point = self.head

        while times != 0 and self.lenght > 1:
            if ent.flow:
                ent.flow(ent)
            if ent.lifetime == 1:
                self.destroy_after(back_point)
            else:
                back_point = back_point.next
            times -= 1
            if ent.lifetime > -1:
                ent.lifetime -= 1
            ent = back_point.next

    # executa a entidade apos a entidade informada e retorna-a
    # argument
    #    |
    #   [a]-> [b]-> [...]
    #          |
    #        return
    def step_after(self, back_point: Entity):
        if type(back_point) != Entity:
            status.report(1, 'Channel.step_after()')
            return None

        ent = back_point.next

        if ent.flow:
            ent.flow(ent)
        if ent.lifetime == 1:
            self.destroy_after(back_point)
        else:
            back_point = back_point.next
        ent.lifetime -= 1

        return back_point