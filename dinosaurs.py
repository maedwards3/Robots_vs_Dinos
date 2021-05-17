class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.energy = 65000000
        self.attack_power = attack_power
        self.health = 500
        self.is_dying = False
        self.is_dead = False

    def tail_swing_attack(self, robot):
        if self.energy >= 42250000:
            print(f"{self.type} ferociously used TAIL SWING on {robot.name}!")
            self.energy -= 3900000
            robot.health -= self.attack_power
            if robot.health < 50:
                print(f"Looks like {robot.name} is breaking down...SEND HIM TO THE SCRAP YARD!")
        else:
            print(f"{self.type} missed!")

    def claw_swipe_attack(self, robot):
        if self.energy >= 9750000:
            print(f"{self.type} used a frenzied CLAW SWIPE at {robot.name}!")
            self.energy -= 1300000
            robot.health -= self.attack_power + 5
            if robot.health < 50:
                print(f"Looks like {robot.name} is breaking down...SEND HIM TO THE SCRAP YARD!")
        else:
            print(f"{self.type} missed!")

    def charge_attack(self, robot):
        if self.energy >= 45500000:
            print(f"{self.type} recklessly CHARGED at {robot.name}!")
            self.energy -= 2600000
            robot.health -= self.attack_power + 7
            if robot.health < 50:
                print(f"Looks like that {robot.name} is breaking down...SEND HIM TO THE SCRAP YARD!")
        else:
            print(f"{self.type} missed!")

    def attack(self, robot):
        attack_type = input('Which attack method do you want obliterate your opponent with? Select <0> or <1> or <2>.')
        if attack_type == 0:
            self.tail_swing_attack(robot)
        elif attack_type == 1:
            self.claw_swipe_attack(robot)
        else:
            self.charge_attack(robot)

    def quickly_scurry_away_to_eat_a_smaller_dinosaur(self):
        print(f"{self.type} just ate a young dino *mmmm veal*!")
        self.energy += 6500000
        self.health += 50
