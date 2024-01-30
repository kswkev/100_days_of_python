
SELECTION_PROMPT_TEXT = "What would you like? (espresso/latte/cappuccino):"

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
continue_processing = True


def user_prompt():
    """Prompts the user to select an option from the menu and returns that selection"""
    selection = input(SELECTION_PROMPT_TEXT).lower()
    return selection


def print_report():
    """Prints a report detailing the current values of water, milk, coffee and profit"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Profit: ${profit}")


def sufficient_resources_available(selection):
    """Takes in the selection and checks the resources required to make that selection are currently available"""
    item_ingredients = MENU[selection]["ingredients"]
    required_water = 0
    required_milk = 0
    required_coffee = 0
    sufficient = True

    for key in item_ingredients:
        if key == "water":
            required_water = item_ingredients["water"]
        elif key == "milk":
            required_milk = item_ingredients["milk"]
        elif key == "coffee":
            required_coffee = item_ingredients["coffee"]

    if required_water > resources["water"]:
        sufficient = False
        print("Sorry there is not enough water.")

    if required_milk > resources["milk"]:
        sufficient = False
        print("Sorry there is not enough milk.")

    if required_coffee > resources["coffee"]:
        sufficient = False
        print("Sorry there is not enough coffee.")

    return sufficient


def process_coins():
    """Prompts the user for the number of quarters, dimes, nickles and pennies, then returns the total value"""
    total = 0
    total += int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def provide_change_if_required(entered, required):
    """If the entered amount exceeds the required amount, the different is outputted"""
    if entered > required:
        refund = entered - required
        print(f"Here is ${round(refund, 2)} change")


def make_drink(selection):
    """Deducts the required water, milk and coffee from the current stock"""
    item_ingredients = MENU[selection]["ingredients"]
    for key in item_ingredients:
        if key == "water":
            resources["water"] -= item_ingredients["water"]
        elif key == "milk":
            resources["milk"] -= item_ingredients["milk"]
        elif key == "coffee":
            resources["coffee"] -= item_ingredients["coffee"]

    print(f"Here is your {selection}")


def process_selection(selection):
    """Goes through the steps required to make a coffee"""
    sufficient_resources = sufficient_resources_available(selection)
    if sufficient_resources:
        print("Please enter some coins")
        total_amount_entered = process_coins()
        amount_required = MENU[selection]["cost"]
        if total_amount_entered < amount_required:
            print(f"Sorry that's not enough money, ${total_amount_entered} refunded")
        else:
            provide_change_if_required(total_amount_entered, amount_required)
            global profit
            profit += amount_required
            make_drink(selection)


while continue_processing:
    user_selection = user_prompt()

    if user_selection == "off":
        continue_processing = False
    elif user_selection == "report":
        print_report()
    elif user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":
        process_selection(user_selection)
