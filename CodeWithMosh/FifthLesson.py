# DataStructures
# Lists
#all imports are added in the beginning , say we are coding and we need a certain package, we import that , so as we write programs these are added, we dont know initially what we need
from pprint import pprint#used later in code for printing
from sys import getsizeof
from array import array
from collections import deque
letters = ['a', 'b', 'c']
# list can also contain list
matrix = [['a', 'b'], [1, 2, 3, 4]]
combined = letters+matrix
print(combined)
zeros = [0]*5
print(zeros)
print(len(combined))  # 3 elements n first and 2 in the second
# list keyword can be used to create a list with an iterable
# we have already learnt that range is an iterable as well as a string is an iterable, iterable is something we can iterate/loop om
chars = list('lets check this')
print(chars)
numbers = list(range(20))
print(numbers)


# Accessing Items
print(numbers[0])
print(numbers[1:3])
print(numbers[::2])  # the last parameter is the step
print(numbers[::-1])

test = ['a', 'b', 'c', 'd']
# replacing an item in list
test[0] = 'A'
print(test)

# List Unpacking
test1 = ['a', 'b', 'c', 'd']
var1 = test1[0]
var2 = test1[1]
# Above is not a clean way
# Number of variables on left should be equal to list length, else error
var1, var2, var3, var4 = test1
print(var4)
# Unpacking and packing(into others), if you observe same used in functions
var5, *others = test1
print(var5)
print(others)
var6, *others, last = test1
print(var6, last)
print(others)

# Loop over lists
letters_eg = ['a', 'b', 'c']
for i in letters_eg:
    print(i)

i = 0
while i < len(letters_eg):
    print(letters_eg[i])
    i += 1

# if we need index as well, use enumerate funvtion, it returns an enumerate object which is an iterable
# in each iteration returns a tuple
for index, letter in enumerate(letters_eg):
    print(index, letter)

# Adding removing items
# adding at the end of the list
letters_eg.append('d')
letters_eg.append('e')
# insert to add at a specific position
letters_eg.insert(0, '-')
print(letters_eg)
letters_eg.pop(4)  # to remove at specific position
print(letters_eg)
letters_eg.append('b')
letters_eg.remove('b')  # removes first ocuurence of 'b'
print(letters_eg)
# del to remove a portion of a list
del letters_eg[0:2]
print(letters_eg)
letters_eg.clear()
print(letters_eg)

# Finding items in a list
numbers_eg = [1, 21, 3, 4, 5, 6, 1, 21]
print(numbers_eg.index(21))
print(numbers_eg.count(21))
if 7 in numbers_eg:
    print(numbers_eg.index(7))

# sorting lists
print(sorted(numbers_eg))  # This will not change the original list
# same as above, no impact to original list, creates new
print(sorted(numbers_eg, reverse=True))
print(numbers_eg)
numbers_eg.sort()  # This will change the original list
print(numbers_eg)
numbers_eg.sort(reverse=True)
print(numbers_eg)


# Sorting lists with complex objects
# Sorting tuples
products = [('product1', 100), ('Product2', 20), ('Product3', 10)]


def items_sort(item):
    return item[1]


# Please note we are not passing items_sort() rather items_sort
products.sort(key=items_sort)
print(products)


# Lambda functions
# Above implementation is little ugly , better way is to use a lambda
#lambda parameters:expression
items = [('product1', 100), ('Product2', 20), ('Product3', 10)]
items.sort(key=lambda item: item[1])
print(items)

# Some lambda examples


def y(x): return x**x


print(y(5))


def z(a, b): return a % b


print(z(3, 2))

# Map Function
# say we want a new list with just prices , how do we achieve this
# Crude way
prices1 = []
for item in items:  # items is already defined above for some other example
    prices1.append(item[1])
print(prices1)

