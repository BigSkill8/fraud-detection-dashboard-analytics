#!/usr/bin/env python
# coding: utf-8

# **Importing the necessary libraries and loading the dataset**
# 

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# 
# * **Pandas Library for Data Cleaning**
# * **Importing the Raw Data in data frame name *df* from the folder name *data* by using pandas library**

# In[ ]:


df=pd.read_csv('data/raw_data.csv')
df.head()


# **Checking Data to see it's content, number of observations, or features**

# In[ ]:


print("Dataset loaded successfully!")
df.shape
df.info()
print(df.head())


# End of importing the csv file data
