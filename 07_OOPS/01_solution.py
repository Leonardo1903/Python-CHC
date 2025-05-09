class Car:
    total_cars = 0
    def __init__(self,brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1
        
    def get_brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model
    
    def fullName(self):
        return f'{self.__brand} {self.__model}'
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are a mode of transport."


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
            
    def fuel_type(self):
        return "Electric"

Car1 = Car("Audi", "Q3")
Car2 = ElectricCar("Tesla", "Model S", "100kWh")


print(f'Car1 brand: {Car1.get_brand()}')
print(f'Car1 model: {Car1.model}')  
print(f'Car1 fullName: {Car1.fullName()}')
print(f'Car1 fuel_type: {Car1.fuel_type()}')
print(f'Car1 general_description: {Car.general_description()}')

print(f'Car1 is instance of Car: {isinstance(Car1, Car)}')
print(f'Car1 is instance of ElectricCar: {isinstance(Car1, ElectricCar)}')

# print(f'Car2 brand: {Car2.__brand}')
print(f'Car2 brand: {Car2.get_brand()}')
print(f'Car2 model: {Car2.model}')
print(f'Car2 battery size: {Car2.battery_size}')
print(f'Car2 fuel_type: {Car2.fuel_type()}')
print(f'Car2 general_description: {Car2.general_description()}')
print(f'Car2 is instance of Car: {isinstance(Car2, Car)}')
print(f'Car2 is instance of ElectricCar: {isinstance(Car2, ElectricCar)}')

print(f'Total cars: {Car.total_cars}')


class Battery:
    def battery_info(self):
        return "Battery info"

class Engine:
    def engine_info(self):
        return "Engine info"

class ElectricCar2(Battery,Engine,Car):
    pass


Car3 = ElectricCar2("BMW", "i3")

print(f'Car3 brand: {Car3.get_brand()}')
print(f'Car3 model: {Car3.model}')
print(f'Car3 fuel_type: {Car3.fuel_type()}')
print(f'Car3 general_description: {Car3.general_description()}')
print(f'Car3 battery_info: {Car3.battery_info()}')
print(f'Car3 engine_info: {Car3.engine_info()}')
print(f'Car3 is instance of Car: {isinstance(Car3, Car)}')
print(f'Car3 is instance of ElectricCar: {isinstance(Car3, ElectricCar)}')
print(f'Car3 is instance of ElectricCar2: {isinstance(Car3, ElectricCar2)}')
print(f'Car3 is instance of Battery: {isinstance(Car3, Battery)}')
print(f'Car3 is instance of Engine: {isinstance(Car3, Engine)}')