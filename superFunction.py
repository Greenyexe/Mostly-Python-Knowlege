# super() = Function used to give access to the methods of a parent class.
# Returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        return self.width * self.length

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        return self.width * self.height * self.length

square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())