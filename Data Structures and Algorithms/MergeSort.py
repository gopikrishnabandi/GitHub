"""Implementing a merge sort"""


def mergesort(list1):
    # to divide the list, and if condition below is for terminating the loop
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        # recursion to further break the lists to granular level
        mergesort(left_list)
        mergesort(right_list)
        # left list index
        i = 0
        # right list index
        j = 0
        # original list index, we reinsert elements back to the list after sorting
        k = 0
        # above can also be written as i=j=0
        # Merging lists
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
                k += 1
            else:
                list1[k] = right_list[j]
                j += 1
                k += 1
        # Adding any missing elements that were left out in comparison on left
        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1
        # Adding any missing elements that were left out in comparison on right
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1


n = int(input('Enter Size of the list:'))
list_example = [int(input('Enter List Value:')) for i in range(n)]
print('list before sorting', list_example)
mergesort(list_example)
print(list_example)
