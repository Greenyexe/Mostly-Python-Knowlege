# ********************************************
# if __name__ == '__main__'
# ********************************************

# Why tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__
# __name__ will not have __main__ asigned to it if it is being run from another module

if __name__ == "__main__":
    print("Running the module directly")
else:
    print("Running other module indirectly")