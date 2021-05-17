from dinosaurs import Dinosaur
from robots import Robot
from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet
        self.herd = Herd

    def run_game(self):
        print(
            "Welcome to Robos vs Dinos! Where a fleet of Robots are set to fight a herd of Dinosaurs in epic "
            "proportion!")
        input("Select <1> for the Herd to move first, or <2> for the Fleet to move first.")
        if input == 1:
            self.battle_royale()
        elif input == 2:
            self.battle_royale()
        else:
            input("Please select <1> or <2>.")

    def battle_royale(self):
        while self.herd.herd_is_wiped_out is True or self.Fleet.fleet_is_destroyed is True:
            if input == 1:
                self.dino_turn()
                print(self.dino_turn())
            elif input == 2:
                self.robo_turn()
                print(self.robo_turn())

    def dino_turn(self):
        self.show_dino_opponent_options()
        input("Select opponent to attack: <1> , <2> , <3>.")
        if input == 1:
            Dinosaur.attack(robot=r1)
        elif input == 2:
            Dinosaur.attack(robot=r2)
        elif input == 3:
            Dinosaur.attack(robot=r3)
        else:
            input("Please select <1> , <2> or <3>.")

    def robo_turn(self):
        self.show_robo_opponent_options()
        input("Select opponent to attack: <1> , <2> , <3>.")
        if input == 1:
            Robot.attack(dinosaur=d1)
        elif input == 2:
            Robot.attack(dinosaur=d2)
        elif input == 3:
            Robot.attack(dinosaur=d3)
        else:
            input("Please select <1> , <2> or <3>.")
            
    def show_dino_opponent_options(self):
        # print the remaining indexes of the Robot fleet & print their health
        pass

    def show_robo_opponent_options(self):
        # print the remaining indexes of the Dinosaur fleet & print their health
        pass

    def display_winners(self):
        # if list == 0 health, print winner name (fleet or herd)
        pass
