# *************************** Q:1 *****************************

# Q:1 - Basic class and object creation ?

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    
    def get_brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model
        
    def fullName(self):
        return f"{self.__model} {self.__brand}"   
    
    def fuel_type(self):
        return "petrol diesel"
    
    @staticmethod   
    def description():
        return "this is a car"

class Electric_car(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
    def fuel_type():
        return "petrol diesel"
    
my_car = Car("car1","car2")

my_car2 = Electric_car("tesla","Model S","67kwh")

print(my_car.model)
    