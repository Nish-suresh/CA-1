import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Demographics_of_India'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
print(soup)
soup.find('table')
soup.find_all('table')[8]
soup.find ('table', class_ = 'wikitable sortable')
table = soup.find_all('table')[8]
print(table)
table_titles = table.find_all('th')
table_titles
population_table_titles = [title.text.strip() for title in table_titles]

print(population_table_titles)
population_table_titles = [title.text.strip() for title in table_titles]

print(population_table_titles)
import pandas as pd 
df = pd.DataFrame (columns = population_table_titles)

df
column_data = table.find_all('tr')
for row in column_data[1:]:
  row_data = row.find_all('td')
  Individual_row_data = [data.text.strip() for data in row_data]
  length = len(df)
  print(Individual_row_data)
