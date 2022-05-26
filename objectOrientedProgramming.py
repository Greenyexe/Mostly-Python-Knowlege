# object is an instence of a class; like an object in real life

from car import Car

car1 = Car("Ford", "Focus", 2016, "blue")
car2 = Car("Ford", "Mustang", 2022, "red")

print(car1.make)
print(car1.model)
print(car2.year)
print(car1.colour)

car1.drive()
car2.stop()