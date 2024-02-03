# Write your code below this line 👇
def prime_checker(number):
    divisible = False
    i = 2

    while i < number and divisible == False:
        if number % i == 0:
            divisible = True
        i += 1

    if divisible:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))  # Check this number
prime_checker(number=n)