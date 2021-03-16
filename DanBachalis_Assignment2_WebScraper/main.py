import pandas as pd
import requests
from bs4 import BeautifulSoup

# Set the URL
url = "http://18.206.38.144:8000/random_company"

# Create empty companies dataframe and Names and Purposes lists for appending scraped data
companies = pd.DataFrame(columns = ['Company', 'Purpose'])
nameList = []
purposeList = []

a = 0 # counter

# Scrape the URL 50 times for company names and purposes
while a < 50:
    a += 1

    # Use get request to get a response from the URL
    response = requests.get(url)

    # Initialize the response in a working document
    soup = BeautifulSoup(response.content, "html.parser")

    # Obtain the Name and Purpose of the company from the body of the webscraped URL
    for string in soup.body.strings:
        if (string.find('Name: ') != -1):
           nameList.append(string[6:])
        elif (string.find('Purpose: ') != -1):
            purposeList.append(string[9:])

# Append names and purposes to companies dataframe
companies['Company'] = nameList
companies['Purpose'] = purposeList

# Write the companies dataframe to an Excel file
companies.to_excel("D:\Dan\Stevens\Fin Tech\Companies.xlsx", index = False)
