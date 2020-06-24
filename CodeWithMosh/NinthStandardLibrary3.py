# Working with sqlite3
# sqlite is very light weight and is perfect for small mobile apps and desktop apps
# in last program we created .json, lets write that into a table
import sqlite3
import json
from pathlib import Path
movies = json.loads(Path("movies.json").read_text())
print(movies)
# now we want to store the movies in a database
# database file name can be anything, if it doesnt exists this line will create it
with sqlite3.connect("db.sqlite3") as conn:
    # a connection object is created with above statement
    command = "INSERT INTO Movies VALUES(?,?,?)"  # sql statement
    for movie in movies:
        # 2nd argument we only need values to be inserted in a table called Movie where structure is already defined, we insert values as a tuple
        conn.execute(command, tuple(movie.values()))
    conn.commit()  # with this all changes will be written to the database
# if we run the program we are going to get an error, operational error, no such table, Movies
# at this point we have an empty database and havent defined any tables
# search google for dbbrowser for sqlite3 and install the same, which has UI to create database objects
# once installed, open db.sqlite3 file from open database tab(the file is created only when you run the program once)
# create table called Movies with 3 fiields, id , title and year with id as pk, and the rest two as not null
# cick write changes
# now run program again
# now go to Dbbrowser and view table data
# how to read data from a table database
# comment above line and uncomment below to see
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "select * from Movies"
#     # when we read data from database we get a cursor object, hence name given like that
#     cursor = conn.execute()
#     # cusror is an iterable object
#     for row in cursor:
#         print(row)  # returns each rows as one tuple
#     # cusror will be at end of file after this remember
#     # conn.commit is only needed for writing
#     # alternatively we can use below which gives a list of all rows as a list
#     movies = cursor.fetchall()
#     print(movies) #we get a list of tuples
