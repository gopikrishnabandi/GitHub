# lower case names for variables, meaningful pneumonic names, underscore to seperate words
# for any programs where you need to give output run it from terminal using python filename.py
import math
student_count = 20
price_per_course = 560.0
number_of_courses = 10
revenue = 0
class_high_gpa = True
if student_count >= 10:
    revenue = number_of_courses*price_per_course*student_count
else:
    discount = 0.5
    revenue = number_of_courses*price_per_course*student_count*discount
print('Total Revenue is', revenue)
message = """This is gopi
learning from code with mosh,
going good so far"""
print(message)
course_name = 'Python Programming'
print(len(course_name))
# indexing and slicing a string, index starts from 0 , last letter index is -1 as in opposite direction
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])#from 0 till 2 index, 2 not included
print(course_name[:3])#from start till 3
print(course_name[0:])
print(course_name[:])#no start and end, so means complete
print(course_name[-1:])
print(course_name[-1:-1])
# escape sequenses in python
# \'
# \"
# \\
# \n
course = 'code with \'mosh\''
course_1 = "code with \"mosh\""
course_2 = 'code with \\mosh\\'
course_3 = 'code with \n mosh'
print(course, course_1, course_2, course_3)
# concatenation with formatted strings
first_name = 'gopi'
last_name = 'krishna'
print(first_name+' '+last_name)
print(f'{first_name} {last_name} {"is of length"} {len(first_name)+len(last_name)}')
# string methods
name = ' Arjuna phalguna '
print(name.upper())
print(name.lower())
print(name.title())
print(name.lstrip())
print(name.rstrip())
print(name.strip())
print(name.find('pha'))
print(name.find('Pha'))  # returns -1 if not found
print(name.replace('a', 'A'))
print('pha' in name)
print('guna' not in name)
# Numbers
# a+bj is complex number in python
print(2**3)
print(10/3)
print(10//3)
print(10 % 3)
x = 2
x += 3  # augmented assignment, for any operator it can be used like -, *
print(round(2.9))
print(abs(-2.9))
# import math at top for more functions
print(math.ceil(2.2))
print(math.factorial(5))
# type conversion
x = input('x: ')
print(type(x))
y = int(x)+2
print(y)
print(f'x: {x} y:{y}')
print(bool(""))  # False
print(bool(0))  # False
print(bool(1))
print(bool(-1))
print(bool("False"))  # only emepty string will give false, this will be true
print(bool(None))  # False
