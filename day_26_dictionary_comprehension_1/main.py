sentence = input("Enter a sentence: ")
# 🚨 Don't change code above 👆
# Write your code below 👇

words = sentence.split(" ")
result = {word:len(word) for word in words}

print(result)
