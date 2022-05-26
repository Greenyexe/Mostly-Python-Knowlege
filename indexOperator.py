# index operator [] = gives access to a sequence's element (e.g. str, list, tuples)

name = "bruno Greenfield!"

#if (name[0].islower()):
#    name = name.capitalize()

firstName = name[0:5].upper()# don't need the 0 as python just assumes
lastName = name[6:].lower() # don't need last number as python just assumes
lastCharacter = name[-1]

print(firstName)
print(lastName)
print(lastCharacter)