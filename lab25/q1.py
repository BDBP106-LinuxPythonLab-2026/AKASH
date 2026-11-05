class Car:
    showroom = 'NewAge'

    @classmethod
    def change_showroom(cls, new_name):
        cls.showroom = new_name

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.max_speed = 200
        self.started = False


toyota_camry = Car("Toyota", "Camry", "2020", "Blue")
print(toyota_camry.make)
print(toyota_camry.model)
print(toyota_camry.year)
print(toyota_camry.color)

ford_mustang = Car("Ford", "Mustang", "2022", "Black")
print(ford_mustang.make)
print(ford_mustang.model)
print(ford_mustang.year)
print(ford_mustang.color)

try:
    print(Car.make)
except AttributeError as e:
    print(f"Error caught: {e}")

print(Car.__dict__)

# showroom = 'NewAge'

# @classmethod
# def change_showroom(cls, new_name):
#     cls.showroom = new_name

Car.change_showroom("FutureMotors")
print(Car.__dict__)
#
print(toyota_camry.__dict__)
