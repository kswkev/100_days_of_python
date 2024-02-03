fruits = eval('["Apple", "Pear", "Orange"]')
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
      fruit = fruits[index]
    except IndexError:
      fruit = "Fruit"
    print(fruit + " pie")


# 🚨 Do not change the code below
make_pie(4)