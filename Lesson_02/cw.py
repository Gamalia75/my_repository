# ######
# DIGITS
# ######

a = 10
b = 1.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(-a)
print("="*50)

# #######
# STRINGS
# #######

string = "Hello, World!"
print(string[0])
print(string.upper())
print(string.lower())
print(string + "!!")
print(string.replace(" ", ""))
print(string[0:3])      #Hel
print(string[0:5:2])    #Hlo
print(string[-1])       #!
print(string[::-1])     #!dlroW ,olleH

print("="*50)
# ###########
# COLLECTIONS
# ###########

#List - списки
my_list = [1, "two", 3.0]
print(my_list)
print(my_list[1])
my_list.remove("two")
print(my_list)        #[1, 3.0]
print(my_list[::-1])  #[3.0, 1]
my_list.append("one")
my_list.insert(1, "Three")
print(my_list)        #[1, 'Three', 3.0, 'one']

my_second_list = [23, "John", "male"]
my_list.extend(my_second_list)
print(my_list)        #[1, 'Three', 3.0, 'one', 23, 'John', 'male']
print(my_list.count('Three')) #1
print(my_list)
my_list.reverse() #['male', 'John', 23, 'one', 3.0, 'Three', 1]
print(my_list)
print(my_second_list)

print("="*50)
#Кортежі - Tuple
my_str = "Hello, world!"
my_tuple_1 = tuple(my_str) #('H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!')
print(my_tuple_1)
my_tuple_3 = tuple(my_str.split(" ")) #('Hello,', 'world!')
print(my_tuple_3)

my_tuple_2 = (23, "Natalia", "female", True)
#my_tuple_2.append("666") Буде помилка - кортежі змінювати не можна! А списки можна!


print("="*50)
#Словники - Dictioanary
dict_1 = {}
print(dict_1)
dict_2 = {"dict": 1, "dictionary": 2}    #{'dict': 1, 'dictionary': 2}
print(dict_2)
dict_3 = dict(short="dict", long="dictionary")  #{'short': 'dict', 'long': 'dictionary'}
print(dict_3)
dict_4 = dict.fromkeys(['one', 'two', 'three'], 60)  #{'one': 60, 'two': 60, 'three': 60}
print(dict_4)

my_dict = {1: "one1", 2: "two2"}  # one1
print(my_dict[1])

print(dict_2.get('dict'))  # 1
print(dict_2.items())      #dict_items([('dict', 1), ('dictionary', 2)])
print(dict_2.keys())       #dict_keys(['dict', 'dictionary'])
print(dict_2.pop('dict'))  # 1
print(dict_2)              #{'dictionary': 2}

print("="*50)
#set and frozenset
my_set_1 = set()
print(my_set_1)
my_set_2 = set("Sets are used to store multiple items in a single variable")
print(my_set_2)
my_set_3 = set("The frozen function returns an immutable frozemset")
print(my_set_3)

my_set_4 = set.union(my_set_2, my_set_3)
print(my_set_4)

my_set_5 = set.difference(my_set_2, my_set_3)
print(my_set_5)

my_set_5.add("W")
print(my_set_5)

my_set_5.discard("W")
print(my_set_5)

my_frozenset = frozenset("The frozen function returns an immutable frozemset")
print(my_frozenset)
print(my_set_3)


print("="*50)
# #########
# FIFO LIFO
# #########

queue = list()
queue.append(1)
queue.append(2)
queue.append(3)

'''
print(queue.pop(0))  # 1
print(queue.pop(0))  # 2
print(queue.pop(0))  # 3
'''

print(queue.pop())  # 3
print(queue.pop())  # 2
print(queue.pop())  # 1