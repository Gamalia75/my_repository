# 2. Взявши за основу код домашнього завдання лекції 14,
# розробіть набір тестів з використання бібліотеки pytest для методів
# додавання нових елементів, пошуку мінімального і максимального значень
# та видалення елементів бінарного дерева.

from tree import Tree


def test_find_min():
    tree1 = Tree(8)
    tree1.left = Tree(3)
    tree1.left.left = Tree(1)
    assert tree1.min_value() == "1"


def test_find_max():
    tree2 = Tree(8)
    list_n = [10, 2, 39]
    tree2.list_insert(list_n)
    assert tree2.max_value() == "39"


def test_insert():
    tree3 = Tree(8)
    list_n = [10, 2]
    tree3.list_insert(list_n)
    tree4 = Tree(2)
    assert tree3.min_value() == tree4.min_value()


def test_delete():
    tree5 = Tree(8)
    list_n = [10, 2, 39]
    tree5.list_insert(list_n)
    tree6 = Tree(8)
    list_n = [10, 2, 39]
    tree6.list_insert(list_n)
    tree6.delete(39)
    assert tree5.max_value() != tree6.max_value()
