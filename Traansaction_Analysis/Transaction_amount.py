#!/usr/bin/env python
# coding: utf-8

# **Transaction Amount Analysis**

# Importing necessary libraries

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px


# load datasets

# In[ ]:


df1 = pd.read_csv('cleaned_data.csv')

df1.head()


# Transaction Time Behavior Analysis
# 
# Time-based behavior helps detect fraud when transactions happen too quickly/at unusual times.

# Step 1: Convert Time to Hours
# 
# This makes analysis easier.

# In[ ]:


df1["Hour"] = (df1["Time"] / 3600) % 24

print(df1[["Time", "Hour"]].head())


# Step 2: Transactions Per Hour (lim=20)

# In[ ]:


hourly_tx = df1.groupby("Hour").size().head(20)  # limit to 20 entries

hourly_tx.plot(kind="bar")
plt.title("Transactions per Hour (Limited to 20)")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Transactions")
plt.show()


# Step 3 — Fraud Occurrence by Hour (lim=20)

# In[ ]:


fraud_hourly = df1[df1["Class"] == 1].groupby("Hour").size().head(20)  # limit to 20 entries

fraud_hourly.plot(kind="bar")
plt.title("Fraud Transactions by Hour")
plt.xlabel("Hour")
plt.ylabel("Fraud Count")
plt.show()


# End

# 
