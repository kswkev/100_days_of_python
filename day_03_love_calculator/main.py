print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

score = 0
score += name1.count("t") + name2.count("t")
score += name1.count("r") + name2.count("r")
score += name1.count("u") + name2.count("u")
score += name1.count("e") + name2.count("e")
score *= 10

score += name1.count("l") + name2.count("l")
score += name1.count("o") + name2.count("o")
score += name1.count("v") + name2.count("v")
score += name1.count("e") + name2.count("e")

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")