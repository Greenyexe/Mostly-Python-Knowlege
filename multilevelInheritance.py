# multilevel inheritance = when a derived (child) class inherits another derived (child) class
# like a family tree

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()