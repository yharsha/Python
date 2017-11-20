print("Starting web scrapping.....!!!")
#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#import the library used to query a website
from urllib.request import urlopen
page =urlopen(wiki)
print("page...............")
print(page)
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup=BeautifulSoup(page)
print("soup................")
# print(soup)
print("soup prettify................")
# print(soup.prettify())
print("soup title................")
all_links=soup.find_all("a")
# for link in all_links:
#      print (link.get("href"))

all_tables=soup.find_all('table')
right_table = soup.find('table',class_='wikitable sortable plainrowheaders')
# print("table")
# print(right_table)

#lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

for row in right_table.find_all("tr"):
    cells=row.find_all('td')
    states=row.find_all('th')#To store second column data
    if len(cells)==6:
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/Ut']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
# df
print("*************************")
print(df)

# from selenium import webdriver
# import time
#
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/usr/bin/chromium"
# driver = webdriver.Chrome(chrome_options=options)
# driver.get('https://en.wikipedia.org/wiki/Andaman_and_Nicobar_Islands')










