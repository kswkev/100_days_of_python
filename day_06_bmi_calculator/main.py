# 1st input: enter height in meters e.g: 1.65
height = input("enter height in meters e.g: 1.65: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("enter weight in kilograms e.g: 72: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = float(weight) / float(height) ** 2
print(int(bmi))