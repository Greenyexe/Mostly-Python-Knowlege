#imports packages
import os
from random import randint
#-------------------------------------------------------

#range of numbers to be used in the random number generator
numberOfBars = int(input("Enter the range: "))

try:
    if numberOfBars > 43:
        raise ValueError("The range is too big")
    else:
        pass
except ValueError:
    print("The range is too big to be visualised correctly")
    if input("Do you want to continue? (y/n) ") == "y":
        pass
    else:
        exit()
#-------------------------------------------------------

#quantity of times to generate a random number
numberOfGenerations = int(input("Enter the number of generations: "))
#-------------------------------------------------------

#asks the user if the want a file to be created and if so, creates it
if input("Would you like the output as a file? ") == "y":
    file = True
    try:
        FILE = open("bias_visulisation_chart.txt", "w")
    except:
        print("Error: File could not be created")
        file = False
randomNumbers = []
#-------------------------------------------------------

#uses a random number generator to generate a random number and then adds it to the randomNumbers string
def generateRandomNumber(numberOfBars):
    global randomNumbers
    randomNumbers.append(randint(0, numberOfBars))
#-------------------------------------------------------

#updates the graph
def reloadGraph():
   os.system("cls") #clears the screen
   for i in range (0, numberOfBars+1):
        exec(f"number{i} = round(randomNumbers.count({i}) / numberOfGenerations * 100)")#calculates the percentage of times a number appears in the randomNumbers list
    
   print("Bias visulisation graph: ") #title of the graph
   print("----------------------------------------------------")#divider
   for i in range (0, numberOfBars+1):
        if i >= 10:
            exec(f"print({i}, '|', '=' * number{i} + '>')")#if the number is greater than 10, it is printed with a single space after it
        else:
            exec(f"print({i}, '', '|', '=' * number{i} + '>')")#if the number is less than 10, it is printed with a double space after it
#-------------------------------------------------------

#main loop
for i in range (0, numberOfGenerations):
    generateRandomNumber(numberOfBars)
    reloadGraph()

    #file output
    if i == numberOfGenerations-1 and file == True:#if the last iteration is reached, the output is saved to a file
        with open("bias_visulisation_chart.txt", "a") as external_file:
            os.system("cls")#clears the screen
            for i in range (0, numberOfBars+1):
                    exec(f"number{i} = round(randomNumbers.count({i}) / numberOfGenerations * 100)")#calculates the percentage of times a number appears in the randomNumbers list
                
            print("Bias visulisation chart: ", file=external_file)#title of the graph
            print("---------------------------------------------------- ", file=external_file)#divider
            for i in range (0, numberOfBars+1):#
                if i >= 10:
                    exec(f"print({i}, '|', '=' * number{i} + '>', file=external_file)")#if the number is greater than 10, it is printed with a single space after it
                else:
                    exec(f"print({i}, '', '|', '=' * number{i} + '>',file=external_file)")#if the number is less than 10, it is printed with a double space after it
            print("", file=external_file)#new line")
            print("Range: " + str(numberOfBars), file=external_file)#adds the range of the graph
            print("Number of generations: " + str(numberOfGenerations), file=external_file)#adds the number of generations
            print("", file=external_file)#new line
            print("By Zoobdude", file=external_file)#adds the author
            external_file.close()#closes the file
            reloadGraph()#reloads the graph one last time so that the user can see the output

            print("The bias visulisation chart has been sucsessfuly saved to the file 'bias_visulisation_chart.txt'")#informs the user that the file has been saved

def clear(): #Clears the screen
  print("\033c",end = "")