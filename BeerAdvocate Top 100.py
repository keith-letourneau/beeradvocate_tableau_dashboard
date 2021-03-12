#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import urllib.request


# In[2]:


#parse top beer webpage
new_url = 'https://www.beeradvocate.com/beer/top-rated/'
req = requests.get(new_url)
soup = BeautifulSoup(req.text, 'lxml')

soup_a = []
soup_b = []

#get anchor text for beer and brewery name
for link in soup.find_all('a'):
    soup_a.append(link.text.strip())

beer = soup_a[118:]
beer_name = beer[::3]
beer_name = beer_name[:100]

brewery = soup_a[119:]
brewery_name = brewery[::3]
brewery_name = brewery_name[:100]


# In[5]:


#get bold txt for ratings and reviews
for rating in soup.find_all('b'):
    soup_b.append(rating.text.strip())
    
rate = soup_b[4:]
ratings = rate[::3]
ratings = ratings[:100]

review = soup_b[3:]
reviews = review[::3]
reviews = reviews[:100]

#create dataframe
df = pd.DataFrame(beer_name, index=range(1,101), columns=['Beer Name'])
df['Brewery Name'] = brewery_name
df['Rating'] = ratings
df['Rating'] = pd.to_numeric(df['Rating'])
df['Number of Reviews'] = reviews
df['Number of Reviews'] = pd.to_numeric(df['Number of Reviews'])
df.tail()


# In[ ]:


#export dataframe to csv
df.to_csv(r'C:\Users\keith\Downloads\BeerAdvocate_Top100.csv', index = True) 


# In[12]:


#visualize some of the data
sns.set_style('darkgrid')
plt.figure(dpi=1200)
sns.histplot(df['Rating'], bins=10, color="red", kde=True)
plt.xticks(fontsize=9, rotation=90)
plt.title('BeerAdvocate Top 100 Ratings Range')
plt.show()

