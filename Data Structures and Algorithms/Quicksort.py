def quicksort(arr):
    less = []
    pivots = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivots.append(i)
        less = quicksort(less)
        more = quicksort(more)
        return less + pivots + more


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
print(test)

