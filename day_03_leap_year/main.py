# Which year do you want to check?
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
leap = False

if year % 4 == 0:
  leap = True
  if year % 100 == 0:
    leap = False
    if year % 400 == 0:
      leap = True

if leap:
  print("Leap year")
else:
  print("Not leap year")