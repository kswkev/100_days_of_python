# Calculator

# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


def listKeys(dict, delim):
    output = ""
    for key in dict:
        output += key + delim

    return output


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

continue_calculating = "y"
num1 = int(input("What's the first number?: "))
while continue_calculating == "y":
    print(listKeys(operators, ","))
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the next number?: "))
    answer = operators[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    num1 = answer