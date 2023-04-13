
# ########################
# Algorithmic Complexity
# ########################

# ########################
# Constant - O(1)
# ########################

# Example 1
nums = list((1, 2, 3, 4, 5))
firstNumber = nums[0]


# Example 2
def get_size(nums: list((1, 2, 3, 4, 5))):
    size = len(nums)


# Example 3
def sum_pair(a, b):
    return a + b


# ########################
# Linear - O(n)
# ########################

# Recursive function
def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


#  Linear function
def pair_sum_sequence(n):
    summa = 0
    for i in n:
        summa += pair_sum(i, i + 1)
    return summa


def pair_sum(a, b):
    return a + b


# ########################
# Logarithmic - O(log n)
# ########################

# Example - Binary search function (див. нище)

# ########################
# Linearithmic - O(n * log n)
# ########################

# Example - Merge sort
def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


def merge(array, left_index, right_index, middle):

    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
merge_sort(array, 0, len(array) -1)
print(array)

# ########################
# Quadratic - O(n2), O(n**2)
# ########################

# Feature - nested cycles
def print_pairs(nums):
    for i in nums:
        for j in nums:
            print(i, j)

print_pairs(array)

# ########################
# Recursion
# ########################

# Recursive function for file list making
import os

path = 'C:\\Student'  # change folder

def go_file(path, level=1):
    print("Level=", level, "Content:", os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print("Go down, path + '\\'" + i)
            go_file(path + '\\' + i, level + 1)
            print("Return in", path)

go_file(path)


# ########################
# Search Algorithms
# ########################

# Membership Operators
quest1 = 'apple' in ['orange', 'apple', 'grape']
print(quest1)

# Linear Search
def linear_search(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1

print(linear_search([1, 2, 3, 4, 5, 2, 1], 2))

# Binary Search
def binary_search(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print(binary_search([10,20,30,40,50], 20))

# Jump Search
import math

def jump_search (lys, val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val and lys[right] >= val:
            break
        left += jump;
    if left >= length or lys[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return -1

print(jump_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))

# Fibonacci Search

def fibonacci_search(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1;
    return -1


print(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 6))

# Exponential Search

def exponential_search(lys, val):
    if lys[0] == val:
        return 0
    index = 1
    while index < len(lys) and lys[index] <= val:
        index = index * 2
    return binary_search(lys[:min(index, len(lys))], val)


print(exponential_search([1, 2, 3, 4, 5, 6, 7, 8], 3))

# Interpolation Search

def interpolation_search(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1

print(interpolation_search([1, 2, 3, 4, 5, 6, 7, 8], 6))
Lesson6.py
Lesson6.py. На экране.