# 1.	Напишіть клас автомобіля з атрибутами: марка, колір, об’єм двигуна.
# Та методами: їхати вперед, їхати назад.
# Напишіть ще один клас автомобіля, який є успадкованим від першого.
# Додайте в нього методи повороту праворуч та ліворуч.

class Car:
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume

    def drive_forward(self):
        print("Drive forward")

    def drive_backward(self):
        print("Drive backward")


class Car2(Car):
    def turn_left(self):
        print('Turn left')

    def turn_right(self):
        print('Turn right')


print(f"\n  Для класа Car  \n")

car = Car('Volvo', 'black', 3.0)
car.drive_backward()
car.drive_forward()

print(f"\n  Для класа Car2  \n")

car2 = Car2('Audi', 'white', 3.5)
car2.turn_left()
car2.drive_backward()
car2.turn_right()
car2.drive_forward()
