# Exceptions are used to handle code errors
from timeit import timeit#added to code when at the end we needed this package
# Exceptions
try:
    age = int(input('Enter age:'))
except ValueError as er:
    print('you didnt enter a valid age')
    # print(er)
    # print(type(er))
else:  # only executed if no exceptions are thrown
    print('No exceptions were thrown')
print('Execution continues with next steps')

# Handling different expressions
try:
    age = int(input('Enter age:'))
    Factor = 10/age

except (ValueError, ZeroDivisionError):
    print('you didnt enter a valid age')
# except ZeroDivisionError:
#     print('you didnt enter a valid age')
# better way is above , instead of giving a new error
else:
    print('No exceptions were thrown')
print('Execution continues with next steps')

# Cleaning up
try:
    file = open('SecondLesson.py')
    # now this file needs to be closed,if we put at end of try, it will not close if exception occurs
    # if we keep in exception, it will execute only if exception occurs
    # so the solution is to use a finally block
    age = int(input('Enter age:'))
    Factor = 10/age

except (ValueError, ZeroDivisionError):
    print('you didnt enter a valid age')
# except ZeroDivisionError:
#     print('you didnt enter a valid age')
# better way is above , instead of giving a new error
else:
    print('No exceptions were thrown')
finally:  # use it to close external/shared resources or to execute a piece of code that needs to be
    # run irrespective of an exception or not
    file.close()
    print('file closed')
print('Execution continues with next steps')

# With Statement
# used to automatically release external resources
# file object has magic methods which support context management protocol i.e., __enter and __exit methods
# they automatically close the resource when used with "With"

try:
    with open('SecondLesson.py') as file:
        # with open('SecondLesson.py') as file, open('ThirdLesson.py') as target:
        # we can use with two files as well, python automatically closes both
        print('File opened')
    age = int(input('Enter age:'))
    Factor = 10/age

except (ValueError, ZeroDivisionError):
    print('you didnt enter a valid age')

else:
    print('No exceptions were thrown')
print('Execution continues with next steps')


# Raising Exceptions
def calculate_factor(age):
    if age <= 0:
        raise ValueError('Age cannot be less than or equal to 0')
    else:
        return 10 / age


# calculate_factor(-1)
try:
    calculate_factor(-1)
except ValueError as error:
    print(error)
# without above try excet block, we will get a traceback and not just error given in 'raise'
#  comment the above block and uncomment the above function call line to check


# cost of raising exceptions
# prefer not to raise exceptions as they come with a performance cost
# lets check time taken
# from timeit import timeit
code1 = """
def calculate_factor(age):
    if age <= 0:
        raise ValueError('Age cannot be less than or equal to 0')
    else:
        return 10 / age


# calculate_factor(-1)
try:
    calculate_factor(-1)
except ValueError as error:
    pass
    """
print('First Code', timeit(code1, number=10000))
code2 = """
def calculate_factor(age):
    if age <= 0:
       return None
    return 10 / age


xfactor= calculate_factor(-1)
if xfactor==None:
    pass
    """
print('First Code', timeit(code2, number=10000))
# see difference in code times
# so as more times a program is run, cost of raising an excpetion becomes more
# pass statement to avoid priniting 10000 times, it basically doesnt do anything
