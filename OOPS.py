# CLASS AND OBJECTS 
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def fullName(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Mode s","85kwh")
print(my_tesla.model)
print(my_tesla.fullName())

# my_car = Car("Toyota", "Supra")
# print(my_car.brand)
# print(my_car.fullName())

