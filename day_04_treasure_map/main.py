line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

col = 0
if position[0].lower() == "a":
  col = 0
elif position[0].lower() == "b":
  col = 1
else:
  col = 2

row = int(position[1])-1
map[row][col] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")