# *args = parameter that will pack all arguments into a tuple
# can't change tuple so you can change to list with args = list(args)
# useful so that a function can accept a varying amount of arguments

def add(*args): #args can be named whatever, you just have to have the *
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3, 4))