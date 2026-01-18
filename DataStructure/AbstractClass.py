from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def drive(self):
        pass

class PetrolCar(Vehicle):
    def drive(self):
        print(f"{self.brand} uses petrol")

class ElectricCar(Vehicle):
    def drive(self):
        print(f"{self.brand} uses battery")

v1 = PetrolCar("Toyota")
v2 = ElectricCar("Tesla")

v1.drive()
v2.drive()
