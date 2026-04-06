# CLASS AND OBJECTS 
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    def get_brand(self):
        return self.__brand + " !"
    def fullName(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol"
    @staticmethod
    def general_description():
        return "This is a car."
    
    @property
    def model(self):
        return self.__model;

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"

# Encapsulation
# If any variable has two underscore __ then it will be private. 

# Ploymorphism
# Here the same method name called but working is different in both the classes. This is called method overriding. 

my_car = Car("Toyota", "Supra")
# my_car.model = "Corolla"
print(my_car.model)


# safari = Car("Tata", "Safari")
# print(safari.fuel_type())

# Tesla = ElectricCar("Tesla", "Model S", "85 kWh")
# print(Tesla.fuel_type())

# my_tesla = ElectricCar("Tesla", "Mode s","85kwh")
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.fullName())

# my_car = Car("Toyota", "Supra")
# print(my_car.brand)
# print(my_car.fullName())

