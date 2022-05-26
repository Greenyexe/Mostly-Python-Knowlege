# exception = events detected during the execution that interrupt the flow of a program

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
except ZeroDivisionError as e: # as e just stores the exeption error. E can be anything but it is good practice to use e as it stands for error and fellow developers can understand
    print("You can't divide by zero! idiot!")
    print(e)
except ValueError as e:
    print('Enter only numbers plz')
    print(e)
except Exception as e:
    print('something went wrong :(')
    print(e)
else:
    print(result)
finally:
    print('This will always execute')