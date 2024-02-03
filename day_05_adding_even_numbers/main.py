target = int(input("Enter a number between 0 and 1000")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
calculated_sum = 0
for number in range(0, target+1, 2):
    calculated_sum += number


print(calculated_sum)