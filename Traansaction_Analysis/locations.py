#!/usr/bin/env python
# coding: utf-8

# **Location Analysis (Fraud Detection by Location)**
# 
# If your dataset contains a Location column (e.g., country, city, ATM ID, merchant region), you can analyze suspicious geographic patterns.
# 
# Since my current dataset (the Kaggle credit card dataset) does NOT have a location column, I need a simulated banking dataset

# Importing Necessary labraries

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt  
import numpy as np
import  plotly.express as px


# Import Dataset

# In[ ]:


df2 = pd.read_csv('cleaned_data.csv')
df2.head()


# Creating Simulated Countrys

# In[ ]:


# Create a list of simulated countries
locations = [
    "USA", "UK", "Canada", "Germany", "France",
    "Nigeria", "India", "Brazil", "China", "Japan"
]

# Randomly assign location to each transaction
np.random.seed(42)  # for reproducibility
df2["Location"] = np.random.choice(locations, size=len(df2))

print(df2[["Location"]].head())


# Displyaing Updated simulated dataset

# In[ ]:


df2.head()


# Location fraud

# In[ ]:


location_fraud = df2.groupby("Location")["Class"].mean()

print("Fraud Rate by Location:")
print(location_fraud)


# Transcation Fraud Distribution By Location(Bar Chart)

# In[ ]:


df2["Location"].value_counts().plot(kind="bar")
plt.title("Transaction Distribution by Location")
plt.xlabel("Location")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.show()


# Globe description of Fraud transaction across stimulated locations

# In[ ]:


# Simulated locations
locations = {
    "USA": (37.0902, -95.7129),
    "UK": (55.3781, -3.4360),
    "Canada": (56.1304, -106.3468),
    "Germany": (51.1657, 10.4515),
    "France": (46.2276, 2.2137),
    "Nigeria": (9.0820, 8.6753),
    "India": (20.5937, 78.9629),
    "Brazil": (-14.2350, -51.9253),
    "China": (35.8617, 104.1954),
    "Japan": (36.2048, 138.2529)
}

# Assign random locations
np.random.seed(42)
df2["Location"] = np.random.choice(list(locations.keys()), size=len(df2))

# Map coordinates
df2["Latitude"] = df2["Location"].map(lambda x: locations[x][0])
df2["Longitude"] = df2["Location"].map(lambda x: locations[x][1])

# Step 2 — Create Globe Scatter Plot
fig = px.scatter_geo(
    df2 ,
    lat="Latitude",
    lon="Longitude",
    color="Class",  # Fraud or Normal
    hover_name="Location",
    hover_data=["Amount", "Class"],
    projection="orthographic",  # makes it a globe
    title="Global Transaction Distribution (Hover for Details)"
)

fig.update_layout(
    geo=dict(showland=True, showocean=True),
)

fig.show()


# In[ ]:





# In[ ]:




