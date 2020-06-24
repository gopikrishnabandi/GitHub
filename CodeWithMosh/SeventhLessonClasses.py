# Classes
# Class is a blueprint to create  new objects
# object is an instance of a class
# class:Human, Object:Gopi,Priya

# creating a class
# pascal naming convention, every Word is capital, no underscores


from collections import namedtuple
from abc import ABC, abstractmethod


class Point:
    def draw(self):  # all functions in class shouls have one parameter
        print('Drawing point')


point = Point()
print(type(point))
print(isinstance(point, Point))  # True, point is an instance of Point Class
print(isinstance(point, int))  # False, not an instance of int
point.draw()

# constructors


class Human:
    def __init__(self, x, y):
        self.x = 'Created by God'
        self.y = 'To do good'

    def walk(self):
        print(f'We are humans and we are {self.x} {self.y}')


obj = Human(0, 0)
obj.walk()  # no need to give self, python interpreter automatically does it

# class vs instance attributes


class Employee:
    ceo = 'Jeff'  # Class attribute, will be same for all instances of the class
    # can be accessed both with instance and class names

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def details(self):
        print(
            f'The employee details are name is {self.name} and dept is {self.dept}')


emp1 = Employee('Gopi', 'BI')
emp1.details()
emp1.salary = 200000
print(emp1.ceo)
print(Employee.ceo)
print(emp1.salary)
emp2 = Employee('Priya', "Coding")
print(emp2.ceo)

# class vs instance methods
# class method is defined at a class level


class Students:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def startattendance(cls):
        return 'starting attendance is zero for all students'

    def labno(self):
        print(f'The lab number is LB-{self.x} and labidentiy is LB-{self.y} ')


stu1 = Students.startattendance()
print(stu1)
# stu1.labno() will throw an error
stu2 = Students(1, 'Gopi')
stu2.labno()

# Magic methods
# they are called by python interpreter automatically, have two underscores before and after


class Students1:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'

    def labno(self):
        print(f'The lab number is LB-{self.x} and labidentiy is LB-{self.y} ')


stu2 = Students1(1, 'Gopi')
print(stu2)  # prints module.classname and address as that is the default implementation of __str__ magic method
# however we can redefine it as above, the above code block of __str__ is added after this comment is written
# so dont be confused


# Comparing objects
class Students2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def labno(self):
        print(f'The lab number is LB-{self.x} and labidentiy is LB-{self.y} ')


stu2 = Students2(1, 'Gopi')
stu3 = Students2(1, 'Gopi')
stu4 = Students2(2, 'Priya')
# returns false without magic method, as it comapres refrences of these objects
print(stu2 == stu3)
print(stu4 > stu3)
# no need to define a seperate magic method for less than though it exists, __gt__ can be used
print(stu4 < stu3)


# Performing Arithmetic operations
class Records:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Records(self.x+other.x, self.y+other.y)


aud1 = Records(1, 2)
aud2 = Records(2, 3)
# add method above returns a Records object , so printing it will print reference
print(aud1 + aud2)  # prints reference
combined = aud1 + aud2
print(combined.x, combined.y)  # prints correctly


# Making Custom Containers
class TagCloud:
    def __init__(self):
        # declaring an empty dictionaryand assigning the tags
        self.tags = {}

    def add(self, tag):
        # o is default value if the tag doesnot exist
                # so if new tag comes , by default it is not in dict, so assigned 0
        # after +1 it becomes 1
        # later after that if same tag comes, get will return 1 , so 1+1 is 2
        # self.tags[tag] = self.tags.get(tag, 0) + 1
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # used to read a number of a given tag
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

# to know no of items in the TagCloud
    def __len__(self):
        return len(self.tags)

# if we want to iterate over the container
    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add('Python')
cloud.add('Python')
cloud.add('python')
# so to avoid reading lower case a different tag , we can use lower method
print(cloud.tags)

# if we want to access like this cloud["Python"], to implement this we need to use a magic method
# getitem magic method above is used for the same
# for setting a tag count, we can use the set method above
cloud['Java'] = 8
cloud.add('Ruby')
print(cloud['Ruby'])
print(len(cloud.tags))

for x in cloud:
    print(x)


# Private Members
# above code has an issue
# try below, uncomment next line and try to know the issue
# print(cloud.tags["PYTHON"])
# We will get key error as everything is stored in dictionary as lowercase

# so we need to hide the .tags attribute , so that we cannot use it from the outside
# self on tags in the constructor, press F2(used to change in visualstudiocode)
# prefix with two underline to make it inaccessible/private
# technically still can access, but will be difficult to access by mistake
class TagCloud1:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud1 = TagCloud1()
cloud1.add('Python')
cloud1.add('Python')
cloud1.add('python')

