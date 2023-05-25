# Dependency needed to install file 

!pip install xlrd
!pip install openpyxl

# Import required library

import pandas as pd

# Read data from CSV file

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

# Print first five rows of the dataframe

df.head()

# Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()

# Access to the column Length

x = df[['Length']]
x

# Get the column as a series

x = df['Length']
x

# Get the column as a series

x = df['Length']
x

# Access the value on the first row and the first column

df.iloc[0, 0]

# Access the value on the second row and the first column

df.iloc[1,0]

# Access the value on the first row and the third column

df.iloc[0,2]

# Access the value on the second row and the third column
df.iloc[1,2]

# Access the column using the name

df.loc[0, 'Artist']

# Access the column using the name

df.loc[1, 'Artist']

# Access the column using the name

df.loc[0, 'Released']

# Access the column using the name

df.loc[1, 'Released']

# Slicing the dataframe

df.iloc[0:2, 0:3]

# Slicing the dataframe using name

df.loc[0:2, 'Artist':'Released']