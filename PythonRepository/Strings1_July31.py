#strings have indexable data with in it, index starts with 0, we use index operator []
fruit='banana'
letter=fruit[0]+fruit[1]#concatenation also can be done
print(letter)
x=3
letter1=fruit[x+2]#we can use expression
print(letter1)
#beyond range is traceback eg: letter[7]
print(len(fruit))#value is 6
index=0
while index<len(fruit):
    print(index,fruit[index])
    index=index+1
#one more way, more elegant and dedfinite
#iteration table taken care by python in below for loop
for x in fruit:
    print(x)
#trying with list to check
exoticfruits=['kiwi','dragon fruit','avacado']
for x in exoticfruits:#now x will iterate through the list elements
    print(x)
#find number of a's
count=0
for y in fruit:
    if y=='a':
        count=count+1
print('count of a\'s is',count)#\is an escape character
#slicing a string
print(fruit[1:4])#1 till 4 , not including 4
print(fruit[1:20])#interestingly not a traceback, how python is built
print(fruit[2:3])#prints index 2 letter which n
print(fruit[:2])#prints from 0 till 2 not inlucing 2, which will be ba
print(fruit[2:])#prints from 2 till end, which is nana
print(fruit[:])#prints everything from begining till end , banana
print(fruit[::])#same as above line
