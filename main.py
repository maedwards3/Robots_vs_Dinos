from robots import Robot
from dinosaurs import Dinosaur
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield

r1 = Robot('WALL-E')
r2 = Robot('T-800')
r3 = Robot('Roomba')

d1 = Dinosaur('Trogdor', 55)
d2 = Dinosaur('Allosaurus', 42)
d3 = Dinosaur('Spinosaurus', 55)

Fleet(3)
Fleet.create_fleet(r1)
Fleet.create_fleet(r2)
Fleet.create_fleet(r3)
print(Fleet.robot_fleet)

Herd(3)
Herd.create_herd(d1)
Herd.create_herd(d2)
Herd.create_herd(d3)
print(Herd.dinosaur_herd)