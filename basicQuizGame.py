# Basic quiz game. 
# The user is asked a series of questions and given a set of answers.
# The user is then asked if they want to play again.

# all comments were written by github copilot

def newGame(): # new game function
    guesses = [] # guesses is a list
    correctGuesses = 0 # correctGuesses is a number
    questionNumber = 1 # questionNumber is a number

    for i in questions: # for each item in questions
        print("--------------------") # print a line
        print(i) # print the question
        
        for j in options[questionNumber - 1]: # for each item in options
            print(j) # print the options

        guess = input().capitalize() # guess is a string
        guesses.append(guess) # append the guess to the guesses list

        correctGuesses += checkAnswer(questions.get(i), guess) # correctGuesses = correctGuesses + checkAnswer(questions.get(i), guess)
        questionNumber += 1 # questionNumber = questionNumber + 1

    displayScore(correctGuesses, guesses) # displayScore(correctGuesses, guesses)

#***************************************************************************

def checkAnswer(answer, guess): # checkAnswer(answer, guess)
     if answer == guess: # if answer is equal to guess
         return 1 # return 1
     else: # else
         return 0 # return 0

#***************************************************************************

def displayScore(correct, userTry): # displayScore(correct, userTry)
    print("--------------------") # print a line
    print("RESULTS") # print results
    print("--------------------") # print a line

    print("Answers: ", end="") # print answers

    for i in questions: # for each item in questions
        print(questions.get(i), end=" ") # print the question

    print() # print a new line
    print("--------------------") # print a line

    print("Guesses: ", end=" ") # print guesses
    for i in userTry: # for each item in userTry
        print(i, end=" ") # print the guess

    print() # print a new line
    print("--------------------") # print a line

    score = int((correct/len(questions)*100)) # score = (making it an interger) correct (which is already a number) divided by len(the amount of items in questions) * 100 to get a percentage
    print("Your score is: "+str(score)+"%") # print the score

#***************************************************************************

def playAgain(): # playAgain()
    response = input("Do you want to play again? (yes or no): ") # response is a string
    response = response.lower() # response is a string

    if response == "yes": # if response is equal to yes
        return True # return True
    else: # else
        return False # return False

#***************************************************************************

questions = { # questions is a dictionary
    "Who created Python?: ": "A", # question 1
    "What year was Python created?: ": "B", # question 2
    "Python is tributed to which comedy group?: ": "C", # question 3
    "Is the Earth flat?: ": "D" # question 4
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"], # options is a list
                  ["A. 1989", "B. 1991", "C. 2000", "D. 2016"], 
                  ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"], 
                  ["A. Yes", "B. No", "C. Sometimes", "D. AMOGUS"]]

newGame() # newGame()

while playAgain(): # while playAgain()
    newGame() # newGame()

print("Byeeeee") # print bye