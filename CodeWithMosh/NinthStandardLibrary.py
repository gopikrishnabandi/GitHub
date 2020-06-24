# Working With Path
# Working with Files and Directories
import json
import csv
from zipfile import ZipFile
import shutil
from time import ctime
from pathlib import Path
# we can use a rawstring prefix to avoid \\ in the directory path, this is to avoid \\ being treated by python as an escape sequence
# there are differentt ways to create a path object
# Path(r"C:\Program Files\Microsoft ") with rawstring one \ is enough
# Path() represnts current folder
# Path("ecommerce/__init__.py")    #relative path
# Path()/Path("ecommerce") Combine Path objects
# Path()/"ecommerce"/"__init__.py" Combine Path object with a string/strings
# Path.home() #returns home directory of the current user
# we will use the one in line 8 i.e, relative path for this exercise
path = Path("ecommerce/__init__.py")

# Path object has various useful members
# python 3 pathlib in google to see all, we will see some imp here
print(path.exists())  # to see if the file/directory exists
print(path.is_file())  # to check if the path represents a file
print(path.is_dir())  # to check if the path is a directory
print(path.name)  # returns file name in this path __init__.py
print(path.stem)  # returns file name without extension i.e., __init__
print(path.suffix)  # returns extension of the file
print(path.parent)  # returns parent folder
# create a new path object based on tthis existing path but only change the name and the extension of the file
path = path.with_name("file.txt")
print(path.name)  # ecommerce/file.txt
print(path.absolute())
# returns absolute path C:\Users\Gopi\Documents\GitHub\CodeWithMosh\ecommerce\file.txt
# This file doesnt exist yet , they are only representing its path
# similar to with_name we have with suffix
# we use that to change extension of a file
path = path.with_suffix(".py")
# note that we have not renamed the file , we are only repesnting path object
print(path)


# Working witth Directories
path = Path("ecommerce")
# all the below are self explonatory
# path.exists
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")
path.iterdir()  # we can get list of files and directories in this path
# python returns a generaor object as there can be a million files in this
print(path.iterdir())
for p in path.iterdir():
    print(p)

# if there are less files , we can convert the generator to a list comprehension
files_and_dir = [p for p in path.iterdir()]
print(files_and_dir)
# we get array of WiindowsPath objects
# Path is base class for PosixPath and WindowsPath classes
# Posix is standard in unix based OS, in windows we will see Windows
# if we want only directories
dir1 = [p for p in path.iterdir() if p.is_dir()]
print(dir1)
# this is useful to get list of files and directories
# but has two issues, cannot sarch by pattern , second cannot search recursively
py_files = [p for p in path.glob("*.py")]  # *.* for all files
print(py_files)
# for recursive we can use rglob method
# we will get all .py files in ecommerce and its children
py_files_r = [p for p in path.rglob("*.py")]
print(py_files_r)


# Working with Files
path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink() to delete
print(path.stat())  # to get information/stats regarding the file
# gives info like size ,last access time, modified time , creation time etc..
# you will get time in seconds after epic (i.e., computer time and this is platform dependent)
# to get human readabale time , from time import ctime
print(ctime(path.stat().st_ctime))
print(path.read_text())  # prints everything in the file as a string
# this is better than with open as ..
# path.write_text("blah blah blah")
# However for copying, not ideal
# we have to write target.write_text(source.read_text()) with source and target being path objects of Source and Target Respectively
# there is a better way, using shutil module(shell utilities module which has different copying/moving files and directories)
# import shutil
# source=Path("ecommerce/__init__.py")
# target=Path()/"__init__.py"
# shutil(source, target)

# Working with zip files
# from zipfile import ZipFile
# will create a file in our current folder , which we assign to zip
# with ZipFile("files.zip", "w") as zip:
# lets say we want to get all files in the current directory and write them to this zip file
# so we create a path object to reference the ecommerce directory  and call rglob to recorsively find all
# files in this directory and all its children
# Path returns a generator , so we iterate over it
# for path in Path("ecommerce").rglob("*.*"):
#     zip.write(path)
# zip.close()
# if something goes wrong, zip.close may not be called ,so we should use a try finally
# or even better the with statement , which is shorter and cleaner
# so comment out zip.close and add a a with statement in above code
# when we run this we will get a zip file
# comment above lines once zip is created and run below code(Line 96,101-103)
# write below code to read from the same
with ZipFile("files.zip") as zip:  # in read mode no need to use r
    print(zip.namelist())  # prints list of all files in this zip
# we can get information on any of the files
    info = zip.getinfo("ecommerce/__init__.py")  # returns an info object
    print(info.file_size)
    # since size is small file size will be same as compress size as there is nothing much to compress
    print(info.compress_size)
# to extract all files from a zip file
    # will extract into extract directory, will create once we run and have all the eecommerce files and directories
    zip.extractall("extract")

# Working with CSV Files(Comma seperated Value)
# import csv
# we cannot use path, so we will use open
with open("data.csv", "w") as file:
    # csv module has a writer method
    # first parameter has to be a file object for this method, that is why we cannot use path
    writer = csv.writer(file)  # givesa csv writer object
    # we can write tabular data with the writer to our csv file
    # headings in first row
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([5000, 2, 3])
    writer.writerow([6000, 3, 51])
# we will have a data.csv file create in our project folder
# to read the data
# with open("data.csv") as file:
#     reader = csv.reader(file)
#     print(list(reader))
# each line is printed as a list in terminal
# each value in list displayed as a string, eventhough we are dealing with a number, so onus on us to convert to int,float etc..
# we can also iterate over this reader object because it is an iterable
    # for row in reader:
    # print(row)
    # the above tow lines will not return output as print(list(reader)) will ove index of list to end of file, so comment that out to dispaly
# suppose we have a directory with thousands of csv files
# we can itearte over the directory, open the csv file and remove the first row  , so we can do many interesting things
# one more example is calculating sum of a bill over different transactions