items_1 = [('product1', 100), ('Product2', 20), ('Product3', 10)]
mp = map(lambda item: item[1], items_1)
# if we print above we get a map object
print(mp)
# Crude way
for item in mp:
    print(item)

# Better way is to give map object to a list , as map is an iterable
a = list(map(lambda item: item[1], items_1))
print(a)


# Filter function
# say we want to get a list with prices gretaer than or equal to 20
b = list(filter(lambda item: item[1] >= 20, items_1))
print(b)
# if we want ust prices again we have to use a lambda with map
print(list(map(lambda item: item[1], b)))


# List Comprehensions
# To map and filter lists better way is to use list comprehensions , unlike above it is more elegant and clean code wise

student_grades = [('Golu', 99), ('Priya', 98), ('Molu', 100)]
# we will first demonstrate using map and filter how we do, along with list comprehension on the side as comparision
grades_map = list(map(lambda student: student[1], student_grades))
print(grades_map)
grades_map_list_comp = [student[1] for student in student_grades]
print(grades_map_list_comp)

grades_filter = list(filter(lambda student: student[1] >= 98, student_grades))
print(grades_filter)
grades_filter_list_comp = [
    student for student in student_grades if student[1] >= 98]
print(grades_filter_list_comp)
grades_filter_list_comp2 = [student[1]
                            for student in student_grades if student[1] >= 98]
print(grades_filter_list_comp)


# Zip Function
# say we want to combine two lists into a list of tuples with first element with first and so on
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list(zip(list1, list2)))
# we pass iterables as arguments to zip, abc is a string which is an itearble
print(list(zip("abc", list1, list2)))
# If we dont pass enough elements in any list to combine, it will be skipped
print(list(zip("ab", list1, list2)))

# Stacks-Data Strcuture
# Last in Fisrt out (LIFO)
# We will use list object as a stack
choclate_jar = [1, 2, 3]
# to add items to top of  a stack
choclate_jar.append(4)
print(choclate_jar)
# To remove item from top of a stack
last = choclate_jar.pop()
print(last)
print(choclate_jar)
# to know element top of a stack
print(choclate_jar[-1])
# to check if list is empty
if not choclate_jar:
    print('Empty List')


# Queues
# FIFO behavior - Fisrt in Fist out
# List is not a feasible solution to implement queue, becuaes of FIFO, if one element is removed, many elements need to move places
# Thats why we use deque object, which we need to import first
# from collections import deque, deque is a class in collections module
queue = deque([])  # creating an emepty queue using deque object
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # method specific to deque
print(queue)
if not queue:
    print('Queue is empty')


# Tuples
# Tuple is a read only list, they are immutable
# in real world they are used in cases where accidental insertion , dletion eeds to be prevented
point = ()  # empty tuple
temp = 1,
print(type(temp))
point1 = (1, 2)+(3, 4)
print(point1)
print(point1*2)  # new tuple , original tuple is immutable
print(point1)
print(point1[1:2])
point2 = tuple([1, 2, 3, 4])
print(point2)
point2 = tuple("Hello")  # This will work as we are reassigning the tuple
print(point2)
x, y, *others_tuple = point2
print(others_tuple)
if 'l' in others_tuple:
    print('Exists')

# Swapping Variables
x = 10
y = 11
temp = y
y = x
x = temp
print(x, y)

# in python more efficiently , we can write this avoiding third variable
x, y = y, x  # This is a tuple declaration on the right and tuple unpcaking on the left
# using the same concept allows to declare multiple variables in single line in python
a, b = 1, 2


# Arrays
# use arrays if lists are giving perf issue
# typecode is to be given as  first parameter, for each data type there is a specific letter assigned, check documenntation
# can only be an integer list , cannot insert or assign other types
numbers = array("i", [11, 21, 33, 4])
print(numbers)
numbers.append(51)
numbers.pop(4)  # removes element at index 4
numbers.insert(1, 10)  # inserst at index 1, rememeber index starts at 0
print(numbers)
numbers.remove(21)
del numbers[2:4]
print(numbers)


