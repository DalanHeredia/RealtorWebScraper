############################
# Author: Dalan Heredia
# Feb 07 2023
############################

############################
# VIEW THE README
############################

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# insert city name, use a '-' for spaces.
city_name = input("Please Enter Your City Name. Use '-' for spaces. \n")

# Insert state abbreviation
state = input("Please Enter Your State abbreviation. \n")

# CHANGE WEBDRIVER PATH TO YOUR LOCAL WEBDRIVER YOU INSTALLED
driver = webdriver.Chrome('')

# Get 1st Page

driver.get('https://www.realtor.com/realestateagents/' + city_name + '_' + state + '/')

# Create Arrays
results = []
phone_results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

# Find Names
for a in soup.findAll(attrs='mobile-agent-card-wrapper'):
    name = a.find("a")
    if name not in results:
        results.append(name.text)

# Find Phone Numbers
for link in soup.find_all('a', {"class": "btn-contact-me-call"}):
    phone_results.append(link.get('href'))

pageNumber = 2

while pageNumber <= 29:
    # Get 2nd Page
    driver.get('https://www.realtor.com/realestateagents/' + city_name + '_' + state + '/pg-' + str(pageNumber))
    # Find Names
    for a in soup.findAll(attrs='mobile-agent-card-wrapper'):
        name = a.find("a")
        if name not in results:
            results.append(name.text)

    # Find Phone Numbers
    for link in soup.find_all('a', {"class": "btn-contact-me-call"}):
        phone_results.append(link.get('href'))

    #Iterates through pages
    pageNumber += 1
    #Slows down HTTP Requests to prevent connection refusal
    time.sleep(5)
    #Quits Driver
    driver.quit()

# Debug
print(results)
print(phone_results)

# Create and export to names.csv
df = pd.DataFrame({'Names': results, 'Phone': phone_results})
df.to_csv('names.csv', index=False, encoding='utf-8')

