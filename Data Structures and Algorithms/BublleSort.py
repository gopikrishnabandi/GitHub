"""Implementing Bubble sort on an array"""


def bubblesort(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


test1 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
bubblesort(test1)
print(test1)
