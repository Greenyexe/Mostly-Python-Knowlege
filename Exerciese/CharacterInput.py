userInput = input("What is your name? :  ") # input() is a function that takes user input
age = int(input("What is your age? :  ")) # int() is a function that converts the user input to an integer
year = int(input("What year is it now? :  ")) # int() is a function that converts the user input to an integer

newAge = 100 - age # newAge is the age you have left to be 100

print("Hello {} you will turn 100 in the year {}".format(userInput, year + newAge))