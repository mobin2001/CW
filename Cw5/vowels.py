vowels = "aeiouAEIOU"

words = ["apple", "banana", "cherry", "date", "elderberry"]

count_vowels = lambda word: sum(1 for char in word if char in "aeiouAEIOU")

sorted_words = sorted(words,key = count_vowels,reverse= True)

print(sorted_words)