#!/usr/bin/env python
# coding: utf-8

# **Importing the necessary Libraries**

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# **Load Dataset** 

# In[ ]:


df=pd.read_csv('raw_data.csv')


# **Removing Missing Values**

# In[ ]:


#Check missing values
print("Missing values before cleaning:")
print(df.isnull().sum())


# In[ ]:


#Remove duplicates
df.drop_duplicates(inplace=True)


# In[ ]:


#remove rows with missing values
df.dropna(inplace=True)


# In[ ]:


df.info()
df.head(10)


# **Saving the Processed Data to csv *data folder***

# In[ ]:


df.to_csv('cleaned_data.csv', index=False)
print("Processed data saved successfully!")


# saved in a file name cleaned_data.csv file
