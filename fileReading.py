try:
    with open('testText.txt') as file:# you will probably need the file name path but as its in the same folder its fine
        print(file.read()) 
except FileNotFoundError:
    print("That file was not found :(")