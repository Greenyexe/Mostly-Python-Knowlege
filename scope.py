# scope = The region that a variable is recognized
# A variable is only available from inside the region it is created. 
# A gloable and locally scoped versions of a varable can be created

# l = local
# e = enclosing
# g = global
# b = built-in

name = "Bruno" # global scope (available inside & outside functions)

def displayName():
    name = "Greenfield" # local scope (available only inside this funtion)
    print(name)

print(name)
displayName()