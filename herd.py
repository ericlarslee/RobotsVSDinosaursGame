from dino import Dino


class Herd:
    def __init__(self):
        self.type = 'dino'
        self.dinos = []
        self.populate_herd()


    def populate_herd(self):
        dino1 = Dino('Trike', 15, 10, 3)
        dino2 = Dino('Raptor', 10, 10, 5)
        dino3 = Dino('TRex', 10, 10, 4)
        self.dinos = [dino1, dino2, dino3]
        for token in self.dinos:
            print(token)

    def print_herd(self):
        for dinosaur in self.dinos:
            print(dinosaur.Name)

