# 3.	Напишіть клас Parallelogram, який приймає два аргументи width і length
# і метод get_area, який вираховує площу паралелограму.
# Успадкуйте від нього клас Square, перевизначіть в ньому метод get_area
# таким чином, щоб він вираховував площу квадрату.

class Parallelogram:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def get_area(self):
        return self._width * self._length

class Square(Parallelogram):
    def get_area(self):
        return self._width * self._width

a = Parallelogram(5, 10)
print(a.get_area())

b = Square(5, 5)
print(b.get_area())
