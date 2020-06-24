# browser Automation
# check github login and check name on right corner account profile
# new project PySelenium
# pipenv install selenium in terminal
# we need driver to automate browsers
# pypi.org search selenium, under drivers we see drivers for diff browsers, copy to python home drive
# change virtual envi
# C:\Users\Gopi\Documents\GitHub\CodeWithMosh>C:/Users/Gopi/.virtualenvs/PySelenium-rCKkkFmX/Scripts/activate.bat
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://github.com")
# we can find elemnts by class, id, name
# we need to find sign in
signin_link = browser.find_element_by_link_text(
    "Sign in")  # retuns a web element
signin_link.click()
# inspect elemnt of username
username_box = browser.find_element_by_id("login_field")
# to fill we have send_keys
username_box.send_keys("give ur username")
password_box = browser.find_element_by_id("password")
password_box.send_keys("give ur pwd")
# to submit
password_box.submit()

# to verify gopikrishnabandi is in the right corner , we can use page_source method
assert "gopikrishnabandi" in browser.page_source

# one more way
# inspect element, class name is user-profile-link
profile_link = browser.find_element_by_class_name("user-profile-link")
# we need to find the innerhtml
link_label = profile_link.get_attribute("innerHTML")
# now we need to assert
assert "gopikrishnabandi" in link_label
# read more about waits and page objects in selenium-python documentation to learn more, this helps organising and reuse of code as test cases
browser.quit()  # this is to close browser windows
