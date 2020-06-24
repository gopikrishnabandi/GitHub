# Modules are used to group relatable content in one file, just like how a supermarket has isles
# else if we put all code in only file, it will be difficult
# Better way to import is as below , instead of from SeventhLessonClasses import * as we will only import what we need
# also by import * , we run into the risk of overriding the methods withe same name
# press control +space after import to know the list of methods in the module we are importing from
# another way is to write import FileName and write methodname(Arguments)
# Creating Sales.py to explain conceps
from ecommerce.shopping import greetings
import sys  # this statement is used for a later example, skip for now
from ecommerce.Sales import calc_tax
import ecommerce.Sales
from ecommerce.Sales import calc_shipping, calc_tax
from ecommerce import Sales
ecommerce.Sales.calc_shipping()
calc_tax()
Sales.calc_shipping()
Sales.calc_tax
# compiled pyhton Files
# modules that are imported conce compiled are stored in __pychache__ for future compilations performance
# used for faster compilation times and module loading
# only if datestamp of the modules we imported changes wrt the cache file, it will recompile
# else it will used the already compiled file, format of that file is .pyc
# when running from this current file we will not have cache of this file as it already has it now during runtime, only will cache whichever we are importing
# also in the compile file name we can see which falavor and version of python is being used, in this case it is cpython 3.7


# ModuuleSearchPath
# when we import sales it will look for sales.py in current direcetory
# if not found it will find in bunch of directories
# how do we know those paths where python will search for Sales, if it is not found in current directory
# we can know by import sys and sys.path
print(sys.path)


# how can we import Modules from a subdirectory
# this is our next topic
# Packages
# As project grows , we may have to keep hundreds of files in logical subdirectories instead of main directory
# Else it will become very difficult to organize or edit code
# we are going to create a new subdirectory called E Commerce and move the sales.py there
# once we move Sales.py to a new subfolder we get an error
# so we need to make ecommerce a package
# create a file with name '__init__.py'
# package is a container for one or more modules
# in file system terms, Package is mapped to a directory, a module is mapped to a file
# change import Sales to import ecommerce.Sales, wherever sale. is used prefix with ecommerce.
# this makes code noisy, to avoid this we can use from statement
# from ecommerce.Sales import calc_shipping, calc_tax
# if too many we can import Sales as an object i.e., from ecommerce import Sales
# all combinations are listed above


# SubPackages
# as packages grow we may want to break them into subpackages
# create a subfolder called shopping in ecommerce
# add __init__.py in shopping to make it a package
# if Sales.py is then moved to shopping folder to use it..
# from ecommerce.shopping import Sales will be the logic
# not moved here in this exercise to avoid already clumpsy and confusing code
# rather created a new file called greetings
#from ecommerce.shopping import greetings
greetings.welcomegreeting()
# intra package references
# we sometimes want to import from sibling packages
# say in Sales.py we want to use contact
# we have in ecommerce , customer and in it we have the contact.py
# we can use absolute and relative import statements
# absolute import
#from ecommerce.customer import contact
# contact.phonenumbers()
# code is written in Sales.py open that

# relative import
# from . represents the current package
#  .. takes one level up
# we will be at ecommerce level with two dots
#from ..customer import contact
# it is recommened to use absolute import
# only if it becomes like from A.B.C.D and so on use relative import


# The dir() Function
# dir built in function gives list of methods and atributes in an object
print(dir(Sales))
print(Sales.__name__)  # Name of our module
print(Sales.__package__)  # Name of package
print(Sales.__file__)  # Path to the file


# Executin Modules as Scripts
# when we write anything in Sales.py which we are importing here that will be executed when the module is loaded, refering to the print statement at the beginning
# in from statement itself we get print, no need to call any method
# using same technique we can write initilization code for our packages
# go to __init__.py file and add a print there i.e., in ecommerce folder
# now go to Sales Module and print the Name of the module
# when we run from here , see what happens, we get name as ecommerce.Sales
# when we run Sales.py we see we get name as __main__
# because name of program that starts our code is always main
# in other file where we import we get the name of the module
# go to Sales.py and an if block in the end
# if __name__ == "__main__":
#     print('Executing Locally')
#     calc_tax()
# with this code we can use Sales.py file as a script or a reusable module in another module
# when we import __name__ is no longer main , the logic will be according to the functions that will be used
