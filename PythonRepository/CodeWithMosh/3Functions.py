#creating a function without parameters
def greet():
    print('Hello There')
    print('Welcome')#2 line breaks after function as per pep 8


greet()
#creating a function with parameters
def adding(a,b):#a, b are parameters
    sum=a+b
    return sum
print(adding(1,2))#1,2 are arguments
#Types of functions
#1)perform a task 2)Return a value
#greet above is of 1st type, adding is of 2nd type
#with return functions, advantage is we can do anything with returned evaluate

def greet1(name):
    print(f'Hi {name}, good morning')

greet1('Gopi')
print(greet1('Gopi')) #will return Hi Gopi, good morning and None
#why None is returned ?
#python functions by default returns None, None is the object which returns lack of something
#though this function is returning None, it classifies as a function which performs a certain task

#keyword arguments
#to make program more readable
def increment(number,by):
    return number+by
print(increment(2,1))#not readable
print(increment(2,by=1))#making it readable by using keywords,we can use keywords for both arguments as well

#Default argumennts
def incre(number,by=1):#default value for by is 1 if not passed
    return number+by
print(incre(5))#6
print(incre(5,5))#10
#all  default arguments should follow non default arguments as a rule, else error

#variable number of argumennts *args
def display(*numbers):
    print(numbers)
display(2,3,4,5)#(2,3,4,5) is printed which is a tuple
#we can iterate over a tuple, and modify above as to print
def display1(*numbers):
    for i in numbers:
        print(i)
display1(2,3,4,5)
def multiply(*numbers):
    total=1
    for i in numbers:
        total*=i
    return total
print(multiply(2,3,4,5,6,7))

#**args for pssing multiple key value pairs or multiple keyword arguments
#python will automatically pacakage them into a data structure called dictionary
def cricketer(**details):
    print(details)
    print(details["name"])#we can only give things defined below in all , status cant be given as it is given only for one cricketer
cricketer(name='sachin',age=50,status='retired',level='elite')
cricketer(name='manish',age=23,level='beginner',iplstatus='active')

#scope
#variables and parameters of a function have scope only in a function, they are called local variables
#global variables have scope anywhere
"""
def scope1():
    message='Hi'
print(message)#will throw error saying message is not defined"""

#we can decalre a global variable instaed by decalring it outside the functions
message='Hi'
def scope1():
    message='Hello'
print(message)#will print Hi

#to modify global variable , we can use global keyword
#but it is a bad practice, since global variables are..
#used throughout by programs , so many blocks of code may depend on initial value of it
message1='Hi'
def scope2():
    global message1 #tells python interpreter to use global variable
    message1='Hello'
scope2()#without this Hi will be printed as variable will not be printed
print(message1)
#debugging --refer code with mosh lecture, can be done with vs code only
#study concepts of debugging step by step and break points
#windows shortcuts video

#fizz buzz coding interview exercise
#if divisble by 3, return Fizz, if divisble by 5 return Buzz,if divisble by both 3 an 5 Fizzbuzz
#for any other number, return same numbers
def fizzbuzz(number):
    if number%3==0 and number%5!=0:
        return 'Fizz'
    elif number%3!=0 and number%5==0:
        return 'Buzz'
    elif number%3==0 and number%5==0:
        return 'FizzBuzz'
    else:
        return number
#what you wrote is more time complex, write algorithm in reverse order (not conditiosn not needed)
#else block not needed as well
print(fizzbuzz(int(input('Enter fizz buzz value'))))

#actual way
def fizzbuzz1(num):
    if (num%3==0) and (num%5==0):
        return 'FizzBuzz'
    if num%3==0:
        return 'Fizz'
    if num%5==0:
        return 'Buzz'
    return num
print(fizzbuzz1(int(input('Enter number for fizzbuzz1:'))))
