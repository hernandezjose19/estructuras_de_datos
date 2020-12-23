class Pila():

    def __init__(self):

        self.lista = [1, 2]


    def push(self, elemen):

        self.lista.append(elemen)
        print(f"Se anadio el elemnto {elemen}")
        print(self.lista)


    def pop(self):

        print(self.lista)
        del self.lista[-1]
        print(self.lista)


    def peek(self):

        print(self.lista[-1])




