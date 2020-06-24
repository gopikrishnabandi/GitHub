# numpy
# pyNumbers
# pipenv install numpy
# cd C:\Users\Gopi\.virtualenvs\PyNumbers-ftmLIQUC\Scripts, activate after that
# has multidiemsnional arrays that are better than regaular arrays
import numpy as np
array = np.array([1, 2, 3])
print(array)
print(type(array))
array = np.array([[1, 2, 3], [4, 5, 6]])  # two dimensional
print(array.shape)
# we have helper methods to create different arrays
# data type is int , else by default float
zero_array = np.zeros((3, 4), dtype=int)
print(zero_array)
# np.ones(3,4) for ones
# np.full((3,4),5) #for a specific number
# np.random.random((3,4)) #without numpy this will be a longer code
# accessing
print(zero_array[0][0])
array1 = np.random.random((3, 4))
print(array1)
array2 = np.ones((2, 2), dtype=int)
array3 = np.array([[3, 0.1, 0.2, 4], [1, 0.1, 2, 4]])
print(array3 > 0.2)  # we get a boolean array if elements greater than 0.2
# boolean indexing, this creates new array wih values that are only graeetr than 0.3
print(array3[np.array(array3 > 0.3)])
print(np.sum(array1))  # compuattions
# we have floor, ceil, round etc to get arrays
print(np.floor(array1))  # retuns a new array with floor of each item
# we can also perform arithemtic operations, sum , product, div etc..
first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first+second)
third = first+2
print(third)  # added to each elemnt

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch*2.54
print(dimensions_cm)

# regular python without numpy
dimensions_inch = [1, 2, 3]
# dimension_cm=[item_expression for item in list] syntax of list comprehension, use this to easily write a list comprehension
dimension_cm = [x*2.54 for x in dimensions_inch]
