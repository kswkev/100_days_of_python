class Car:
    def __init__(self):
        self.wheels = 4

    def refuel(self):
        print("I need fuel")


class PetrolCar(Car):
    def __init__(self):
        super().__init__()

    def refuel(self):
        super().refuel()
        print("Filling up with petrol")


class DieselCar(Car):
    def __init__(self):
        super().__init__()

    def refuel(self):
        super().refuel()
        print("Filling up with diesel")

class ElectricCar(Car):
    def __init__(self):
        super().__init__()

    def refuel(self):
        super().refuel()
        print("Charging up")

class HybridCar(Car):
    def __init__(self):
        super().__init__()

    def refuel(self):
        super().refuel()
        print("Charging up")
        print("Filling up with petrol")