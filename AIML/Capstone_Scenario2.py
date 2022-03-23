#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import sklearn
from sklearn.decomposition import TruncatedSVD


# In[61]:


ros_ratings = pd.read_csv('C:/Users/41782/Desktop/IIIT PG/ROS IIIT/Preprocessed_Inventory_Data.csv')
ros_ratings = ros_ratings.dropna()
ros_ratings.head()


# #### Utility Matrix based on products sold and user reviews
# **Utility Matrix : **An utlity matrix consists of all possible user-item preferences (ratings) details represented as a matrix. The utility matrix is sparse as none of the users would buy all the items in the list, hence, most of the values are unknown.

# In[21]:


# Subset of ROS Ratings

ros_ratings = ros_ratings.head(10000)
len(ros_ratings.index)


# In[23]:


ros_ratings['userid'] = range(1, len(ros_ratings.index)+1)
ratings_utility_matrix = ros_ratings.pivot_table(values='Rating', index='userid', columns='Product ID', fill_value=0)
ratings_utility_matrix.head()


# In[17]:


ratings_utility_matrix.shape


# In[18]:


#Transposing the matrix
X = ratings_utility_matrix.T
X.head()


# Unique products in subset of data

# In[26]:


X.shape


# In[ ]:


X1 = X


# ### Decomposing the Matrix

# In[63]:


# Fetch 10 matching products and tranform
SVD = TruncatedSVD(n_components=100)
decomposed_matrix = SVD.fit_transform(X)
decomposed_matrix.shape


# In[65]:


decomposed_matrix


# ### Correlation Matrix

# In[64]:


correlation_matrix = np.corrcoef(decomposed_matrix)
#correlation_matrix.shape


# ### Isolating Product ID # 202212001 from the Correlation Matrix.
# Assuming the customer buys Product ID # 202212100 (randomly chosen)

# In[55]:


index = 175
i = 202212001
product_id = list(X.index)
product_id[0]


# In[56]:


correlation_product_ID = correlation_matrix[index]
correlation_product_ID.shape


# In[57]:


Recommend = list(X.index[correlation_product_ID > 0.90])

# Removes the item already bought by the customer
#Recommend.remove(i) 

Recommend

