# lambda function = function written in 1 line using lambda keyword
#                               accepts any number of arguments, but only has one expression.
#                              (think of it as a shortcut)
#                              (useful if needed for a short period of time, throw-away)

# lambda parameters:expression

#def double(x):
#    return x * 2

#print(double(5))


double = lambda x:x * 2
multiply = lambda x, y: x * y
fullName = lambda firstName, lastName: firstName + " " + lastName
ageCheck = lambda age:True if age >= 18 else False
print(double(5))
print(multiply(5, 3))
print(fullName("Bruno", "Greenfield"))
print(ageCheck(19))