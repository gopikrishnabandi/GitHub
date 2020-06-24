# pip install requets from command prompt
# we use this package to send http  requests
# to activate run, pipenv shell
# change virtual environment from the bottom left hand corner in vs code
# import requests
import requests
# requests has a method get to send an http request for getting data
# first parameter is url to get data from an endpoint, google business search end point
# get method returns a response object
# response = requests.get("https://api.yelp.com/v3/businesses/search")
# print(response)
# we will get response 401 which is an error , i.e., without authentication, need to give api Key and token
# clenaer way along with fixing above issue, commented above two code lines to show correct way
url = "https://api.yelp.com/v3/businesses/search"
# set hedaers as a dict with required key value pairs, this is to avoid 401
api_key = "give api key"
headers = {
    "Authorization": "Bearer "+api_key
}
params = {
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
print(response.text)
# only if authorization is passed in header, we will get erro saying specify location or latitude and longitude
# so give location above, by using one more key word argument called params, just like headers we define a dict for it
# if we give nyc, we get list of businesses in Newyork
# lets filter further more
params1 = {
    "term": "Doctor",
    "location": "NYC"

}
response1 = requests.get(url, headers=headers, params=params1)
print(response1.text)
# what we get is a json object
# it has a property called businesses and is set to an array
# in that array we have a set of json objects
# instead of text attribute call the json method, which will give a dictionary
# result = response1.json()["businesses"]
# instead of result give name as businesses
businesses = response1.json()["businesses"]
# now we have a list of businesses
# if we print now we get a list of dictionaries
# print(businesses)
# Rather each dictionary has key value pairs id, alias, name and so on..
# name is the name of the business
# lets say we only want name
for business in businesses:
    print(business["name"])
# we can take this further, use list comprehension to get businesses which are rated 4*
# [item for item in list], this is the syntax
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]
print(names)


# Hiding API Key
# create a config file with api key and import it instead of directly giving it in the file
# create a .gitignore file to specify the files that should not be uploaded to git
#import config
# config.api_key is the only change in the code above
# create a config.py and place api_key = "your api key" in that
# create a .gitignore and type config.py in it
