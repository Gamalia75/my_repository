# # Написати рекурсивну функцію, яка вертає суму чисел, що є елементами списку.

# list = [20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4]


# def sum_numbers(numbers):
#     if len(numbers) == 0:
#         return 0
#     return numbers[0] + sum_numbers(numbers[1:])
#
# list = [20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4]
# print(sum_numbers(list))
# 15


Massiv = [1, 2, 3, 4, 5]
Summa = 0

def DSumma(x):
    global Summa
    if x == len(Massiv):
        return
    Summa += Massiv[x]
    DSumma(x + 1)


DSumma(0)
print('\nSumma = ', Summa)

list = [20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4]
print(list)
print(list[3:])