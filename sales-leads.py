import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import json
from html.parser import HTMLParser
import os

#initialize driver

CHROMEDRIVER_PATH = "c:\Repo\chromedriver\chromedriver"

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

companies = ["AMERICAN HEALTH CARE SOFTWARE ENTERPRISES INC owner linkedin owner", "AMBULATORY CARE OF WARTBURG"]

csv_file_path = os.path.join(os.path.dirname(__file__), "data", "contacts.csv")
csv_headers = ["company name", "results"]
    

for search_term in companies:
    #navigate to google
    driver.get("https://www.google.com/")
    #driver.get("https://www.buzzfile.com/Home/Basic") #https://www.buzzfile.com/Home/Basic
    print(driver.title) #> Google
    #driver.save_screenshot("search_page.png")
    # FIND AN ELEMENT TO INTERACT WITH...
    # a reference to the HTML element:
    # <input title="Search">
    searchbox_xpath = '//input[@title="Search"]'
    #searchbox_xpath = '//input[@value=""]'
    #searchbox_xpath = '//input[@placeholder="SearchbyCompanyName"]'
    #searchbox = driver.find_element_by_name('searchTerm')
    searchbox = driver.find_element_by_xpath(searchbox_xpath)
    # INTERACT WITH THE ELEMENT
    print(search_term)
    searchbox.send_keys(search_term)
    searchbox.send_keys(Keys.RETURN)
    #print(driver.title) #> 'Prof Rossetti GitHub - Google Search'
    #driver.save_screenshot("search_results.png")
    soup = BeautifulSoup(driver.page_source, features = "lxml")
    #soup = BeautifulSoup(driver.page_source, 'html.parser')
    companylinks = soup.find_all("div", "r")
    #companylinks = soup.find_all("span", "company-trade-style") # class name and what class equals
    title = soup.title
    results = soup.h3
    print(results)
    with open(csv_file_path, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        writer.writerow({
            "company name": title,
            "results": results, 
            })
    
#linkedin = companylinks["a href"]
#print(linkedin)

#driver.quit()