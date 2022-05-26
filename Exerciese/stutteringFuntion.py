#def stutter():
#    word = input("Input the word you want stuttering: ")
#    word = word.capitalize()
#    print(word[:2]+"... " + word[:2] + "... " + word + "?")
#
#stutter()

stutter = lambda word:word[:2]+"... "+word[:2]+"... "+word+"?"
print(stutter("Bruno"))