print(cloud.tags)

# now with __ added, we dont have in dropdown .tags or __tags
# but still can access, but harder
# every class has __dict__ property which gives all attributes

print(cloud1.__dict__)
# __tags is renamed as _TagCloud1__tags
print(cloud1._TagCloud1__tags)

# so unlike java, C# , in python we dont have private members.
# private memebers are still accessible
# __ is more of a convention to avoid accidental access


# Properties--Read again
# want to have control over an attribute in class
# say price of product cannot be negative
# we can make this field private and define two methods for setting and getting value
class Product:
    def __init__(self, price):
        #self.__price = price
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


# product = Product(-50)
product = Product(100)

# above is unpythonic , we can use a property
# a property is an object that sits infront of an attribute and allows to set and get the values of it


class Product1:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
    # if we comment this block , we can only have read only property, we cannot change it, will get error if we try to update


product = Product1(10)
print(Product1.price)


# Inheritance
# in programming we have a concept called "Dry"-Dont repet yourself
# so without inheritance we will exactly be doing that , if we need to declare common methods across different classe

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# to inherit write Base(Parent) class in the brackets of the Sub(child) Class


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()

f = Fish()
f.eat()
print(f.age)

# The object class
# Every class is a sub class of "object" class in python
# All the below statements are True
print(isinstance(f, Animal))
print(isinstance(m, Animal))
print(isinstance(Animal, object))
print(issubclass(Animal, object))
print(issubclass(Fish, object))
print(issubclass(Mammal, Animal))

# Method Overriding
# Replacing or extending a method defined in the base class
# In this example we are extending the __init__ method in parent class in child class by specifying its own attributes


class Animal1:
    def __init__(self):
        print('Animal Constructor')
        self.age = 1

    def eat(self):
        print("eat")

# say we want to set eye color of the Mammal in its constructor


class Mammal1(Animal1):
    def __init__(self):
        # This below statement can be down as well , i.e., we can call it after child constructor
        super().__init__()
        print('mammal constructor')
        self.eyecolor = 'black'
        # super().__init__()

    def walk(self):
        print("walk")


m1 = Mammal1()
print(m1.eyecolor)
print(m1.age)
# This above statement will throw an error without super keyword  given in Sub class
#  as the constructor in sub class replaced the one in base class
# This is called method overrriding
# without super, the __init__ in child class will replace the parent for all of its own objects


# Multi Level Inheritance
# introduces problems, limit yourself to one or two levels
# eg is Animal(Base) class has eat which has a child class called Bird, which has a function fly
# the Bird class is inherited by Chicken class, so chicken can use the fly method. But chickens cant fly which is an issue


# Multiple Inheritance
# In python a class can have multiple base classes or can inherit from multiple classes
# Just like multi level inheritance , it is a source of issues if not used properly

class Employee_Eg:
    def greet(self):
        print("Employee greet")


class Person_Eg:
    def greet(self):
        print("Person Greet")


class Manager_Eg(Employee_Eg, Person_Eg):
    pass


m = Manager_Eg()
# lets see what happens when we call greet method for this object of Manager class
# which greet will be printed
m.greet()
# Employee greet will be printed as interpreter will first encounter "Employee" in the class definition
# interepreter first will check in the original class,next 1st base class will be used and so on
# this above behavior is undesirable, because if someone by mistake or intentionally move the order of inheritance, program will produce different results
# There are good examples of Multiple inheritance as well , Eg: Flyer, Swimmer ,FlyingFish(child)
# problem is only when we have common methods in base clases or if the size of Base classes become big and complex, will add unnecessary issues


# A good Example of inheritance
# Reading data from multiple streams

class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            # custom exception, all exceptions are inherited from Exception class
            # see syntax above on how to create it
            raise InvalidOperationError("stream is already open")
        self.opened = True

# close is exactly opposite of open , so reuse code, copy paste and change
    def close(self):
        if not self.opened:
            # custom exception
            raise InvalidOperationError("stream is already closed")
        self.opened = False

# Reading is different for Files and N/w , whereas opening and closing a stream is same
# thats why this is a good case of inheritance , as commong properties are being inherited
# while the native logic for reading is being defined in the child class


class FileStream(Stream):
    def Read(self):
        print('Reading Data from a File')


class NetworkStream(Stream):
    def Read(self):
        print('Reading Data from a Network')


# Abstract Base Classes(abc)
# There are two issues with above example
# 1) We can instantiate the Base Class Directly i..e, we can cdoreate s=Stream() and s.open()
# we dont know whether it is a file or a Network
# the correct way is to instantiate subclass  and open
# so we should make the base class Abstract, so that we cannot instantiate it

