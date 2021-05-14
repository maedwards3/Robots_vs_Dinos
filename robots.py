class Robot:
    def __init__(self, name, weapons):
        self.name = name
        self.power_level = 700000
        self.health = 750
        self.weapon = weapons
        self.is_breaking_down = False
        self.is_destroyed = False

    def flying_longsword_attack(self, dinosaur):
        self.weapon = "Longsword"
        if self.power_level >= 455000:
            print(self.name, f" used FLYING LONGSWORD to attack ", dinosaur.type, f"!")
            self.power_level -= 42000
            dinosaur.health -= 60
            if dinosaur.health < 75:
                print(f"Looks like that ", dinosaur.type, f" is very weak!")
        else:
            print(self.name, f" missed!")

    def long_range_attack(self, dinosaur):
        self.weapon = "Laser Beam"
        if self.power_level >= 100000:
            print(self.name, f" used LASER BEAM with pinpoint accuracy on ", dinosaur.type, f"!")
            self.power_level -= 14000
            dinosaur.health -= 35
            if dinosaur.health < 75:
                print(f"Looks like that ", dinosaur.type, f" is very weak!")
        else:
            print(self.name, f" missed!")

    def hell_in_the_sky_attack(self, dinosaur):
        self.weapon = "105mm Howitzer"
        if self.power_level >= 500000:
            print(self.name, f" rained hell from above with a 105mm Howitzer on", dinosaur.type, f"!")
            self.power_level -= 75000
            dinosaur.health -= 85
            if dinosaur.health < 75:
                print(f"Looks like that ", dinosaur.type, f" is very weak!")

    def refresh_relube(self):
        print(self.name, f" just drizzled new oil over their gearboxes!")
        self.power_level += 70000
        self.health += 75
