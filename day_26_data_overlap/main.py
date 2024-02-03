with open("file1.txt") as file:
    file1_numbers = [int(character) for character in file.readlines()]

with open("file2.txt") as file:
    file2_numbers = [int(character) for character in file.readlines()]

result = [number for number in file1_numbers if number in file2_numbers]


# Write your code above 👆
print(result)
