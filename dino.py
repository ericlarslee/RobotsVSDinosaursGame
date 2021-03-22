class Dino:
    def __init__(self, name, health, energy, attack_power):
        self.Name = name
        self.Health = health
        self.Energy = energy
        self.Attack_Power = attack_power

    def set_attributes(self):
        pass

    def damage_taken(self,damage):
        self.Health -= damage
        print(f'--------------------\n{self.Name} took {damage} damage\n--------------------')