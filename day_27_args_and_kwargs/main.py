def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,5,10))
print(add(3,2))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(5, add=2, multiply=3))


class Car:

    def __init__(self, **car_config):
        self.make = car_config.get("make")
        self.model = car_config.get("model")
        self.colour = car_config.get("colour")
        self.seats = car_config.get("seats")

my_car = Car(make="Nissan")
print(my_car.make)