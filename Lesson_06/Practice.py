print("="*100)
print("Задача №1: «Вгадай число»" + "\n")

import random
def guess_number():
    guess_num = random.randint(1, 100)
    min_num = 1
    max_num = 100
    for i in range(1, 7):
        print("="*100)
        print(f"Спроба №: {i}")
        at_num = int(input(f"Введіть число від {min_num} до {max_num}: "))
        if at_num == guess_num:
            print("=" * 100)
            print(f"Ви вгадали число {guess_num} і використали {i} спроб")
            break
        elif at_num > guess_num and i < 6:
            max_num = at_num - 1
            print(f"Менше. Загадане число від {min_num} до {max_num}")
        elif at_num < guess_num  and i < 6:
            min_num = at_num + 1
            print(f"Більше. Загадане число від {min_num} до {max_num}")
        elif at_num != guess_num and i == 6:
            print("=" * 100)
            print(f"Ви не вгадали! Було загадано число: {guess_num}")

guess_number()
