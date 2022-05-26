class Car:

    wheels = 4 # class variable

    def __init__(self, make, model, year, colour): # self refers to the object being worked on
        self.make = make    #instance variable
        self.model = model     #instance variable
        self.year = year    #instance variable
        self.colour = colour    #instance variable

    def drive(self):
        print("This "+self.model + " is driving")

    def stop(self):
        print("This "+ self.model +" is stopped")