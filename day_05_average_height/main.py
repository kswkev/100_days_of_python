# Input a Python list of student heights
student_heights = input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
count = 0
total_height = 0
for height in student_heights:
    total_height += height
    count += 1

average_height = int(round(total_height / count, 0))

print(f"total height = {total_height}")
print(f"number of students = {count}")
print(f"average height = {average_height}")