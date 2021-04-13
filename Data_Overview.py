#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import random 
import matplotlib.pyplot as plt


# In[4]:


j = __import__('json').loads(open('yelp_academic_dataset_review.json', 'r', encoding='utf-8').read())


# In[3]:


df = pd.read_json("yelp_academic_dataset_review.json")


# In[ ]:


len(df)


# In[ ]:


df_sample_1 = df.sample(frac = 0.1)


# In[ ]:


# yelp = df_sample_10[["review_id", "stars", "date", "text", "useful"]]
yelp = df_sample_10[["stars", "text", "useful"]]
yelp


# In[ ]:


useful_review = yelp[yelp["useful"] >= 10]
len(useful_review)


# In[ ]:


useful_review


# In[ ]:


grouped = yelp.groupby(by = "stars").size()
grouped


# ## Save as a zip file that contains out.csv

# In[ ]:


compression_opts = dict(method='zip', archive_name='out.csv')  

df.to_csv('out.zip', index=False, compression=compression_opts)


# ## Convert notebook to py file

# In[ ]:


get_ipython().system('jupyter nbconvert --to script Data_Overview.ipynb')

