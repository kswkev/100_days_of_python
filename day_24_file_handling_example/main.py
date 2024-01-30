# Opening an existing file
file = open("existing_file.txt")
contents = file.read()
print(contents)
file.close()

# Opening an existing file using the with keyword
with open("existing_file.txt") as file:
    contents = file.read()
    print(contents)

# Creating a new file
with open("new_file.txt", mode="w") as file:
    file.write("Here's some text")

# Appending text to an exisiting file
with open("new_file.txt", mode="a") as file:
    file.write("\n and some more")
