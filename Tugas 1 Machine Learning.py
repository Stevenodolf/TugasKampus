#!/usr/bin/env python
# coding: utf-8

# # 1

# 1. Unsupervised Learning : Clustering, karena data yang ada tidak membuahkan hasil sesuatu dan di soal kita mau menentukan max min value.

# # 2

# In[2]:


import pandas as pd
airData = pd.read_csv("listings.csv")
print(airData.head())


# In[3]:


maxValue = airData.max()
print(maxValue)
minValue = airData.min()
print(minValue)


# In[5]:


print(airData.isna())


# In[9]:


newAirDrop = airData.dropna()
print(newAirDrop.isna().values.any())
print(len(newAirFill))


# In[8]:


newAirFill = airData.fillna(0)
print(newAirFill.isna().values.any())
print(len(newAirFill))


# In[ ]:




