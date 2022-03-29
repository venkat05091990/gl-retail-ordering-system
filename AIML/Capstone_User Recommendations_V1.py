#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

import sklearn
from sklearn.decomposition import TruncatedSVD


# In[3]:


ros_ratings = pd.read_csv('Customer Ratings DataSet.csv')
ros_ratings = ros_ratings.dropna()
ros_ratings.head(10)


# In[4]:


ros_ratings.shape


# #### Utility Matrix based on products sold and user reviews
# **Utility Matrix : **An utlity matrix consists of all possible user-item preferences (ratings) details represented as a matrix. The utility matrix is sparse as none of the users would buy all the items in the list, hence, most of the values are unknown.

# In[5]:


ratings_utility_matrix = ros_ratings.pivot_table(values='rating', index='userid', columns='productid', fill_value=0)
ratings_utility_matrix.head()


# In[6]:


ratings_utility_matrix.shape


# Unique products in subset of data

# ### Decomposing the Matrix

# In[7]:


# Reduce the dimention to 100 products and tranform
SVD = TruncatedSVD(n_components=100)
decomposed_matrix = SVD.fit_transform(ratings_utility_matrix)
decomposed_matrix.shape
decomposed_matrix


# In[8]:


decomposed_matrix.shape


# ### Correlation Matrix

# In[9]:


correlation_matrix = np.corrcoef(decomposed_matrix)
correlation_matrix.shape


# In[10]:


correlation_matrix


# In[11]:


user_indices = pd.Series(ratings_utility_matrix.index)
user_indices[:5]


# In[12]:


import pickle

filename = 'user_indices.sav' #model_dumpfile_name
pickle.dump(user_indices, open(filename, 'wb')) #name of model and variable


# In[13]:


loaded_indices = pickle.load(open("user_indices.sav", 'rb'))


# In[63]:


loaded_indices


# In[56]:


filename = 'corr_matrix.sav' #model_dumpfile_name
pickle.dump(correlation_matrix, open(filename, 'wb')) #name of model and variable


# In[57]:


loaded_corr_matrix = pickle.load(open("corr_matrix.sav", 'rb'))


# In[58]:


loaded_corr_matrix


# In[59]:


filename = 'df.sav' #model_dumpfile_name
pickle.dump(ros_ratings, open(filename, 'wb')) #name of model and variable


# In[60]:


loaded_df = pickle.load(open("df.sav", 'rb'))
loaded_df


# In[14]:


def similarUsers(user_id, correlation_matrix = correlation_matrix):
    recommended_users = []
    
    idx = user_indices[user_indices == user_id].index[0]

    score_series = pd.Series(correlation_matrix[idx]).sort_values(ascending = False)
    print(score_series)
    
    top20_indexes = list(score_series.iloc[1:21].index)
    
    for i in top20_indexes:
        recommended_users.append(list(user_indices)[i])
    return recommended_users


# In[15]:


similar_users = similarUsers(10002)


# In[16]:


simusers = pd.DataFrame(similar_users, columns = ['userid'])


# In[17]:


ros_ratings


# In[18]:


sorted_ratings = pd.merge(simusers, ros_ratings, on=['userid']).sort_values('rating', ascending =False)
sorted_ratings.shape


# In[19]:


#sorted_ratings = sorted_ratings.drop(sorted_ratings[(sorted_ratings['rating'] == 0.0)].index)
#sorted_ratings = sorted_ratings.dropna()
sorted_ratings['productid'] = sorted_ratings['productid'].astype(int)


# In[20]:


sorted_ratings = sorted_ratings.groupby('productid', as_index=False)['rating'].mean()


# In[21]:


sorted_ratings = sorted_ratings[sorted_ratings['rating']>3]
sorted_ratings


# In[22]:


def recommendations(sorted_ratings):
    recommended_prods = []
    len_rating = len(sorted_ratings)
    if(len_rating>0 and len_rating<21):       
        recommended_prods = list(sorted_ratings['productid'][1:len_rating])
    if(len_rating>20):
        recommended_prods = list(sorted_ratings['productid'][1:20])
    return recommended_prods


# In[23]:


output = recommendations(sorted_ratings)
output


# In[ ]:




