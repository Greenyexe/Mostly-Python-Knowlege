class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self): #more import than what is inherited from parent class
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()