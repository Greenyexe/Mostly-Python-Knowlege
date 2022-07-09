def vowles_in_str(word):
  vowles = ["a", "e", "i", "o", "u"]
  count = 0
  for i in word:
    if i in vowles:
      count +=1
  return count

print(vowles_in_str(input("Enter a word: ")))