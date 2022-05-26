# zip(*iterables) = aggregate elements from two or more iterable (list, tuples, sets, ect.)
# creates a zip object with paire elements stored in tuples for each element

usernames = ["Dude", "Bro", "Hacker"]
passwords = ["P@ssword", "abc123", "guest"]
loginDate = ["1/1/2021", "2/1/2022", "3/1/2021"]

#users = dict(zip(usernames, passwords))

#print(type(users),"\n")

#for key,value in users.items():
#    print(key+": "+value)

users = zip(usernames, passwords, loginDate)

for i in users:
    print(i)