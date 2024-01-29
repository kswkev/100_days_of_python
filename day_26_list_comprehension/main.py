def printLists(message, oldList, newList):
    print(message)
    print(f"Old list: {oldList}")
    print(f"New list: {newList}")
    print("\n")

# Create a new list with 1 added to the value of each entry in the existing list
numbers = [1,2,3]
new_numbers = [number + 1 for number in numbers]
printLists("New list with 1 added", numbers, new_numbers)

# Double the numbers 1-4 from a range
doubled = [n*2 for n in range(1, 5)]
print(doubled)

# Create a new list of the names with have fewer than 5 characters
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
printLists("New list with names shorted than 5 characters", names, short_names)

# Take numbers from a list and create a new list with only the even numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [number for number in numbers if number % 2 == 0]
printLists("New list with even numbers only", numbers, even_numbers)

# Use a function to calculate the total sum of the preceeding entries
total = 0
def calculate_total(number):
    global total
    total += number
    return total
numbers = [1,2,3,4,5,6,7,8,9,10]
running_total = [calculate_total(number) for number in numbers]
printLists("Running sum total", numbers, running_total)

# Nest list comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
doubled_even_numbers = [n*2 for n in [number for number in numbers if number % 2 == 0]]
printLists("Doubled numbers", numbers, doubled_even_numbers)

# Use a function to determine if an entry should be included
def is_even(number):
    return number % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [number for number in numbers if is_even(number)]
printLists("Even numbers using a function", numbers, even_numbers)

# Use a higher order function to find odd and even numbers
def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 == 1

def conditional(number, function):
    return function(number)

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [number for number in numbers if conditional(number, is_even)]
odd_numbers = [number for number in numbers if conditional(number, is_odd)]
printLists("Even numbers using a higher order function", numbers, even_numbers)
printLists("Odd numbers using a higher order function", numbers, odd_numbers)