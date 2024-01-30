#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
#for i in range(1, nr_letters+1):
#  password += letters[random.randint(0, len(letters)-1)]

#for i in range(1, nr_symbols+1):
#  password += symbols[random.randint(0, len(symbols)-1)]

#for i in range(1, nr_numbers+1):
#  password += numbers[random.randint(0, len(numbers)-1)]


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
remaing_letters = nr_letters
remaing_symbols = nr_symbols
remaing_numbers = nr_numbers

while remaing_letters + remaing_symbols + remaing_numbers > 0:
  character_type = random.randint(1, 3)

  if character_type == 1 and remaing_letters > 0:
    password += letters[random.randint(0, len(letters)-1)]
    remaing_letters -= 1

  elif character_type == 2 and remaing_symbols > 0:
    password += symbols[random.randint(0, len(symbols)-1)]
    remaing_symbols -= 1

  elif character_type == 3 and remaing_numbers > 0:
    password += numbers[random.randint(0, len(numbers)-1)]
    remaing_numbers -= 1

print(password)