#Refer to Youtube Videos by Amulya Academy
def insertion_sort(test):
    for i in range(len(test) - 1):
        min_val = min(test[i:])
        min_index = test.index(min_val, i)
        if test[i] != test[min_index]:
            test[i], test[min_index] = test[min_index], test[i]
        print("step ", i, test)
    return test


list1 = [56, 0, 2, 3, 0, 12]
print("unsorted list", list1)
insertion_sort(list1)
print("sorted list", list1)
