#Lists
list1=['a','b','c','d']
list2=[1,2,3,4]
list3=[[1,2,3],['a','b','c']]#2 dimensional matrix
zeros=[0]*5 #for repeating items in a list
print(zeros)
combined=zeros+list3#+ for concatenating lists
print(combined)
numbers=list(range(20))#list function takes an iterator
print(numbers)
chars=list("Hello world")#string is also an iterable
print(chars)
print(len(chars))#length of a list
#accessing items in a list is similar to strings
print(list2[0])#1
print(list3[-1])#['a','b','c']
#modifying list
list4=['one',2,3,4,5,6,7,8,9,10]
print('Actual list is',list4)
list4[0]=1
print('Modified list after modifying is',list4)
#slicing a list
print('list slice is ',list4[0:2])#[1,2]
#stepping and slicing
print('Every 2nd element of list is',list4[::2])#starts at 0, next index 2 and so on
#reversing a list
print('reversing list',list4[::-1])
#unpacking and packing Lists
first,second=[1,2]#list unpacking to two variables
print(first,second)
#number of variables on lhs should be same as items in list, else error
#in case of a list with many values , we can do as below
first1,second1,*other1=[1,2,3,4,5,6,7,8,9]
print(other1)#[3,4,5,6,7,8,9]#we are packing left overs into a list called other1
first2,*other2,last2=[2,4,6,8,10,12,14]
print(first2)#2
print(last2)#14
print(other2)#[4,6,8,10,12]
print(other2[0:2])#we can perform list operations
#looping over Lists
for i in list4:
    print(i)
#getting index using enumerate function
for number in enumerate(list4):#enumerate function retrurns an enumerate object which iterates over list4
#in each iteration eneumerate will give a tuple, first item is index, second is the item
    print(number)
for index,number in enumerate(list4):#unpacking tuple just like a list into two iteration variables
    print(index,number)
#one more way to generate the same as above-using index function
for i in list4:
    print(list4.index(i),i)
#adding/removing items
#append,insert,pop,remove,del clear
eg=['a','b','c','d','e','f','f','f']
eg.append('g')#adds element g at the end of the list
eg.insert(1,'A')#Inserts 'A' at index 1, i.e., after 'a'
eg.pop()#removes last element 'g'
eg.pop(1)#removes 'A' which is at index 1,can remove only one elemennt at a specified index
#to remove an element
eg.remove('f')#removes first ocuurence of 'f' , we can iterate in a for loop to remove multiple 'f's
#to remove a part of
del eg[5:6]#unlike pop del can remove a substring
print(eg)#['a','b','c','d','e','f']
eg.clear()#to clear a list
print(eg)#[] empty list exists,only elements cleared

#Finding objects in a list
eg1=['a','b','c','d','d','d','e','a']
#to know index of a value in list
print(eg1.index('d'))#first occurence is at index 3
#to know count
print(eg1.count('a'))#2 , as 'a' is there twice in the list
#print(eg1.index('g')) will return an error as it doesnt exist, unlike find function which returns -1 this throws a value error
#to mitigate above use an if block, only if true it will execute
if 'g' in eg1:
    print(eg1.index('g'))

#sorting lists
eg2=[2,31,22,4,56,1,82,11]
eg2.sort()#to sort in ascending
print(eg2)
eg3=[2,31,22,4,56,1,82,11]
eg3.sort(reverse=True)#to sort in descending
print(eg3)
#above two examples modify our original list, to not modify initial list and sort , see below
#we use sorted function
eg4=[2,31,22,4,56,1,82,11]
print(sorted(eg4))#sorted in ascending and stored in temp list in memory
print(sorted(eg4,reverse=True))#sorted in descending and stored in temp list in memory
print(eg4)#original list intact
#sorting lists with complex objects eg:tuples
items=[('product1',10),('product2',8),('product3',20)]
#if we use sort method, python doesnt know what to sort on, it needs a key
def items_sort(item):
    return item[1]#takes an item and returns its price
items.sort(key=items_sort)#we can use only keyword argument here as a rule(try without key, as well as key1), as well as please note we are sending each item in items to the function to know what to sort based on
print(items)

#above way is little ugly, lets see an elegant way to do it using lambda
#we will be using lambda expression also called a lambda function
#lamda is an anonymous function used in Python
#syntax for this is lambda parameters:expression

#we can rewrite above code as
items1=[('product1',10),('product2',8),('product3',20)]
items1.sort(key=lambda item:item[1])
print(items1)

#example of lambda
a=lambda x,y:x**y
print(a(2,3))#8

#More on lambda

items_new=[('product1',10),('product2',8),('product3',20)]
#suppose we want to print a  list with just the prices
prices=[]
for item in items_new:
    prices.append(item[1])
print(prices)

#More elegant way is to use map function to acieve above
#map takes a function as first param, and one or more iterables as second param
items_new1=[('product1',100),('product2',80),('product3',200)]
#print(map(lambda item:item[1],items_new1))#returns a map object,to print values we can use below code
#mp=map(lambda item:item[1],items_new1)
#for i in mp:
#    print(i)

#even better than above commented code is
prices1=list(map(lambda item:item[1],items_new1))
print(prices1)
