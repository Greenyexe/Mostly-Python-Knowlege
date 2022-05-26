userInput = input("What is your name? :  ")
age = int(input("What is your age? :  "))
year = int(input("What year is it now? :  "))

newAge = 100 - age

print("Hello", userInput, "you will turn 100 in the year", year + newAge)