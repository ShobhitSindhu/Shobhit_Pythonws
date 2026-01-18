class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand}: Vroom vroom!")

class ElectricCar(Car):
    def drive(self):
        print(f"{self.brand}: Silent electric hum")

class Truck(Car):
    def drive(self):
        print(f"{self.brand}: Heavy diesel engine")

garage = [Car("Toyota"), ElectricCar("Tesla"), Truck("Ford")]

for vehicle in garage:
    vehicle.drive()
