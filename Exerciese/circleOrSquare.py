#import math

#def circleOrSquare(circle, square):
#    circle *= 2*math.pi
#    square = math.sqrt(square)*4
#    return True if square < circle else False
#print(circleOrSquare(16, 625))

circleOrSquare=lambda r,a:a**.5*4<6.28*r
print(circleOrSquare(16, 625))