# multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal is flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

fish = Fish()
hawk = Hawk()
rabbit = Rabbit()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()