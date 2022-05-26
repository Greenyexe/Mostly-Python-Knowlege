# Basic quiz game. 

def newGame():
    guesses = []
    correctGuesses = 0
    questionNumber = 1

    for i in questions:
        print("--------------------")
        print(i)
        
        for j in options[questionNumber - 1]:
            print(j)

        guess = input().capitalize()
        guesses.append(guess)

        correctGuesses += checkAnswer(questions.get(i), guess)
        questionNumber += 1

    displayScore(correctGuesses, guesses)

def checkAnswer(answer, guess):
     if answer == guess:
         return 1
     else:
         return 0

def displayScore(correct, userTry):
    print("--------------------")
    print("RESULTS")
    print("--------------------")

    print("Answers: ", end="")

    for i in questions:
        print(questions.get(i), end=" ")

    print()
    print("--------------------")

    print("Guesses: ", end=" ")
    for i in userTry:
        print(i, end=" ")

    print()
    print("--------------------")

    score = int((correct/len(questions)*100)) # score = (making it an interger) correct (which is already a number) divided by len(the amount of items in questions) * 100 to get a percentage
    print("Your score is: "+str(score)+"%")

def playAgain():
    response = input("Do you want to play again? (yes or no): ")
    response = response.lower()

    if response == "yes":
        return True
    else:
        return False

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth flat?: ": "D"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
                  ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
                  ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
                  ["A. Yes", "B. No", "C. Sometimes", "D. AMOGUS"]]

newGame()

while playAgain():
    newGame()

print("Byeeeee")