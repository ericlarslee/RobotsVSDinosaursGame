from dino import Dino


class Herd:
    def __init__(self):
        self.type = 'dino'
        self.dinos = []
        self.populate_herd()

    def populate_herd(self):
        dino1 = Dino('Trike', 4, 10, 3)
        dino2 = Dino('Raptor', 4, 10, 5)
        dino3 = Dino('TRex', 4, 10, 4)
        self.dinos = [dino1, dino2, dino3]

    #   def print_herd(self):
    #   for dinosaur in self.dinos:
    #       print(dinosaur.Name)

