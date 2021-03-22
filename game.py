
from herd import Herd
from fleet import Fleet





def game():
    dino_player_herd = Herd()
    robot_player_fleet = Fleet()

    def dino_turn:
        for dino in dino_player_herd:
            print(f'{dino.Name} has {dino.Health} health and {dino.Attack_Power} attack power')
        choice = input('Which dino would you like to use to attack?')
        for dino in dino_player_herd:
            if choice == dino:
                for robot in robot_player_fleet:
                    print(f'{robot.Name} has {robot.Health} health and {robot.Attack_Power} attack power')
                target = input('Which robot would you like to attack?')
                for robot in robot_player_fleet:
                    if target == robot:
                        robot.Health -= dino.Attack_Power
                    if robot.health < 1:
                        robot_player_fleet.pop(robot)


    

    while dino_player_herd != [] & robot_player_fleet !=[]:
        dino_turn()
