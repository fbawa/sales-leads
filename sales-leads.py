import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

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

search_term = "Pepsi"
searchbox.send_keys(search_term)

searchbox.send_keys(Keys.RETURN)
#print(driver.title) #> 'Prof Rossetti GitHub - Google Search'
driver.save_screenshot("search_results.png")


#
# ALWAYS QUIT THE DRIVER
#
#response = requests.get("https://www.buzzfile.com/Search/Company/Results?searchTerm=Pepsi&amp;type=1")
#response_html = response.text

#soup = BeautifulSoup(response_html, features = "lxml")
soup = BeautifulSoup(driver.page_source, features = "lxml")

#titles = soup.find_all("span", "title")

#print(type(titles)) #> <class 'bs4.element.ResultSet'> (like a list)
#print(titles[5]) #> <span class="title">Macbeth</span>
#print(titles[5].text) #> Macbeth
#exit()

companylinks = soup.find_all("span", "search-display-info") # class name and what class equals

print(companylinks)




exit()
books = []
for list_item in booklinks:
    title = list_item.find("span", "title").text #> class name and what class equals
    author = list_item.find("span", "subtitle").text #> "William Shakespeare"
    downloads = list_item.find("span", "extra").text #> '830 downloads'
    downloads_count = int(downloads.replace(" downloads", "")) #> 830
    book = {"title": title, "author": author, "downloads": downloads_count}
    print(book)
    books.append(book)

print(books[2]["title"]) #> Macbeth


#booklinks = soup.find_all("li", "booklink") # class name and what class equals

#books = []
#for list_item in booklinks:
#    title = list_item.find("span", "title").text #> class name and what class equals
#   author = list_item.find("span", "subtitle").text #> "William Shakespeare"
 #   downloads = list_item.find("span", "extra").text #> '830 downloads'
  #  downloads_count = int(downloads.replace(" downloads", "")) #> 830
   # book = {"title": title, "author": author, "downloads": downloads_count}
    #print(book)
    #books.append(book)

#print(books[2]["title"]) #> Macbeth