# Sets
# a unordered collection of items that cannot have duplicates, does not support indexing, cannot be accessed like lists
# used in mathematical calculations
# represented using curly braces

a = [1, 2, 3, 4, 4, 5, 1]
b = set(a)
print(b)
# c = {1, 2, 3} + {4, 5}
# print(c) , This will result in an error
b.add(7)
b.remove(5)
print(b, len(b))
c = {4, 5, 7}
# where sets shine is in mathematical operations
print(b | c)  # Union
print(b & c)  # Intersection
print(b - c)  # difference
print(b ^ c)  # Symmetric difference i.e., either in first or second but not in both, i.e, excluding intersection of two sets

if 7 in c:
    print("exists")
# indexing is not supported will throw error, as sets are unordered , so c[0] will give an error


# Dictionaries
# collection of key value pairs, eg:Contact name and phone no
# keys should always be of immutable types like string or number, value can be of any type
# can be indexed with key, not with an index position

# declaration
dict1 = {'a': 1, 'b': 2}
# better way is to use dict keyword, with keyword arguments
dict2 = dict(a=1, b=2)
print(dict2)
# Adding to a dictionary
dict2['c'] = 3
# dict2.append('e', 4)
# print(dict2) will give error as append is not a supported method

# with get we can handle usin default value if key is not found
print(dict2.get('d', "Key Does Not exist"))

if 'c' in dict2:
    print('Key Exists')

del dict2['c']  # to delete a key value pair
print(dict2)

# to loop
for key in dict2:
    print(key, dict2[key])

for x in dict2.items():
    print(x)

for key, value in dict2.items():  # same as abaove but unpacking, so elegant
    # https://www.geeksforgeeks.org/python-dictionary-items-method/
    #    .items returns a lists
    print(key, value)


# Dictionary Comprehensions
values = {x: x * 2 for x in range(5)}
print(values)
# we can create comprehensions for Lists,sets and dictionaries
# with dictionaries we provide both key and value in the expression
# whereas in lists and sets we just give the expression

# what about tuple comprehensions,that is our next topic generators

# generators
# when the size of the comprehension expression is huge, we use generaors
# as lists store everything in memory,geneartors spit out new values in each iteration
values_generator = (x * 2 for x in range(10))
print(values_generator)  # prints geneartor object
values_list = [x * 2 for x in range(10)]
print(values_list)  # prints list
# from sys import getsizeof-to know size in bytes , how much memory is occupied
print(getsizeof(values_list))
print(getsizeof(values_generator))
# since genaerots doent store values in memory, they spit out new values in each iteration , hence length is not a valid function, will result in an error


# unpacking operator
# very useful with data structures
numbers = [1, 2, 3]
print(*numbers)  # to print not as a list , but individually

# useful when creating lists
# * can be used to unpack any iterable
values_eg = list(range(5))  # regular way
values_eg1 = [*range(5)]  # *unpacks
print(values_eg1)
values_eg2 = [*range(5), * "Hello"]
print(values_eg2)

# * can also be used to combine lists
list3 = [1, 2, 3]
list4 = [4, 5, 6]
list5 = [*list3, *list4, * "Hello"]
print(list5)

# ** will be used for dictionaries, refer below
dict3 = {'x': 1, 'y': 10}
dict4 = {'x': 10, 'z': 2}
combined = {**dict3, **dict4, 'a': 1}
print(combined)
# {'x': 10, 'y': 10, 'z': 2, 'a': 1} is output , x will take last value when getting combined


# Exercise
sentence = "This is a common interview question"
# write most common letter
# write tomorrow without checking
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)
# import pretty printing module
# from pprint import pprint
pprint(char_frequency, width=1)
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)  # this returns a list
print(char_frequency_sorted)
print(char_frequency_sorted[0])


def addition(x, y):
    print(x+y)
