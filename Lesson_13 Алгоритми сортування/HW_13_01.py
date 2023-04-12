# 1. Створіть три списки: int_list, float_list і str_list.
# Користуючись пакетами рандомізації, заповніть словник
# int_list випадковими цілочисельними значеннями, у кількості 5000 елементів,
# в діапазоні від 0 до 1000.
# Заповніть словник float_list випадковими значеннями,
# у кількості 5000 елементів, в діапазоні від 0.1 до 100.0.
# Також заповніть словник str_list випадковими словами, теж у кількості 5000 елементів.

import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())

print("Int List:", int_list)
print("Float List:", float_list)
print("String List:", str_list)
