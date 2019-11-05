#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[9]:


df = pd.read_csv("./Plaza_Coffee.csv",sep = ";")


# In[45]:


df_output = df.groupby(by=["Company","Payment"]).agg({"Quantity": "sum"}).reset_index()


# In[48]:


companies = {"Deloite & Touche": {"Cash": 0, "Credit": 0},
            "EY": {"Cash": 0, "Credit": 0},
            "KPMG": {"Cash": 0, "Credit": 0},
            "PWC": {"Cash": 0, "Credit": 0}}


# In[51]:


for i in range(len(df_output)):
    companyName, payment, quantity = df_output.iloc[i]["Company"], df_output.iloc[i]["Payment"], df_output.iloc[i]["Quantity"]
    companies[companyName][payment] = quantity  


# In[54]:


for key,value in companies.items():
    companyName = key
    cashCount = value["Cash"]
    creditCount = value["Credit"]
    print("From {0} {1} people have bought stuff on discount and paid in cash, also assistants got {2} serving of coffee on credit".format(companyName,cashCount,creditCount))
    


# In[ ]:




