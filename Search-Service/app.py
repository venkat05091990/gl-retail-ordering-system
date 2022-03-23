# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:42:03 2022

@author: Deeplearn
"""

import streamlit as st
import pandas as pd
df = pd.read_csv(r"C:\Users\sudheerkona\Downloads\IIIT_Project\flipkart_data.csv")
s=st.text_input("enter text")
def pred(n,s):
    temp = [x for x in df.name if s in x.lower()]
    #count=0
    #if len(temp)>n:temp=[]
    if temp==[] or len(temp)>n:
       # count=1
        list1 = [x for x in range(len(df.name)) if len(set(s.split()).intersection(set(df.name[x].lower().split())))>0]
        list2 = [len(set(s.split()).intersection(set(df.name[x].lower().split()))) for x in range(len(df.name)) if len(set(s.split()).intersection(set(df.name[x].lower().split())))>0]
        df1 = pd.DataFrame([list1,list2]).T
        df1.columns = ['train_index','match_count']
        subset = df1.sort_values(by=['match_count'],ascending=False).reset_index(drop=True).iloc[0:n]
    
        for k in subset.index:
            temp.append(df.name[k])
    return temp
#    else:
 #       count =2
  #      for t in temp:
   #         st.write(t)

#if st.button("Submit"):
temp = pred(10,s)
for c in temp:
    st.write(c)
 #   st.write(count)
