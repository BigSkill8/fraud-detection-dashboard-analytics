#!/usr/bin/env python
# coding: utf-8

# **Transaction frequency Analysis**

# **Importing Libraries**

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# load dataset

# In[ ]:


df1 = pd.read_csv('cleaned_data.csv')

df1.head()


# Transaction frequency measures how often transactions occur in a given time period.
# 
# In fraud detection:
# Many transactions in a short time → suspicious

# Step 1: Transaction Frequency

# In[ ]:


df1 = pd.read_csv('cleaned_data.csv')

# Count transactions occurring at same time
df1["TransactionFrequency"] = df1.groupby("Time")["Time"].transform("count")

print(df1[["Time", "TransactionFrequency"]].head())


# Step 2: Fraud Trigger
# 
# Flag suspicious frequency:

# In[ ]:


df1["HighFrequency"] = df1["TransactionFrequency"] > 5


# Step 3: Visualize Frequency

# In[ ]:


df1["TransactionFrequency"].hist(bins=30)
plt.title("Transaction Frequency Distribution")
plt.xlabel("Number of Transactions at Same Time")
plt.ylabel("Count of Transactions")
plt.show()


# * Step 4: Customer / Account Risk Scoring
# 
# Risk scoring ranks customers or transactions by how suspicious they are.

# In[ ]:


# Start risk score
df1["RiskScore"] = 0

# Large transaction
df1.loc[df1["Amount"] > 2000, "RiskScore"] += 2

# Very large transaction
df1.loc[df1["Amount"] > 5000, "RiskScore"] += 3

# High transaction frequency
df1["TransactionFrequency"] = df1.groupby("Time")["Time"].transform("count")
df1.loc[df1["TransactionFrequency"] > 5, "RiskScore"] += 2

# Known fraud label (if exists)
if "Class" in df1.columns:
    df1.loc[df1["Class"] == 1, "RiskScore"] += 5

print(df1[["Amount", "TransactionFrequency", "RiskScore"]].head())


# **Transaction Amount Analysis**
# 
# Step 1:Transaction amount analysis helps identify unusual spending patterns, which are common in fraud cases.

# In[ ]:


print("Transaction Amount Statistics:")
print(df1["Amount"].describe())


# Step 2: Amount Distribution Chart

# In[ ]:


plt.hist(df1["Amount"], bins=50)
plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Amount of Transactions")
plt.show()


# Step 3: Fraud vs Normal Amount Comparison

# In[ ]:


fraud = df1[df1["Class"] == 1]
normal = df1[df1["Class"] == 0]

print("Average Fraud Amount:", fraud["Amount"].mean())


# Step 4: Detect Large Transactions

# In[ ]:


df1["LargeTransaction"] = df1["Amount"] > 2000


# Step 5: Amount Anomaly Detection

# In[ ]:


mean_amt = df1["Amount"].mean()
std_amt = df1["Amount"].std()

threshold = mean_amt + 3 * std_amt
df1["AmountAnomaly"] = df1["Amount"] > threshold


# End 

# 
