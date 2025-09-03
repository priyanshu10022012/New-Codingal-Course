class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_details(self):
        print(f"Vehicle Details:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def show_details(self):
        super().show_details()
        print(f"Doors: {self.doors}")
        print(f"Fuel Type: {self.fuel_type}")

class ElectricCar(Car):
    def __init__(self, make, model, year, doors, battery_capacity):
        super().__init__(make, model, year, doors)
        self.battery_capacity = battery_capacity

    def show_details(self):
        super().show_details()
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        print(f"Range: {self.range} miles")
v = Vehicle("Toyota", "Camry", 2020)
c = Car("Honda", "Civic", 2021, "Petrol", 4, 30)
e = ElectricCar("Tesla", "Model S", 2022, 4, 100)

print("\nVehicle Example:")
v.show_details()
print("\nCar Example:")
c.show_details()
print("\nElectric Car Example:")
e.show_details()