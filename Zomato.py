#!/usr/bin/env python
# coding: utf-8

# # Zomato Data Analysis Project

# # Step 1-Importing Libraries

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Step 2- Create the data frame

# In[12]:


dataframe = pd.read_csv(r"C:\Users\Vaishnavi\Downloads\Zomato data .csv")
print(dataframe)


# In[13]:


dataframe


# # Convert the data type of column-rate

# In[15]:


def handleRate(value):
    value = str(value).split('/')
    value = value[0];
    return float(value)
dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[16]:


dataframe.info


# # Type of restaurant

# In[17]:


dataframe.head()


# In[18]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of restaurant")


# # Conclusion-majority of the restaurant falls in dining category 

# In[19]:


dataframe.head()


# In[26]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type Of Restaurant", c="red", size=30)
plt.ylabel("Votes", c="red", size=20)
plt.title("Votes by Type of Restaurant")  
plt.show()


# # Conclusion-dinning restaurant has received maximum votes

# In[27]:


dataframe.head()


# In[30]:


plt.hist(dataframe['rate'],bins =5)
plt.title("ratings distribution")
plt.show()


# # Conclusion- the majority  restaurant received ratings from 3.4 to 4

# # Average order spending by couples

# In[31]:


dataframe.head()


# In[32]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # Conclusion-the majority of the couples prefer restaurants with an approximate cost of 300 rupees

# # Which mode receives maximum rating

# In[33]:


dataframe.head()


# In[34]:


plt.figure(figsize =(6,6))
sns.boxplot(x = 'online_order',y = 'rate', data = dataframe)


# # Conclusion-offline order received lower rating comparison to online

# In[35]:


dataframe.head()


# In[37]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed in (Type)")
plt.show()


# # Conclusion-dining restaurant primarily accept offline order whereas cafes primarily receive online orders.This suggests that clients prefers order in person at restaurant,but prefer online ordering at cafes
