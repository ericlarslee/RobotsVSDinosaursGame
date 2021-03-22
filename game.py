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
        choice = input('\nWhich dino would you like to use to attack?  ')
        for dino in dino_player_herd.dinos:
            if choice == dino.Name:
                for robot in robot_player_fleet.robots:
                    print(f'{robot.Name} has {robot.Health} health and {robot.Attack_Power} attack power')
                target = input('\nWhich robot would you like to attack?  ')
                for robot in robot_player_fleet.robots:
                    if target == robot.Name:
                        robot.damage_taken(dino.Attack_Power)
                        if robot.Health < 1:
                            robot_player_fleet.robots.pop(robot_player_fleet.robots.index(robot))
                            print(len(robot_player_fleet.robots))


    def robot_turn():
        for robot in robot_player_fleet.robots:
            print(f'{robot.Name} has {robot.Health} health and {robot.Attack_Power} attack power')
        choice = input('\nWhich robot would you like to use to attack?  ')
        for robot in robot_player_fleet.robots:
            if choice == robot.Name:
                for dino in dino_player_herd.dinos:
                    print(f'{dino.Name} has {dino.Health} health and {dino.Attack_Power} attack power')
                target = input('\nWhich dino would you like to attack?  ')
                for dino in dino_player_herd.dinos:
                    if target == dino.Name:
                        dino.damage_taken(robot.Attack_Power)
                        if dino.Health < 1:
                            dino_player_herd.dinos.pop(dino_player_herd.dinos.index(dino))
                            print(len(dino_player_herd.dinos))

    while len(dino_player_herd.dinos) != 0 or len(robot_player_fleet.robots) != 0:
        dino_turn()
        print(len(dino_player_herd.dinos))
        robot_turn()
        print(len(robot_player_fleet.robots))
        if len(dino_player_herd.dinos) == 0:
            print('Congrats RoboMan, You won!')
        else:
            print('Congrats DinoMan, You won!')
