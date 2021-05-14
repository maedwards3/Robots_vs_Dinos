class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.energy = 65000000
        self.attack_power = attack_power
        self.health = 500

    def tail_swing_attack(self, robots):
        print(self.type, f" used Tail Swing to attack a Robot!")
        self.energy -= 1500000
        robots.health -= 42

    def claw_swipe_attack(self, robots):
        print(self.type, f" used Claw Swipe to attack a Robot!")
        self.energy -= 1000000
        robots.health -= 35

    def charge_attack(self, robots):
        print(self.type, f" used Charge to attack a robot!")
        self.energy -= 2000000
        robots.health -= 55

    def quickly_scurry_away_to_eat_a_smaller_dinosaur(self):
        print(self.type, f" just ate a young dino *mmmm veal*!")
        self.energy += 750000
        self.health += 50
