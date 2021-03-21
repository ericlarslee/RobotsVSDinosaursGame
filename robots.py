from weapon import Weapon


class Robot:
    def __init__(self, name, health):
        self.Name = name
        self.Health = health
        self.Power_Level = 1
        self.Weapon = Weapon()
        self.Attack_Power = self.Weapon.attack_damage

        