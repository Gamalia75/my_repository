# 2.	Напишіть програму, яка б приймала список з числами та перевіряла чи всі числа в ньому унікальні.
# Реалізуйте у функції декілька обробок виключень.

def unick_numbers(list):
    try:
        for i in list:
            x = list.index(i)+1
            for n in range(x, len(list)):
                if i != list[n]:
                    flag = "Числові елементи в списку унікальні "
                    if list[n] != 0:
                        check = i / list[n]
                    elif list[n] == 0 and i != 0:
                        check = list[n] / i
                    elif list[n] == 0 and i == 0:
                        check = list[n] * i
                elif i == list[n]:
                    flag = "Числові елементи в списку не унікальні "
                    break
        return flag
    except TypeError as ex:
        print(f"Не всі елементи списку є числами! {ex} ")
    except Exception as ex:
        print(f"Невідома помилка! {ex}")


print(lst1 := [1, 2, 7, 9, 55, "0", 55])
print(unick_numbers(lst1))
print(f"{'#'*100} \n")

print(lst2 := [1, 2, 7, 9, 55, 3, 0])
print(unick_numbers(lst2))
print(f"{'#'*100} \n")

print(lst3 := [1, 2, 7, 9, 55, 2, 7, 0])
print(unick_numbers(lst3))
print(f"{'#'*100} \n")
