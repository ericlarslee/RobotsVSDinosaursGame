from herd import Herd
from fleet import Fleet


def battle():
    dino_player_herd = Herd()
    robot_player_fleet = Fleet()
    print(dino_player_herd)
    print(robot_player_fleet)

    def dino_turn():
        for dino in dino_player_herd.dinos:
            print(f'{dino.Name} has {dino.Health} health and {dino.Attack_Power} attack power')
        choice = input('Which dino would you like to use to attack?')
        for dino in dino_player_herd.dinos:
            if choice == dino.Name:
                for robot in robot_player_fleet.robots:
                    print(f'{robot.Name} has {robot.Health} health and {robot.Attack_Power} attack power')
                target = input('Which robot would you like to attack?')
                for robot in robot_player_fleet.robots:
                    if target == robot:
                        robot.Health -= dino.Attack_Power
                        if robot.Health < 1:
                            robot_player_fleet.robots.pop(robot)
                            return robot_player_fleet.robots
                        return robot.Health

    def robot_turn():
        for robot in robot_player_fleet.robots:
            print(f'{robot.Name} has {robot.Health} health and {robot.Attack_Power} attack power')
        choice = input('Which robot would you like to use to attack?')
        for robot in robot_player_fleet.robots:
            if choice == robot.Name:
                for dino in dino_player_herd.dinos:
                    print(f'{dino.Name} has {dino.Health} health and {dino.Attack_Power} attack power')
                target = input('Which dino would you like to attack?')
                for dino in dino_player_herd.dinos:
                    if target == dino:
                        dino.Health -= robot.Attack_Power
                        if dino.Health < 1:
                            dino_player_herd.dinos.pop(dino)
                            return dino_player_herd.dinos
                        return dino.Health
    while dino_player_herd != [] or robot_player_fleet != []:
        dino_turn()
        robot_turn()
    if dino_player_herd.dinos is []:
        print('Congrats RoboMan, You won!')
    else:
        print('Congrats DinoMan, You won!')
