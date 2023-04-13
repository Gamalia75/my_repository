import copy


'''
def my_function(arg):
    return arg


print(my_function(2))
'''

'''
x = lambda a: a * 3
print(x(10))  # 30

print("String is an argument for print function")

int_variable = int("1")  # Returns int value
'''

'''
def my_function(a):
    a += 1


print(my_function(2))
'''


'''
def my_function(a):
    pass


print(my_function(2))
'''


'''
def my_function(a=1, b=2, c=3):
    print(a)
    print(b)
    print(c)


print(my_function(b=8))
'''


'''
def my_function(*args):
    for i in args:
        print(i)


print(my_function(1, 2, 3))
'''


'''
def my_function(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


my_function(a=1, b=2, c=3)
'''


'''
def my_function(a, b, *, flag=True):
    print(flag)


my_function(1, 2, flag=True)
'''


'''
a = 1


def my_function(a):
    a+=1
    print(a)

my_function(copy.copy(a))
print(a)
'''


'''
def descending(i):
    while i > 0:
        yield i
        i -= 1

for i in descending(10):
    print(i)
'''


'''
l = list(range(10))
print(type(l))
print(l[0])
'''

'''
def recursion():
    password = input("Type pass: ")
    if password != "12345":
        recursion()


recursion()
'''
####################################################
a = lambda s: s%3
print(a(101))

print("="*100)
#######################################################
a = 75
def my_function(a):
    b=0
    if a < 100:
        b = 100
    else:
        b=50
    return b

print(my_function(a))

print("="*100)
######################################################

x = lambda a: 100 if a <100 else 50
print(x(a))
print(x(101))

print("="*100)
######################################################

def prnt_lst(*args):    # Функції, де не вказано параметр RETURN називаються процедурами
    print(type(args))
    for i in args:
        print(i)

sss = prnt_lst("dhgfh", 113, True)
print(sss)
print(type(sss))

print("="*100)
######################################################
def print_list(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print_list(f=12, h="flkjldk")

print("="*100)
###################################################### Функції генератори - замість RETURN пишемо YIELD
def descending(i):
    while i > 0:
        yield i
        i -= 1

for i in descending(10):
    print(i)

print("="*100)
###################################################### Рекурсія
# def recursion():
#     password = input("Type pass: ")
#     if password != "12345":
#         recursion()
#
# recursion()

###################################################### Рекурсія

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))

# Напишіть функцію, яка приймає число менше 100 та за допомогою рекурсії
# збільшує його на 1, поки число не дорівнює 100. Не використовуйте цикли.

def value_100(a):
    print(a)
    if a < 100:
        a += 1
        value_100(a)
    else:
        print("Finish!")

value_100(95)

print("="*100)
###################################################### Задача

# Напишіть функцію, яка приймає довільну кількість аргументів,
# перевіряє кожен з них та повертає False, якщо якийсь з аргументів не є рядком.
# Якщо всі аргументи є рядками, то функція повертає True.

def check_str(*args):
    flag = True
    for i in args:
        if  isinstance(i, str):
            flag = True
        else:
            flag = False
            break
    return flag

print(check_str("hsdkjhk", "sdjhjhg", 4, "3"))
print(check_str("hsdkjhk", "sdjhjhg", "3"))

# Варіант 2
def check_str1(*args):
    for i in args:
        if not isinstance(i, str):
            return False
            break
    return True

print("="*100)
######################################################
print(check_str1("hsdkjhk", "sdjhjhg", 4, "3"))
print(check_str1("hsdkjhk", "sdjhjhg", "3"))

print("="*100)
######################################################

# Напишіть функцію, яка приймає один аргумент — сторону квадрата.
# Функція має повертати його площу, периметр та діагональ.

def square(a):
    l = [a * a, 4 * a, 2 ** 0.5 * a]
    return l

print(square(2))
