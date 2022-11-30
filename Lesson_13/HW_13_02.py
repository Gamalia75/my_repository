# 2. Додайте до попередньої програми код, будь-якого алгоритму сортування.
# Додайте функцію, яка б обраховувала середній час роботи алгоритму сортування.
# Функція повинна приймати список і кількість ітерацій циклів сортування,
# а повертати середній час роботи алгоритму сортування.

import random
import time
from random_words import RandomWords


# Bubble Sort Algorithm
def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
               data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
               swapped = True
        if not swapped:
            break
    print("Bubble Sort: ", data)


num = input("Введіть кількість ітерацій: ")
x = int(num)

print(f"Сортуємо цілі числа \n")
time_sum = 0
for i in range(x):
    int_list = []
    for n in range(0, 5000):
        int_list.append(random.randint(0, 1000))
    print("Int List:", int_list)
    cur_time = time.time()
    bubble_sort(int_list)
    time1 = time.time() - cur_time
    time_sum += time1
    print(f"Duration time attempt {i+1}: {time1} \n")
avg_time1 = time_sum / x
print(f"Середній час сортування для цілих чисел: {avg_time1} секунд \n")

print(f"Сортуємо числа з плаваючою крапкою \n")
time_sum = 0
for i in range(x):
    float_list = []
    for n in range(0, 5000):
        float_list.append(random.uniform(0.1, 100.0))
    print("Float List:", float_list)
    cur_time = time.time()
    bubble_sort(float_list)
    time1 = time.time() - cur_time
    time_sum += time1
    print(f"Duration time attempt {i+1}: {time1} \n")
avg_time2 = time_sum / x
print(f"Середній час сортування для чисел з плаваючою крапкою: {avg_time2} секунд \n")

print(f"Сортуємо слова \n")
time_sum = 0
for i in range(x):
    str_list = []
    w = RandomWords()
    for n in range(0, 5000):
        str_list.append(w.random_word())
    print("Str List:", str_list)
    cur_time = time.time()
    bubble_sort(str_list)
    time1 = time.time() - cur_time
    time_sum += time1
    print(f"Duration time attempt {i+1}: {time1} \n")
avg_time3 = time_sum / x
print(f"Середній час сортування слів: {avg_time3} секунд \n")

print("*"*100)
print(f"Середній час сортування для цілих чисел: {avg_time1} секунд")
print(f"Середній час сортування для чисел з плаваючою крапкою: {avg_time2} секунд")
print(f"Середній час сортування слів: {avg_time3} секунд")
print("*"*100)
