import os

source = "C:\\Users\\edite\\Desktop\\test.txt"
destination = "test.txt" #normaly needs a path

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")