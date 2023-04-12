# 1.	Напишіть функцію, яка б приймала номер місяця, а вертала його назву.
# Реалізуйте у функції декілька обробок виключень.
def month_num(num):
    try:
        if num == 1:
            print(f"{num} місяць - Січень")
        if num == 2:
            print(f"{num} місяць - Лютий")
        if num == 3:
            print(f"{num} місяць - Березень")
        if num == 4:
            print(f"{num} місяць - Квітень")
        if num == 5:
            print(f"{num} місяць - Травень")
        if num == 6:
            print(f"{num} місяць - Червень")
        if num == 7:
            print(f"{num} місяць - Липень")
        if num == 8:
            print(f"{num} місяць - Серпень")
        if num == 9:
            print(f"{num} місяць - Вересень")
        if num == 10:
            print(f"{num} місяць - Жовтень")
        if num == 11:
            print(f"{num} місяць - Листопад")
        if num == 12:
            print(f"{num} місяць - Грудень")
        if num > 12 or num < 1:
            print(f"{num} - некоректне значення місяця 1-12")
    except TypeError as ex:
        print(f'Невірний тип даних: {ex}')
    except Exception as ex:
        print(f'Невідома помилка: {ex}')
    finally:
        print("*"*50)

month_num(12)
month_num("2")
month_num(23)
