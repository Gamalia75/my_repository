# 2.	Написати програми для реєстрації і авторизації користувача з наступним функціоналом:
# -	отримання в інтерактивному режимі логіну і пароля користувача;
# -	верифікація пароля і його шифрування за алгоритмом обраним алгоритмом шифрування;
# -	запис пари "логін-пароль" у словник з перевіркою на колізії;
# -	авторизація користувача за логіном і паролем.

import hashlib

def write_to_file(file_name : str, dictionary):
    with open(file_name, 'w') as f:
        for k, v in dictionary.items():
           f.write(f'{k} {v}\n')
    f.close()

def read_from_file(file_name : str):
    my_dict = {}
    with open(file_name, mode='r', encoding='utf-8') as f:
       for line in f:
           ls = line.split()
           my_dict[ls[0]] = ls[1]

    return my_dict

def registration():
    while True:
        login = input('Введіть ваш логін: ')
        if login in hash_pass_table:
            print('Такий логін вже існує. Оберіть інший.')
        else:
            while True:
                pass1 = input('Введіть ваш пароль: ')
                pass2 = input('Повторіть ваш пароль: ')
                if pass2 == pass1:
                    pass_hash = hashlib.md5(pass2.encode())
                    hash_pass_table[login] = pass_hash.hexdigest()
                    print("Реєстрація успішна!")
                    write_to_file('pass.txt', hash_pass_table)
                    break
                else:
                    print('Паролі не співпадають. Спробуйте ще раз.')
            break

def login():
    while True:
        login = input('Введіть ваш логін: ')
        if login in hash_pass_table:
            count = 0
            while True and count < 3:
                count += 1
                password = input('Введіть ваш пароль: ')
                pass_hash = hashlib.md5(password.encode())
                if hash_pass_table[login] != pass_hash.hexdigest():
                    if count != 3:
                        print(f"Невірний пароль. Спробуйте ще раз. {3 - count} спроб залишилось.")
                    else:
                        print("Невірний пароль. Доступ заборонено. ")
                else:
                    print("Доступ дозволено.")
                    break
            break

        else:
            print("Невідомий логін.")
            choice = input("Якщо хочете спробувати ще раз - натисніть ( 0 ), якщо хочете зареєструватись - натіснить ( 1 ): ")
            if choice.lower() == '1':
                registration()
                break
            elif choice.lower() == '0':
                continue
            else:
                print("Ви ввели невірний символ.")
            break

choice = input("Для входу натисніть ( 0 ), якщо хочете зареєструватись - натіснить ( 1 ): ")
hash_pass_table = read_from_file('pass.txt')
if choice == "1":
    registration()
elif choice == "0":
    login()
else:
    print("Ви ввели невірний символ!")
