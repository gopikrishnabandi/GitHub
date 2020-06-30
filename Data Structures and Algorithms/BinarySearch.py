"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    array = input_array
    i = 0
    j = len(array) - 1
    while i <= j:
        if array[(i + j) // 2] == value:
            return (i + j) // 2
        elif array[(i + j) // 2] > value:
            j = ((i + j) // 2) - 1
        elif array[(i + j) // 2] < value:
            i = ((i + j) // 2) + 1
    else:
        return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_list2 = [1, 3, 9, 11, 15, 19, 29, 31]
test_val1 = 25
test_val2 = 15
test_val3 = 11
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list2, test_val3))
