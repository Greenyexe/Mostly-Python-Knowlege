# nested loops = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loops"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Which symbol do you want?: ")

for i in range(rows): #i can be anything
    for j in range(columns): #j can be anything
        print(symbol, end = "")
    print()