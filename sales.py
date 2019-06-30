import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import json
from html.parser import HTMLParser

#initialize driver

CHROMEDRIVER_PATH = "c:\Repo\chromedriver\chromedriver"

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# NAVIGATE TO GOOGLE.COM...

driver.get("https://www.google.com/")
#driver.get("https://www.buzzfile.com/Home/Basic") #https://www.buzzfile.com/Home/Basic
print(driver.title) #> Google
driver.save_screenshot("search_page.png")

# FIND AN ELEMENT TO INTERACT WITH...
# a reference to the HTML element:
# <input title="Search">

searchbox_xpath = '//input[@title="Search"]'
#searchbox_xpath = '//input[@value=""]'
#searchbox_xpath = '//input[@placeholder="SearchbyCompanyName"]'
#searchbox = driver.find_element_by_name('searchTerm')
searchbox = driver.find_element_by_xpath(searchbox_xpath)

# INTERACT WITH THE ELEMENT

search_term = "AMERICAN HEALTH CARE SOFTWARE ENTERPRISES INC owner name linkedin owner"
searchbox.send_keys(search_term)

searchbox.send_keys(Keys.RETURN)
#print(driver.title) #> 'Prof Rossetti GitHub - Google Search'
driver.save_screenshot("search_results.png")

soup = BeautifulSoup(driver.page_source, features = "lxml")
#soup = BeautifulSoup(driver.page_source, 'html.parser')
companylinks = soup.find_all("div", "r")
#companylinks = soup.find_all("span", "company-trade-style") # class name and what class equals


title2 = soup.h3
print(title2)


#linkedin = companylinks["a href"]
#print(linkedin)

#driver.quit()
