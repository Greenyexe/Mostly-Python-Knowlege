def isTriplet(a, b, c):
    a **= 2
    b **= 2
    c **= 2
    
    a = [a, b, c]
    a.sort()

    if a[0] + a[1] == a[2]:
        return True
    else:
        return False

print(isTriplet(1, 2, 3))