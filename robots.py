from weapons import Weapons


class Robot:
    def __init__(self, name,):
        self.name = name
        self.power_level = 700000
        self.health = 750
        self.weapon_options = [Weapons('Longsword', 60), Weapons('Laser Beam', 35), Weapons('105mm Howitzer', 85)]
        self.chosen_weapon = None
        self.is_breaking_down = False
        self.is_destroyed = False

    def flying_longsword_attack(self, dinosaur):
        if self.power_level >= 455000:
            print(f"{self.name} used FLYING LONGSWORD to attack {dinosaur.type}!")
            self.power_level -= 42000
            dinosaur.health -= self.weapon_options[0].attack_power
            if dinosaur.health < 75:
                print(f"Looks like that {dinosaur.type} is very weak...FINISH HIM!")
        else:
            print(f"{self.name} missed!")

    def long_range_attack(self, dinosaur):
        if self.power_level >= 100000:
            print(f"{self.name} used LASER BEAM with pinpoint accuracy on {dinosaur.type}!")
            self.power_level -= 14000
            dinosaur.health -= self.weapon_options[1].attack_power
            if dinosaur.health < 75:
                print(f"Looks like that {dinosaur.type} is very weak...FINISH HIM!")
        else:
            print(f"{self.name} missed!")

    def hell_in_the_sky_attack(self, dinosaur):
        if self.power_level >= 500000:
            print(f"{self.name} RAINED HELL FROM ABOVE with a 105mm Howitzer on {dinosaur.type}!")
            self.power_level -= 75000
            dinosaur.health -= self.weapon_options[2].attack_power
            if dinosaur.health < 75:
                print(f"Looks like that {dinosaur.type} is very weak...FINISH HIM!")
        else:
            print(f"{self.name} missed!")

    def attack(self, dinosaur):
        weapon_choice = input('Which weapon would you like to send your opponent into extinction? Select <0> or <1> '
                              'or <2>.')
        if weapon_choice == 0:
            self.chosen_weapon = self.weapon_options[0]
            self.flying_longsword_attack(dinosaur)
        elif weapon_choice == 1:
            self.chosen_weapon = self.weapon_options[1]
            self.long_range_attack(dinosaur)
        else:
            self.chosen_weapon = self.weapon_options[2]
            self.hell_in_the_sky_attack(dinosaur)

    def refresh_relube(self):
        print(f"{self.name} just drizzled new oil over their gearboxes!")
        self.power_level += 70000
        self.health += 75
