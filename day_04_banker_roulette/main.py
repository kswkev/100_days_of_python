names_string = "Angela, Ben, Jenny, Michael, Chloe"

names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

randomIndex =  random.randint(0, len(names) - 1)

print(f"{names[randomIndex]} is going to buy the meal today!")