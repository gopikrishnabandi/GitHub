# Primitive types can be numbers, booleans and strings
students = 100#int
wage = 160.5#float
permanent_hire = True #boolean, python is case sensitive so we should give like False or True
name = 'gkb'#string
gopi = 100
krishna = 1000000
bandi = 1000000
gk = 1000000
gkb = bandi
print(students)
print(id(students))
print(id(gopi))
print(id(krishna))
print(id(bandi))
print(id(gk))
print(id(gkb))
a=257
b=257
print(id(a))
print(id(b))
#cannot be always same, check http://foobarnbaz.com/2012/07/08/understanding-python-variables/
#we can use triple quotes for multi line messages, not documentation comments as learned earlier
message = """hi john
how are you ?
"""
print(message)
#\ escapes the next charcater \' \" \\ \n
course = "Python \'Pro\ngram\\ming\""
print(course)
first = 'gopi'
last = 'bandi'
print(first+' '+last)
#formattedstring
full = f'{first}{last}'#f stands for format
print(full)#gopibandi
full = f'{first} {last}' #gopi Bandi bcoz of space
print(full)
full = f"{len(first)+2}{first[1]}"#we can put any expression in b/w paranthesis
print(full)
print(f'{1+1}{2+2}')#using format directly, prints 24
text = 'this is nIce'
print(text[1:-1])#starts at position 1 till -1 which is last charcater
print(text.upper()) #THIS IS NICE
print(text.lower())#this is nice
print(text.capitalize())#This is nIce(only first letter)
print(text.title())#This Is NIce(every fisrt letter after space)
eg = ' gopi krishna bandi '
print(eg.lstrip())
print(eg.rstrip())
print(eg.strip())
print(eg.find('a'))#indexing starts from 0, hence 12
print(eg.find('ban'))#14 is the starting position of b in ban
print(eg.find('Ban'))#returns -1 as it cannot find Ban 
print(eg.replace('a','A'))# gopi krishnA bAndi
print('go' in eg) #True, find gives position , in gives True/False
if 'Kri' in eg:#note here we gave capital K
    print('found Kri')
else:
    print('not found Kri')
print('chowdary' not in eg) #True
x = 1 + 2j #imaginary number can directly be declared in Python
print(x)
#augmented assignment
x = 10
#x=x+3 standard
x += 3
print(x)
print(round(2.9))#3
print(abs(-2.6))#2.6
#for more math functions import math , adding line above, but can add here as well
import math
print(math.ceil(2.2))#3
print(math.floor(2.2))#2
print(math.floor(-2.2))#-3 as it is negative
print(math.factorial(4))#24
x = input("Enter ")
print('Entered value is:'+x)
print(type(x))
y = int(x)+1
print(y)
#"",0 and None are boolean False, rest all are True
print(bool(y))
print(bool('gopi'))
print(bool('False'))#this is also true as it has some char, only empty string or none is false for strings
print(hex(10))
print(oct(10))
print(bin(10))
