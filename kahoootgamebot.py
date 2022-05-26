#Imports
import requests
import random
from threading import Thread, currentThread
import webbrowser
import sys
#-------------------------------------------------------

#input number of codes and number of threads
numberOfThreads = int(input("How many threads do you want to run? "))
numberOfCodes = int(input("How many codes do you want to generate per thread? "))
#-------------------------------------------------------

#creates array of numbers to be used in codegenorator
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#-------------------------------------------------------

#codevalidator function
def is_code_valid(code):
  request = requests.get("https://kahoot.it/reserve/session/" + code)
  return request
#-------------------------------------------------------

#codegenorator function
def codegenorator(digits):
    code = ""
    for i in range(6):
        code += random.choice(digits)
    result = is_code_valid(code)
    if result.status_code == 200:
        webbrowser.open('https://kahoot.it?pin=' + str(code), new=2)
        sys.exit()
        return(code)
#-------------------------------------------------------

#function to run codegenorator in a thread
def realCode():
    for i in range(1, numberOfCodes):
        print(currentThread().getName(), codegenorator(digits))
#-------------------------------------------------------

#creates threads
for i in range(numberOfThreads):
    exec(f"checkerThread{i} = Thread(name='T{i}', target=realCode, args=())")
    exec(f"checkerThread{i}.start()")

# luke is a dumb