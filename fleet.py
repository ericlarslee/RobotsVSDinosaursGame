from robots import Robot

class Fleet:
    def __init__(self):
        self.type = 'robot'
        self.robots = []
        self.populate_fleet()


    def populate_fleet(self):
        robot1 = Robot('Steve', 15)
        robot2 = Robot('Norm', 10)
        robot3 = Robot('Prime', 10)
        self.robots = [robot1, robot2, robot3]
        for token in self.robots:
            print(token)