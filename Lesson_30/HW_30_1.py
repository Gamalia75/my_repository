# 1.	Написати клас для створення і роботи з хеш-таблицями. Клас повинен містити наступні функції:
# -	створення хеш-таблиці заданої довжини;
# -	пошук, додавання і видалення нових елементів:
# -	друкування хеш-таблиці;
# -	виправлення колізій;

class HashTable:

    def __init__(self, lenth : int):
        self.lenth = lenth
        self.hash_table = [[]] * lenth

    def __str__(self):
        return ''.join(map(str, self.hash_table))

    def hash_func(self, key):
        return key % self.lenth

    def search(self, key):
        index = self.hash_func(key)
        if self.hash_table[index]:
            return self.hash_table[index][self.hash_table[index].index(key) + 1]
        else:
            return None

    def add(self, key : int, data):
        index = self.hash_func(key)
        if not self.hash_table[index]:
            self.hash_table[index] = [key, data]
        else:
            self.hash_table[index].extend([key,data])

    def remove(self, key: int, data):
        index = self.hash_func(key)
        result = self.search(key)
        if result:
            if data in self.hash_table[index]:
                self.hash_table[index].remove(key)
                self.hash_table[index].remove(data)
            else:
                error = ValueError(f"Значення \'{data}\' з ключем ({key}) відсутнє в таблиці.")
                raise error
        else:
            error = KeyError(f"Ключ ({key}) відсутний в таблиці.")
            raise error


print("Створюємо хеш-таблицю довжиною 8")
ht = HashTable(8)
print(ht)
print("-"*100)
print("Додаємо декілька елементів")
ht.add(111, "Sydorenko")
ht.add(222, "Petrenko")
ht.add(333, "Homenko")
ht.add(444, "Ivanov")
print(ht)
print("-"*100)
print("Видаляємо елемент")
ht.remove(222, "Petrenko")
print(ht)
print("-"*100)
print("Шукаємо елементи")
print(ht.search(111))
print(ht.search(777))
