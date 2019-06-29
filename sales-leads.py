import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#initialize driver

CHROMEDRIVER_PATH = "c:\Repo\chromedriver\chromedriver"

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# NAVIGATE TO GOOGLE.COM...

driver.get("https://www.buzzfile.com/Home/Basic") #https://www.buzzfile.com/Home/Basic
print(driver.title) #> Google
driver.save_screenshot("search_page.png")

# FIND AN ELEMENT TO INTERACT WITH...
# a reference to the HTML element:
# <input title="Search">

searchbox_xpath = '//input[@placeholder="Search by Company Name"]'
searchbox = driver.find_element_by_xpath(searchbox_xpath)

#
# INTERACT WITH THE ELEMENT
#

search_term = "Benoit Electric"
searchbox.send_keys(search_term)

searchbox.send_keys(Keys.RETURN)
print(driver.title) #> 'Prof Rossetti GitHub - Google Search'
driver.save_screenshot("search_results.png")

#
# ALWAYS QUIT THE DRIVER
#
print(type(search_term))