age = input("Enter you age: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
weeksAt90 = 90 * 52
currentWeeks = int(age) * 52
weeksLeft = weeksAt90 - currentWeeks

print(f"You have {weeksLeft} weeks left.")