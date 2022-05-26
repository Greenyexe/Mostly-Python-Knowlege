# map() = applies a function to each item in an terable (list, tuple, ect...)
#
# map(function, iterable)

store = [("shirt",20.00),
            ("pants",25.00),
            ("jacket",50.00),
            ("socks",10.00)]

to_pounds = lambda data: (data[0],data[1]*0.81)
to_dollars = lambda data: (data[0], data[1]/0.81)

store_pounds = list(map(to_pounds, store))
store_dollars = list(map(to_dollars, store))

for i in store_pounds:
    print(i)
for i in store_dollars:
    print(i)