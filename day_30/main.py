# Exception examples

# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# Traceback (most recent call last):
#   File "C:\Dev\python\100_days_of_python\day_30\main.py", line 5, in <module>
#     with open("a_file.txt") as file:
#          ^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'


# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existant-key"]

# Traceback (most recent call last):
#   File "C:\Dev\python\100_days_of_python\day_30\main.py", line 16, in <module>
#     value = a_dictionary["non-existant-key"]
#             ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
# KeyError: 'non-existant-key'


# IndexError
# fruits = ["Apple", "Pear", "Banana"]
# my_fruit = fruits[3]

# Traceback (most recent call last):
#   File "C:\Dev\python\100_days_of_python\day_30\main.py", line 27, in <module>
#     my_fruit = fruits[3]
#                ~~~~~~^^^
# IndexError: list index out of range


# TypeError
# text = "ABC"
# print(text + 5)

# Traceback (most recent call last):
#   File "C:\Dev\python\100_days_of_python\day_30\main.py", line 38, in <module>
#     print(text + 5)
#           ~~~~~^~~
# TypeError: can only concatenate str (not "int") to str


# try, except, else, finally example
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["non-existant-key"])
except FileNotFoundError as file_error:
    print(f"Error: {file_error}, creating file")
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as key_error:
    print(f"Key {key_error} does not exist")
else:
    contents = file.read()
    print(contents)
finally:
    file.close()


# raising an error
try:
    height = float(input("Please enter your height in meters: "))
    weight = float(input("Please enter your weight in kg: "))

    if height >= 3:
        raise ValueError("Humans aren't 3 meters or taller")
except ValueError:
    print("Please enter a height less than 3 meters")
else:
    bmi = weight / height ** 2
    print(bmi)