# 2 second issue , if say in future we have one more stream, it should have a method exactly called Read
# so that the code is consistent with other streams(sub classes)
# that is it will be good to have a common interafce

 # the solution for both issues is to make base class is abstract(like a half baked class)
 # pupose is to provide common code to its derivatives

# 1st step is importingabstract base class, refer from statement below
# next make the class you want to make abstract by inheriting from ABC
#from abc import ABC,abstractmethod
# this makes instantiating an object not possible


class InvalidOperationError1(Exception):
    pass


class Stream1(ABC):  # To make Stream1 an abstract class
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            # custom exception
            raise InvalidOperationError1("stream is already closed")
        self.opened = False

    # this is problem 2 , we define a method with no implemntation and decorate with abstractclassmethod
    @abstractmethod
    def Read(self):
        pass


class FileStream1(Stream1):
    def Read(self):
        print('Reading Data from a File')


class NetworkStream1(Stream1):
    def Read(self):
        print('Reading Data from a Network')


class MemoryStream(Stream1):
    # if we dont define this method, it will throw error , because abstract methods from Base class have to be defined in child class
    # otherwise the child class will also be abstract , which is an error
    def Read(self):
        print('Reading Data from a Memory Stream')


# stream = Stream1() will cause error as we cannot now create an object on abstract class


# PolyMorphism
# https://www.digitalocean.com/community/tutorials/how-to-apply-polymorphism-to-classes-in-python-3
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class DropDownList(UIControl):
    def draw(self):
        print('Drop Down')


class TextBox(UIControl):
    def draw(self):
        print('Text Box')


def draw(controls):
    for control in controls:
        control.draw()  # draw method is taking many forms (draw method could be called on dropdown, text box etc..), being detirmed at run time
        # That is why it is called polyMorphism


ddl = DropDownList()
tb1 = TextBox()
# print(isinstance(ddl,UIControl)) True
# draw doesnt know what control it is woking with, it only knws at run time
draw([ddl, tb1])

# Python is a dynamica typed language , as we need not provide type of variable like C, Java etc..
# the type is automatically derived at run time
# we have the option of providing the data type still, but there is no need for the same


# DuckTyping
# Previous lesson show polymorphism
# Base class hasan abstract method
# But since python is a dynamically typed language
# we dont necessarily need the UIControl as the base class
# in other words we can delete base class and implement polymorphism
# because no where we have defined "Controls" object , it just has to be an iterable
# And the individual objects should have draw method
# this is called duck typing
# Python doesnt check for the type of controls objects being passed
#  the iterable parts have to have a draw method thats it
# look at below example to understand(it is a modified version of above to show how ducktyping works and polymorphism is implemented)


class DropDownList1():
    def draw(self):
        print('Drop Down')


class TextBox1():
    def draw(self):
        print('Text Box')


def draw1(controls):
    for control in controls:
        control.draw()


dd2 = DropDownList()
tb2 = TextBox()
# print(isinstance(ddl,UIControl)) True
# draw doesnt know what control it is woking with, it only knws at run time
draw1([dd2, tb2])


# Extending built in types
# we can also extend/inhereit built in classes

class Text1(str):
    def duplicate(self):  # self represents the current object which in this case is an intance of a String class
        return self + self  # so here we are concatenitaing a string with itself


text1 = Text1("Python")
# now text1 can access all methods of "String" class
print(text1.lower())
print(text1.duplicate())


class TrackableList(list):
    # Extend append method of list class
    def append(self, object):
        print("Append Called")
        # instead of defining or overwriting , we are simply calling the append method of super class which is "List" class
        super().append(object)
        # hence this is more like extending than overriding, still called method overriding though as a name


list1 = TrackableList()
list1.append("1")
# This is how we implement Extending of built in classes

# Data Classes
# we will come across classes which may not have any methods, just data(attributes)


class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point1(1, 2)
p2 = Point1(1, 2)
print(p1 == p2)  # returns false as python compares address of p1 and p2 (this is before magic method is added, comment that to check)
# you can check this with print(id(p1)) and print(id(p2))

# we can implement a magic method declared above to solve this

# there is a better implementation than this in these kind of data classes
# we use namedtuple , it is   factory function for creating tuple subclasses with named fields
#from collections import namedtuple
# Creating a namedtuple
# We are creating a namedtuple of name Point2
# Point2 the argument is the name of the namedtuple, hence same name is given to the class object being crated, but we can assign any name
# Field names should be string else error, i.e, x and y
Point2 = namedtuple("Point2", ["x", "y"])
p3 = Point2(x=1, y=2)
p4 = Point2(x=1, y=2)
print(p3 == p4)
#namedtuple is immutable
# so p3.x=10 give an error
# rather we can create an new point like p5=Point2(x=10, y=2)
