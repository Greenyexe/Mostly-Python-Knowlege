# filter() = creates a collection of elements from an iterable for which a function returns true
#
# filter(function, iterable)

people = [("Jeff", 43),
                ("Jorden", 16),
                ("Jeremy", 6),
                ("Joe", 35),
                ("John", 54),
                ("Jim", 12)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, people))

for i in drinking_buddies:
    print(i)