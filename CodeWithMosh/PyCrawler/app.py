# web scraping
# not all websites have apis to work with, so we use parse html and get rid of all tags to get the data
# extract list of new questions on stackoverflow.com
# create new folder PyCrawler
# pipenv install beautifulsoup4(popular html and xml scraper)
# C:/Users/Gopi/.virtualenvs/PyCrawler-wRyG8Zpw/Scripts/activate.bat to go to virtual env
# pipenv install requests(to download webpage that contains newest questions)
# change environment to PyCrawler
import requests
from bs4 import BeautifulSoup
response = requests.get("https://stackoverflow.com/questions")
# response.text returns html content of the webpage, we can create a beautiful soup and parse it
soup = BeautifulSoup(response.text, "html.parser")
# soup object mirrors an html document
# we can find different elements
# right click on first question, and click inspect
# anchor tag has title of questions
# have a div tag with id=questions which is the container for all our questions, it has a class question-summary, lets look at one of the question
# it has two divs,one has class stats container(rating) and other div has summary(title and summary of the question)
# we should use soup to find question-summary
# soup has a method select which takes a css selector, . represents a class. css selector is a string that helps find an element in html doc html doc
questions = soup.select(".question-summary")
# questions is a list of tags
print(type(questions[0]))

print(questions[0].attrs)  # we get elements of the dictionary
print(questions[0].get("id", 0))  # 0 is default value
# we need to get title for each question
# in question-summary, we have summary, we have an anchor tag in it with class attribute=question-hyperlink
# tag object has select method like soup object , wher we can pass a css slector
print(questions[0].select(".question-hyperlink"))
# retuns a list of objects, first object is anchor
print(questions[0].select_one(".question-hyperlink"))  # with anchor
# getText gets just the text
print(questions[0].select_one(".question-hyperlink").getText())

for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
# to get votes
# in statscontainer we have class  stats, which has votes, which has vote-count-post
