import random

words=["apple","banana","cherry","orange","kiwi","lemon","grapes","mango", "peach","pineapple","strawberry", "watermelon", "blueberry", "blackberry", "raspberry"]
word=words[random.randint(0,len(words))]

vowels = ["a", "e", "i", "o", "u"]
line_letters = ["a","e","f","h","i","k","l","m","n","t","v","w","x","y","z"]
enclosed_letters = ["a","b","d","o","p","q"]

vowel_count = 0
line_count = 0
enclosed_count = 0

for i in word:
  if i in vowels:
    vowel_count +=1
for i in word:
  if i in line_letters:
    line_count +=1
for i in word:
  if i in enclosed_letters:
    enclosed_count +=1
guess = input(f"There are {vowel_count} vowels, {line_count} line letters, and {enclosed_count} enclosed letters\nGuess the word: ")

if guess == word:
  print("You win!")
else:
  print("You lose!")
  print(f"The word was {word}")