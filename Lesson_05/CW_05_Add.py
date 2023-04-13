# Створити функцію last_lines() яка приймає шлях до файлу та
# кількість останніх рядків та виводить їх у консолі
def last_lines(path, rows):
    with open(path, "r", encoding="utf8") as f:
        row_s = []
        row_str = str(f.read())
        row_s = row_str.split("\n")
        print(row_s)
        print(len(row_s))
        print(rows)
        print(len(row_s)-rows)
        print(row_s[-rows:])
        print(row_s[len(row_s)-rows:])
        print(row_s[(len(row_s)-rows): len(row_s)])
        print(row_s[12:16])

last_lines("test.txt", 4)

# Написати програму, яка створює новий файл і записує у нього усі числа
# від 0 до 100, що кратні 5
# def numbers_100(fn:str):
#     file = open(fn, "x", encoding="utf8")
#     file.close()
#     with open(fn, "w", encoding="utf8") as f:
#         for i in range(1, 101):
#             if i % 5 == 0:
#                 f.write("\n" + str(i))
#
# numbers_100("124.txt")
print("="*100)
################################################################################
# Створити функцію, яка отримує шлях до файлу та повертає кількість рядків у ньому
def row_num(path):
    with open(path, "r", encoding="utf8") as f:
        row_s = []
        row_str = str(f.read())
        row_s = row_str.split("\n")
        print(f"Кількість рядків у файлі {path} = {len(row_s)}")

row_num("123.txt")

print("="*100)
################################################################################
# Створити функцію, яка приймає шлях до каталогу та повертає список з його вмістом
def list_dir(path):
    import os
    print(os.listdir(path))

list_dir("C:\Python\Sturtup_Academy")