from dinosaurs import Dinosaur
# Need to figure where to place "Dinosaur" to import


class Herd:
    def __init__(self, max_herd):
        self.dinosaur_herd = []
        self.max_herd = max_herd
        self.herd_is_wiped_out = False

    def create_herd(self, dinosaur):
        if len(self.dinosaur_herd) < self.max_herd:
            self.dinosaur_herd.append(dinosaur)
            return True
        return False
