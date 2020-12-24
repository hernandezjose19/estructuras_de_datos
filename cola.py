class Cola():

    def __init__(self):

        self.lista = []

    def queue(self, elemen):

        self.lista.append(elemen)
        print(self.lista)

    def dequeue(self):

        del self.lista[0]
        print(self.lista)

    def front(self):
        print(self.lista[0])


mi_cola = Cola()
mi_cola.queue(50)
mi_cola.queue(20)
mi_cola.queue(89)
mi_cola.front()
mi_cola.dequeue()