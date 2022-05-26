# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs): # don't need to name kwargs just need double *
#    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end = " ")
    for key, value in  kwargs.items():
        print(value, end = " ")

hello(title = "Sir", first = "Bruno", middle = "John", last = "Greenfield")  