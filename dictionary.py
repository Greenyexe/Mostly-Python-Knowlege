# dictionary = A changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {"USA":"Washington DC",
                  "India":"New Dehli",
                  "England":"Weymouth init",
                  "Russia":"Moscow"}

capitals.update({"China":"Beijing"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("Russia")
#capitals.clear()

#print(capitals["Russia"])
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key, value in capitals.items():
    print(key, value)