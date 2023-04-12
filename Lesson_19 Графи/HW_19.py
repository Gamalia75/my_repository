# 1. Використовуючи дані із файлу cities.csv, створіть список типу:
# cities = [['city1',city2', km]...]. З отриманого списку створіть граф. Візуалізуйте отриманий граф.
# 2. Напишіть функцію знаходження найкоротшого маршруту між двома населеними пунктами,
# яка приймає у якості аргументів об'єкт графу і пару населених пунктів, а повертає маршрут і його протяжність.
import networkx as nx
import matplotlib.pyplot as plt


def get_list(fn):
    with open(fn, "r") as f:
        row_s = []
        row_str = f.read()
        row_s = row_str.split("\n")
        row_list = []
        for i in row_s:
            if i != '':
                temp_list = []
                el = i.split(";")
                temp_list.append(el[0])
                temp_list.append(el[1])
                temp_list.append(int(el[2]))
                row_list.append(temp_list)
    return row_list

my_list = get_list("cities.csv")

#З отриманого списку створіть граф
g = nx.Graph()
for edge in my_list:
    g.add_edge(edge[0], edge[1], weight = edge[2])

#Візуалізуйте отриманий граф
nx.draw_networkx(g)
plt.title("Ukrainian sities")
plt.show()

#знаходження найкоротшого маршруту між двома населеними пунктами
print(nx.shortest_path(g, 'Sumy', 'Odesa', weight='weight'))
print(nx.shortest_path_length(g, 'Sumy', 'Odesa', weight='weight'))
