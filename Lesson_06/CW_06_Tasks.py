# Завдання
# Написати рекурсивну функцію, яка б вертала ряд Фібоначі у вигляді списку цифр.
# Функція повинна мати вхідний цифровий параметр максимального значення у списку.
el1 = 1
el2 = 1
n = int(input("Введіть максимальне значення для ряда Фібоначі: "))
i = 0
sum_el = 0
while sum_el < n:
    sum_el = el1 + el2
    if sum_el > n:
        break
    print(sum_el)
    el1 = el2
    el2 = sum_el
    i += 1
if i == 1:
    print(f"Значення 1 елемента  - {el1}")
else:
    print(f"Значення {i+2} елемента  - {el2}")


print("="*50)
#
# Написати функцію, яка б вираховувала кількість від’ємних чисел
# у списку [ 20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4].
list = [20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4]
count_minus = 0
for i in range(0, len(list)):
    if list[i] < 0:
        print(list[i])
        count_minus += 1
print(f"Кількість відємних чисел: {count_minus}")


print("="*50)
#
# Написати функцію визначення максимального елементу списку.
list = [20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4]
max_el = int(list[0])
for i in range(1, len(list)):
    if max_el < int(list[i]):
        max_el = int(list[i])
print(f"Максимальний елемент у списку {list}: {max_el}")

print("="*50)
#
# Написати функцію, яка б здійснювала реверсування цілого числа.
# Наприклад: число 298276534 перетворювалося б на 435672892.

num = 298276534
print(num)
list1 = []
new_num = 0
while num >0:
    y = num % 10
    num = num // 10
    list1.append(y)
print(list1)
for i in range(0, len(list1)):
    x = int(list1[i]) * (10**(len(list1)-i-1))
    new_num += x
print(new_num)

print("="*50)
#
# Написати рекурсивну функцію, яка вертає суму чисел, що є елементами списку.
def get_summ(list):
    if x < len(list):
        sum += int(list[x])
        x += 1
    get_summ(list)

list = [20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4]
sum = 0
x = 0
