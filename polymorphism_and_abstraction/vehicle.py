from abc  import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def refuel(self, fuel):
        pass

    @abstractmethod
    def drive(self, distance):
        pass

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption + 0.9

    def drive(self, distance):
        if self.fuel_quantity >= distance * self.fuel_consumption:
            self.fuel_quantity -= distance * self.fuel_consumption


    def refuel(self, fuel):
        self.fuel_quantity += fuel






class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption + 1.6

    def drive(self, distance):
        if self.fuel_quantity >= distance * self.fuel_consumption:
            self.fuel_quantity -= distance * self.fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
