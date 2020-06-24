# we may need features not implemented in python standard library
# repositories of pavkages built by pyhon developers
# pypi.org
# we can use as well as publish to this repository


# APIs
# Application Programming Interface
# many website make their data vailable through APIs
# APIs are end points that are publicly accessible, they have urls just like websites
# yelp has an api to serach businesses( avilable at https://www.yelp.com/developers/documentation/v3/business_search)
# end point is GET https://api.yelp.com/v3/businesses/search
# we can send an http request to this end point to get the list of businesses that match a certain criteria
# http is a protocol that powers ou web
# go to first link, click on developer tools in chrome, network tab, click ctrl+r, see all requests
# go to headers tab and see the different parts of the request
# GET is for getting data, POST is for creating data, PUT for updating, DELETE for deleting data
# status code is the staus code we get as response from web server
# we will see how to communicate with yelp api to search business matching certain criteria


# yelp api
# yelp.com/developers
# REST API stands for representational state transfer api(set of rules and conventions to be followed to buid or consume apis for exchanging data)

# fisrt we have to create an app, go to yelp fusion, documentation
# https://www.yelp.com/developers/documentation/v3
# left handside you can find a button to create app
# generate client id and key which will be needed

# Searching for businesses

# Continued in PyYelp Folder app1.py

# Hiding API Keys
# in PyYelp Folder app1.py

# to come out of a virtual env enter deactivate
# after that use cd  command to navigate to respective folder and create a virtual envi for that

# sending text messages
# in PyText Folder
# create folder PyText
# type cd PyText in terminal, then code . to open vs code for that folder
# continued in app.py in that folder


# web scraping
# not all websites have apis to work with, so we use parse html and get rid of all tags to get the data
# extract list of new questions on stackoverflow.com
# create new folder PyCrawler


# browser Automation
# check github login and check name on right corner account profile
# new project PySelenium
# pip env install selenium in terminal
# we need driver to automate browsers
# pypi.org search selenium, under srivers we see drivers for diff browsers, copy to windows c drive
# change virtual envi


# work with excel spreadsheets
# project PyExcel
# in project we have transcations.xlsx
# pipenv install openpyxl
# select virtual environment from status bar of vs code

# command query violation
# PyExcel app1.py


# Numpy
# PyNumbers
