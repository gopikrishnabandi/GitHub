# Functions
#they perform a certain task when called
def add(x, y):  # x, y are parameters
    return x+y


print(add(2, 3))  # 2,3 are arguments


def greet(first_name, last_name):
    print(f'Hi {first_name} {last_name}, welcome aboard')


greet('gopi krishna', 'bandi')

# Types of Functions
# 1 perform a task
# 2 return a value
# below examples


def alarm(time):
    print(f'alarm will ring at {time}')


alarm(3)


def newalarm(time):
    return time


message = newalarm(3)
# we can use this to do anaything, like writing to a file , modifying it etc..
print(f'alarm will start ringing from {message-1}')

# All functions by default return None, but they are not classified as type 2

# Check what this does, it will return a None extra


def greet1(Name):
    print(f'Hi {Name}')


# Prints Hi Priya and None as , Hi Priya is alraedy printed by the function and None returned by default is printed
print(greet1('Priya'))

# Keyword Arguments


def increment(number, by):
    return(number+by)


print(increment(2, 1))
print(increment(3, by=1))  # by is akeyword argument to make it more readible
print(increment(number=3, by=1))  # Also valid


# Default arguments

def method1(x, y=2):  # default should follow non default
    return x+y


print(method1(5, 6))  # 11
print(method1(5))  # 7


# Example 2
def method2(x, y=2, z=2):
    return x+y+z


print(method2(51))
print(method2(51, 1, 1))
print(method2(51, 1))

# function with xargs
# variable number of arguments


def multiply(*numbers):  # * will create a tuuple which is an iterable
    total = 1
    for number in numbers:  # iterating over the tuple
        total = total*number
    return total


print(multiply(2, 3, 4, 5))

# xxargs
# passing multiple key value pairs or keyword arguments to the function


def user_save(**user):  # ** will create a complex data type called dictionary or key value pair
    print(user)
    print(user["age"])


user_save(name='Gopi', age=31, experience=9, staus='married')


# Scope
# scope of variables inside a function is local, they cannot be accessedd outside, will give error
# global variables can be modified in  a function by using the global keyword i.e., global variable_name prior to changing its value


# Debugging
# check 9th video for info, F9 to start debug point, F10 to proceed, F11 to step into function
# shift F5 to stop debugger
# shift F11 to step out of a function


# Useful shortcuts for writing code faster
# alt and up down arrows to move a line up down
# shift alt up and down to duplicate a line up/down
# ctrl and / to comment/uncomment a line

# Fizz buzz exercise
#divisble by 3 gives Fizz, divisible by 5 gives Buzz, by both Fizz Buzz
def Fizz_Buzz(input):
    if input%3==0 and input%5==0:
        return 'Fizz Buzz'
    elif input%3==0:
        return 'Fizz'
    elif input%5==0:
        return 'Buzz'
    else:
        return input

print(Fizz_Buzz(15))