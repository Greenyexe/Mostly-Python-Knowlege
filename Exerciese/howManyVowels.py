def countVowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for i in word:
        if i in vowels:
            counter += 1
    return counter

print(countVowels("pneumonoultramicroscopicsilicovolcanoconiosis"))