# 1.	Додайте до класу Tree метод, який реалізує додавання
# до бінарного дерева пошуку нових елементів зі списку.
# Метод має містити функціонал, який перевіряє дані із списку
# на відповідність до правил формування бінарного дерева пошуку.
# 2.	Додайте до класу Tree методи пошуку мінімального і максимального
# значення елементів в бінарному дереві пошуку.
# 3.	Розширте функціонал класу Tree, додавши в нього
# метод видалення елементів в бінарному дереві пошуку.

class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

# Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

# findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return print(str(find_val) + " Not Found")
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return print(str(find_val) + " Not Found")
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

# Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

# function to delete the given deepest node (d_node) in binary tree
    def deleteDeepest(self, d_node):
        q = []
        q.append(self)
        while (len(q)):
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

# function to delete element in binary tree
    def deletion(self, key):
        if self == None:
            return None
        if self.left == None and self.right == None:
            if self.key == key:
                return None
            else:
                return self
        key_node = None
        q = []
        q.append(self)
        temp = None
        while (len(q)):
            temp = q.pop(0)
            if temp.id_node == key:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x = temp.id_node
            tree.deleteDeepest(temp)
            key_node.id_node = x
        return self

    def find_min(self):
        current = self
        while current.left != None:
            current = current.left
        return print(f"\n min element {current}")

    def find_max(self):
        current = self
        while current.right != None:
            current = current.right
        return print(f"\n max element {current}")

# Insert list method to create nodes
    def insert_list(self, list_nodes):
        for i in range(len(list_nodes)):
            id_node = list_nodes[i]
            if self.id_node:
                if id_node < self.id_node:
                    if self.left is None:
                        self.left = Tree(id_node)
                    else:
                        self.left.insert(id_node)
                elif id_node > self.id_node:
                    if self.right is None:
                        self.right = Tree(id_node)
                    else:
                        self.right.insert(id_node)
            else:
                self.id_node = id_node


tree = Tree(8)
tree.left = Tree(3)
tree.left.left = Tree(1)
tree.left.right = Tree(6)
tree.right = Tree(10)
tree.right.right = Tree(14)
print(f"\nThe tree before the insertion some elements: \n")
tree.print_tree()

tree.insert(7)
tree.insert(12)
tree.insert(8)
tree.insert(22)
tree.insert(14)
print(f"\nThe tree after the insertion some elements: \n")
tree.print_tree()

print(f"\nFind element 15 \n")
tree.findval(15)

print(f"\nFind element 14 \n")
tree.findval(14)

print(f"\nDelete element 22 \n")
tree.deletion(22)
print(f"\nThe tree after the deletion 22:\n")
tree.print_tree()

tree.find_min()
tree.find_max()

list_n = [10, 2, 39]
tree.insert_list(list_n)
print(f"\nThe tree after the insertion list {list_n}: \n")
tree.print_tree()
