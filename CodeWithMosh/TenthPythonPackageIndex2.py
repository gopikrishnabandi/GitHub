# publsihing packages to pypi.org
# create a new account
# next on terminal install 3 tools globally(chaange python environment on bottom left cornor of the tool)
# pip install setuptools wheel twine
# lets say we are going to create a package to work with pdf files
# create a new project directory which will have the pckage we are going to create
# mkdir gopipdf
# cd gopipdf
# code . to open vscode in new window with this dir
# as best practice we should create a high level directory with the same name as our package
# create new folder under gopipdf with same name, in vs code window
# we can create another folder called tests for unittests, data for high level data
# all our source code will bein gopipdf
# add __init__.py to make it package
# add pdf2text.py
# in order to pubish this to pypi , we need to add theree files
# add setup.py at the root
# go to the corresponsing file for the next steps
# now after setup , we need to create readme file, the one we create will be displayed in home page of our package in pypi
# README give in capitals as convention
# README.md , md is short for markdown
# we can use markdown syntax, for now just create plain text for understanding
# we will need a license file(again in root of project like the two files above)
# go to choosealicense.com, select want improvements template and copy that into our file
# go to setup.py and set long description from empty string to the content of the readme
#from pathlib import Path
# Path("README.md").read_text()
# now everything done, we need to genearte a distribution package
# in terminal of setup.py, run python setup.py sdist bdist_wheel (source distribution and built distribution)
# two dir's build and dist are created
# in dist we have a wheel file which is built distribution as well as another file which is a source distribution
# both are zip files, we can unzip them and see if needed
# final step is to upload them to pypi.org
# we use twine to do that
# in terminal twine upload dist/*
# give username and password when prompted (pypi login details)
# https://pypi.org/project/gopipdf/1.0/
# we can install our pacakges like other packages in pypi
# pipenv install gopipdf
# after install we can use them in any program
#from gopipdf import pdf2text
# pdf2text.covert()


# docstring
#import math
import math
print(math.ceil(9.2))
# for above we get documentation/tool tip when we are using
# go to pdf2text.py for next steps, we use docstrings i.e., triple quotes to acheieve this
# from gopipdf import pdf2txt,if we use this we will see documentation when we are typing,created app.py fle to viw this
# calsses also will be documented

# pydoc
# in python we have an ultiliy called pydoc which comes with python installation
# in terminal type pydoc math to see documentation for math module
# in widnows python -m pydoc math
# for next page press space
# to exit press q in terminal
# python -m pydoc gopipdf.pdf2txt, run this in the other window opened
# we can write this documentation to a html file
# python -m pydoc -w gopipdf
# we can also load doumentation to a webserver
# python -m pydoc -p 1234, 1234 is the port number
# Server ready at http://localhost:1234/
# list of all modules and packages in our system along with python official documentation
