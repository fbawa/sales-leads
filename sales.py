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

csv_file_path = os.path.join(os.path.dirname(__file__), "data", "source.csv") # a relative filepath

with open(csv_file_path, "r") as source: # "r" means "open the file for reading"
    reader = csv.reader(source) # if your CSV doesn't have headers
    source_comp = list(reader) #companies = ["AMERICAN HEALTH CARE SOFTWARE ENTERPRISES INC", "AMBULATORY CARE OF WARTBURG"]

companies  = [val for sublist in source_comp for val in sublist] # getting rid of the brackets

csv_file_path = os.path.join(os.path.dirname(__file__), "data", "contacts.csv")
csv_headers = ["Company Name", "Results", "Links"]
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
for search_term in companies:
    #navigate to google
    driver.get("https://www.google.com/")
    print(driver.title) #> Google
    searchbox_xpath = '//input[@title="Search"]'
    searchbox = driver.find_element_by_xpath(searchbox_xpath)
    # INTERACT WITH THE ELEMENT
    print(search_term)
    searchbox.send_keys(search_term + " ceo founder owner linkedin")
    searchbox.send_keys(Keys.RETURN)
    #scrape the results
    soup = BeautifulSoup(driver.page_source, features = "lxml")
    title = soup.title
    results = soup.h3.text #drop a breakpoint, get class, and get dir to see what you can invoke
    link = soup.cite.text
    with open(csv_file_path, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writerow({
            "Company Name": search_term,
            "Results": results, 
            "Links": link,
            })
    
#driver.quit()
