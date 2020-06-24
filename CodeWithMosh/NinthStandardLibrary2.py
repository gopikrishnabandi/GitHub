# Working with Json Files
# json stands for java script object notation
# popular way to format data in human readable way
# import json
from pathlib import Path
import json
# below code is commented when running second part of the program i.e., reading from json
# writing to json files
# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Kindergarten Cop", "year": 1993}]
# data = json.dumps(movies)
# # print(data)
# #from pathlib import path
# Path("movies.json").write_text(data)
# to read data from json
# comment above code
data = Path("movies.json").read_text()
# we need to parse the string "data" into an array of objects
movies = json.loads(data)
print(movies)
# we can get any items in the array
print(movies[0])  # 1st record
print(movies[0]["title"])  # Terminator
