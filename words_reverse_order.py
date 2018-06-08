# Write a program (using functions!) that asks the user for a long string containing multiple words
# Print back to the user the same string, except with the words in backwards order

words = input("Enter some words: ")
wordsList = words.split()
result = []
for word in wordsList:
    result.insert(0, word)
print (result)
