import car

# normal = car.Car()
# normal.refuel()
#
# petrolCar = car.PetrolCar()
# petrolCar.refuel()
#
# dieselCar = car.DieselCar()
# dieselCar.refuel()
#
# electricCar = car.ElectricCar()
# electricCar.refuel()
#
# hybridCar = car.HybridCar()
# hybridCar.refuel()

cars = [car.Car, car.PetrolCar, car.DieselCar, car.ElectricCar, car.HybridCar]

for type in cars:
    vehicle = type()
    vehicle.refuel()