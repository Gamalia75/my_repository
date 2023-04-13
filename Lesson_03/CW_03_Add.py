# Задача FizzBuzz
# Виведіть на екран числа від 1 до 100.
# Замість чисел, які кратні 3, виведіть слово Fizz
# Замість чисел, які кратні 5, виведіть слово Buzz
# Замість чисел, які кратні 15, виведіть слово FizzBuzz

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
        continue

    if i % 5 == 0:
        print("Buzz")
        continue

    if i % 3 == 0:
        print("Fizz")
        continue
    print(i)

print("="*100)

# Створіть список з рядків. За допомогою List Comprehension отримайте з
# нього новий список рядків, які не довші за 5 символів та починаються з голосних літер.
str = ("Ahhh ljsdfgkjds offg fdsjklk ekkf Ejjj kjgldfg")
letters = ["a", "e", "o", "y", "i", "A", "E", "O", "Y", "I"]
str_new = [i for i in str.split(" ") if len(i)<=5 and i[0] in letters]
print(str)
print(str_new)

print("="*100)


# Використання моржових операторів
my_list = ["I", "Love", "Python"]
pop_item = my_list.pop(0)
print(pop_item)
print(my_list[0])

print(my_list := ["I", "Love", "Python"][0])  # Використання моржових операторів

print("="*100)
my_str = "python"
print(my_str.upper())

print(my_str := "python".upper())   # Використання моржових операторів

my_str = "P Y T H O N"
print(my_str)
print(my_str.replace(" ", ""))
print(my_str := "P Y T H O N".replace(" ", ""))   # Використання моржових операторів
print(type(my_str := 1.2))   # Використання моржових операторів

# Створіть цикл, який роздруковує у консолі всі високосні роки з початку минулого століття.
for i in range(1900, 2022):
    if i % 4 ==0:
        print(f"{i} високосний рік")
