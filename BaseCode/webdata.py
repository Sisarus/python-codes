!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
# !pip install requests==2.26.0

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"


soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())


tag_object=soup.title
print("tag object:",tag_object)


print("tag object type:",type(tag_object))

tag_object=soup.h3
tag_object

tag_child =tag_object.b
tag_child

parent_tag=tag_child.parent
parent_tag

tag_object.parent

sibling_1=tag_object.next_sibling
sibling_1

sibling_2=sibling_1.next_sibling
sibling_2

tag_child.attrs

tag_child.get('id')

tag_string=tag_child.string
tag_string


type(tag_string)

unicode_string = str(tag_string)
unicode_string

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, "html.parser")

table_rows=table_bs.find_all('tr')
table_rows

first_row =table_rows[0]
first_row

print(type(first_row))

first_row.td

for i,row in enumerate(table_rows):
    print("row",i,"is",row)


for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

list_input=table_bs .find_all(name=["tr", "td"])
list_input

table_bs.find_all(id="flight")

list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input

table_bs.find_all(href=True)
table_bs.find_all(href=False)

soup.find_all(id="boldest")

table_bs.find_all(string="Florida")


two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"


two_tables_bs= BeautifulSoup(two_tables, 'html.parser')

two_tables_bs.find("table")

two_tables_bs.find("table",class_='pizza')


url = "http://www.ibm.com"

data  = requests.get(url).text 

soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'

for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))

for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))


#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")


#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))

import pandas as pd

#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>

# we can see how many tables were found by checking the length of the tables list
len(tables)

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

print(tables[table_index].prettify())



population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data

pd.read_html(str(tables[5]), flavor='bs4')


population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

population_data_read_html

dataframe_list = pd.read_html(url, flavor='bs4')

len(dataframe_list)

dataframe_list[5]

pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]