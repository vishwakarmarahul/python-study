
'''
:: Multi-Level Inheritance
Vehicle
 |
Car
|
SportsCar
'''

class Vehicle:
    name = None
    brand = None
    speed = None
    color = None
    power = None
    fuel_type = None
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def drive(self):
        print('driving..')
        return True

class Car(Vehicle):
    types = None
    seating = None
    wheel_size = None
    def __init__(self, name, brand):
        super().__init__(name, brand)

car = Car('mycar', 'bmw')
print(car.drive())

# class SportsCar():
#     def drive2(self):
#         print('Diving..')
#
# class SemiSports(Car, SportsCar):
#     pass
#
# o = SemiSports()
# print(o)





