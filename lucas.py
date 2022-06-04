import random

name = input("What is your name? ")

roast = random.randint(1, 4)

if roast == 1:
  print(name + " is the world's chunkiest THICC BOI")
elif roast == 2:
  print("The world is dark because of "+name+"'s immense MASS")
elif roast == 3:
  print("When "+name+" goes on the lift, "+name+" only goes down")
else:
  print(name + " is so fat that "+ name+ " has their own gravitational field")