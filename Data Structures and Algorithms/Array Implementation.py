#import array as arr
from array import *
#printing an array
vals=array('i',[5,9,-8,4,2])
print(vals)

print(vals.buffer_info())
#reversing an array
vals.reverse()
print(vals)

#printing array elements one by one using for loop 
for i in range(len(vals)):
    print(vals[i])

#printing array elements one by one  
for j in vals:
    print(j)

#creating a new array from a given array
newArr=array(vals.typecode,(a*a for a in vals))
for k in newArr:
    print(k)

#printing using while loop
i=0
while i<len(newArr):
    print(newArr[i])
    i+=1

###################################
#inserting in an array from user input

arraynew=array('i',[])
n=int(input('Enter the size of array:'))
print(n)

for k in range(n):
    x=int(input('Enter the next element of array:'))
    arraynew.append(x)

print(arraynew)


#searching for an element in an array
value=int(input('Enter the Value to be searched:'))
for i in range(len(arraynew)):
    if arraynew[i]==value:
        print(value,'Found at index',i)
        break
else:
    print(value,'Not Found in Array')

#alternate way
counter=0
for e in arraynew:
    if value==e:
        print(value,'Found at index',counter)
        break
    counter+=1
else:
    print(value,'Not Found in Array')

#using functions with array
#Prints index of the element value in the array
print(arraynew.index(value))
#removes last element
arraynew.pop()
print(arraynew)
rm=int(input('Enter Value in above array to be removed:'))
#removes the first occurance of the element
arraynew.remove(rm)
print(arraynew)
#inserts an element ath the given index
arraynew.insert(0,10)
print(arraynew)