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

