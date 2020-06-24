a='gopi'
b='priya'
print(a+b)#no space
print(a,b)#space exists
#in that we use in for loop, can be used a logical operator in an if statements, it reurns True/Fa;se
'g' in a#evaluates to true , but is not printed
print('g' in a)#prints True
if 'p' in b:#in is similar to == in this case
    print('found')
if 'pr'in b:
    print('substring found')
#string comparision
if a=='Gopi':
    print('Strings matched')
elif a<'Gopi':
    print('input is less')
elif a>'Gopi':
    print('Input is greater,lower case is greater in string comparision than upper')
#strings are objects, which have a strong library called the string library
c='Gopi Krishna'
print(c.upper())#GOPI KRISHNA, upper and lower are methods, using dot operator, doesnt change the original string
print(c.lower())#gopi krishna
print('Hi There'.lower())#hi there
print(type(c))#class str
print(dir(c))#methods in class str
print('GOPI krishna'.capitalize())#only first letter is capetalized, rest all in smalls
#in function returns a true/False, Find returns the first position it found it,if not found returns -1
fruit='banana'
print(fruit.find('na'))#there are two na's but it will give the first position it found that sequence
#we can use regular expressions for multiple repitition finding
print(fruit.find('z'))#prints -1
newfruit=fruit.replace('n','z')#doesnt effect/tamper the original fruit
print(newfruit)#prints bazaza, as a recap remember no space can be given in variable names, hence newfruit
anotherfruit=fruit.replace('na','ka')
print(anotherfruit)#bakaka
#stripping whitespaces
teststring='   Hello  Bob  '
print(teststring.lstrip())#removes front space before Hello
print(teststring.rstrip())#removes spaces at end after Bob
print(teststring.strip())#removes spaces at start and end,not in middle though
#Prefixes methods
test='Hello Please'
print(test.startswith('Hello'))#returns True
print(test.startswith('H'))#returns True
print(test.startswith('P'))#returns False
#parsing and Extracting
message='university of michigan abc@michigan.net.edu Aug1 2019 12:47 PM'
startpos=message.find('@')
endingpos=message.find(' ',startpos)#searches for space starting fro the second parameter given in the function
print(message[startpos+1:endingpos])#prints michigan.net.edu
#in python 3 all strings are unicode, earlier we have to convert explicity using 'u' eg x=h'blah blah blah'
