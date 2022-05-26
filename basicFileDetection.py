import os # needed for navigating

myPath = "C:\\Users\\edite\\Desktop\\folder"

if os.path.exists(myPath): 
    print("that location exists!")
    if os.path.isfile(myPath):
        print("that is a file")
    elif os.path.isdir(myPath):
        print("that is a directory")
else:
    print("That location doesn't exist")