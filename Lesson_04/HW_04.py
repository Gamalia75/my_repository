# 1.	Напишіть функцію, яка приймає номер місяця та повертає рядок з назвою пори року, до якої цей місяць відноситься.
print("1.	Напишіть функцію, яка приймає номер місяця та повертає рядок з назвою пори року, до якої цей місяць відноситься.")

def seasons(m):
    if m in (1, 2, 12):
        mn = "Winter"
    elif m in (3, 4, 5):
        mn = "Spring"
    elif m in (6, 7 , 8):
        mn = "Summer"
    elif m in (9, 10 ,11):
        mn = "Fall"
    else:
        mn = "Wrong number of mounth"
    return mn

m = int(input("Введіть номер місяця: "))
print(seasons(m))

print("="*100)

# 2.	Напишіть функцію, яка приймає довільну кількість словників, збирає їх в один словник та повертає його.
print("2.	Напишіть функцію, яка приймає довільну кількість словників, збирає їх в один словник та повертає його.")

def dict_all(*args):
    my_dict = {}
    for i in args:
        my_dict.update(i)
    return my_dict

my_dict1 = {4: "Four", 6: "Six"}
print(my_dict1)
my_dict2 = {1: "One", 2: "Two"}
print(my_dict2)
my_dict3 = {"Abc": "Cba", 123: True}
print(my_dict3)
print(dict_all(my_dict1, my_dict2, my_dict3))

print("="*100)

# 3.	Напишіть функцію, яка перевіряє, чи є слово паліндромом та повертає відповідно True чи False. Паліндром - це слово,
# яке однаково читається зліва направо та справа наліво. Наприклад, "випив".
print("3.	Напишіть функцію, яка перевіряє, чи є слово паліндромом та повертає відповідно True чи False. Паліндром - це слово, яке однаково читається зліва направо та справа наліво. Наприклад, випив.")

def polindrom(w):
    n = 0
    while n < len(w):
        if w.upper()[n] == w.upper()[len(w) - n - 1]:
            print(w.upper()[n], " = ", w.upper()[len(w) - n - 1])
            n += 1
            continue
        else:
            print(w.upper()[n], " != ", w.upper()[len(w) - n - 1])
            return False
        break
    return True

str = input("Введіть слово: ")
print(f"Чи є слово поліндром: {polindrom(str)}")

print("="*100)

# 4.	Напишіть функцію, яка приймає ціле число та повертає суму всіх його цифр. Наприклад, 437. 4+3+7=14.
print("4.	Напишіть функцію, яка приймає ціле число та повертає суму всіх його цифр. Наприклад, 437. 4+3+7=14.")

def sum_num(xyz):
    x = abs(xyz)
    sum = 0
    while x > 0:
        y = x % 10
        sum += y
        print(y)
        x = x // 10
    return sum

xyz = int(input("Введіть ціле число: "))
print(f"Сума цифр числа {xyz} = {sum_num(xyz)}")

print("="*100)

# 5.	Напишіть функцію, яка приймає рядок та повертає літеру, яка зустрічається в ньому найчастіше.
print("5.	Напишіть функцію, яка приймає рядок та повертає літеру, яка зустрічається в ньому найчастіше.")

def max_symbol_count(str):
    max_count = 0
    max_symbol = ""
    for i in str:
        if max_count < str.count(i):
            max_symbol = i
            max_count = str.count(i)
    return max_symbol, max_count

str = input("Введіть рядок: ")
print(f"Символ: {max_symbol_count(str)[0]} зустрічається {max_symbol_count(str)[1]} разів")

print("="*100)
############################################################
# Варіант якщо виводити декілька значень які задовольняють умовам

def max_count(string:str):
    temp_dict = dict()
    symbols = set(string)
    depricated_symbols = [" ", ".", ",", ":", ";", "'", '"', "!", "?", "\\",
                          "/", "|", "*", "(", ")", "{", "}", "[", "]", "\n"]
    for i in symbols:
        if i not in depricated_symbols:
            temp_dict.update({i: string.count(i)})
    max_val = max(temp_dict.values())
    final_dict = {k:v for k, v in temp_dict.items() if v == max_val}
    return final_dict

s = max_count(str)
print(s)
