#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

import sklearn
from sklearn.decomposition import TruncatedSVD


# In[3]:


ros_ratings = pd.read_csv('C:/Users/41782/Desktop/IIIT PG/ROS IIIT/Preprocessed_Inventory_Data.csv')
ros_ratings = ros_ratings.dropna()
ros_ratings.head()


# # The below code gives us the most popular products (arranged in descending order) on the basis of average rating.

# In[6]:


popular_products = ros_ratings.groupby('Product ID', as_index=False)['Rating'].mean()
most_popular = popular_products.sort_values('Rating', ascending=False)
most_popular.head(10)


# In[ ]:




