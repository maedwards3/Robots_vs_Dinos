from robots import Robot
# Need to figure where to place "Robot" in class to import


class Fleet:
    def __init__(self, max_fleet):
        self.robot_fleet = []
        self.max_fleet = max_fleet
        self.fleet_is_destroyed = False

    def create_fleet(self, robot):
        if len(self.robot_fleet) < self.max_fleet:
            self.robot_fleet.append(robot)
            return True
        return False
