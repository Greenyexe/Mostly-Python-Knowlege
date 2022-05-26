# Loop Control Statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("What is your name")
    if name != "":
        break

phoneNumber = "07946-243-883"

for i in phoneNumber:
    if i == "-":
        continue
    print(i, end = "")

for i in range(1, 21):
    if i == 13:
        pass
    print(i)