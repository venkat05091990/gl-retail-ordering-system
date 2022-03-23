#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from pandas import read_csv
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

get_ipython().system('pip install rake-nltk')
from rake_nltk import Rake


# In[4]:


df=read_csv("22_3_2022__0_0_31_Grocery, Fruits and Dry Fruits.csv",sep=",")


# In[5]:


df.head()


# In[9]:


df.columns = df.columns.str.strip()
df['productid'] = df['productid'].astype(int)


# In[10]:


df1 = df[['productid','Product_Name','Brand','Category_Name','Sub_Category_Name','Product_Rating']].copy()
df1.head()


# In[12]:


df1['keywords'] = ""
lst = []

for index,row in df1.iterrows():
    prodname = row['Product_Name']

    r = Rake()
    r.extract_keywords_from_text(prodname)

    key_words_dict_scores = r.get_word_degrees()   
    lst.append(list(key_words_dict_scores.keys()))
df1['keywords'] = lst


# In[13]:


df1.head()


# In[14]:


df1.set_index('productid', inplace = True)
df1.head()


# In[15]:


df1['text'] = ''
columns = ['Brand','Category_Name','Sub_Category_Name']
lst = []
for index, row in df1.iterrows():
    words = ''
    for col in columns:
        words = words + ' ' + row[col] + ' '
    print(words)
    lst.append(words)
df1['text'] = lst


# In[16]:


columns = ['text','keywords']
lst = []
for index, row in df1.iterrows():
    words = ''
    for col in columns:
        words = words + ' '.join(row[col]) + ' '
    print(words)
    lst.append(words)
df1['bag_of_words'] = lst


# In[17]:


df1['bag_of_words'].head()


# In[18]:


df1.drop(['Brand','Category_Name','Sub_Category_Name','Product_Name','text','keywords'], axis = 1, inplace = True)


# In[19]:


df1.head()


# In[20]:


count = CountVectorizer()
count_matrix = count.fit_transform(df1['bag_of_words'])
count_matrix


# In[26]:


indices = pd.Series(df1.index)
indices[:5]


# In[27]:


cosine_sim = cosine_similarity(count_matrix, count_matrix)
cosine_sim


# In[28]:


cosine_sim.shape


# In[29]:


def recommendations(Product_ID, cosine_sim = cosine_sim):
    recommended_prods = []
    
    idx = indices[indices == Product_ID].index[0]
    
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    
    top20_indexes = list(score_series.iloc[1:21].index)
    
    for i in top20_indexes:
        recommended_prods.append(list(indices)[i])
    return recommended_prods


# In[30]:


recommended_prods = recommendations(202212732)


# In[32]:


for index,row in df.iterrows():
    for i in recommended_prods:
        if row['productid'] == i:
            print(row['Product_Name'])


# In[33]:


import pickle

filename = 'cosine_sim.sav' #model_dumpfile_name
pickle.dump(cosine_sim, open(filename, 'wb')) #name of model and variable


# In[34]:


loaded_cosine = pickle.load(open("cosine_sim.sav", 'rb'))


# In[35]:


loaded_cosine


# In[36]:


pickle.dump(indices, open("indices.sav", 'wb')) #name of model and variable


# In[37]:


loaded_indices = pickle.load(open("indices.sav", 'rb'))


# In[38]:


loaded_indices


# In[ ]:




