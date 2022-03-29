from fastapi import FastAPI
import pickle

import pandas as pd


app = FastAPI()

from pydantic import BaseModel

class request_body(BaseModel):
    product_id : str

@app.get("/")
def first_example():
    """
       GFG Example First Fast API Example 
    """
    return {"GFG Example": "FastAPI"}

@app.post('/predict')
def predict(data : request_body):
    def recommendations(Product_ID, indices, cosine_sim):
        recommended_prods = []
    
        idx = indices[indices == Product_ID].index[0]
    
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    
        top20_indexes = list(score_series.iloc[1:21].index)
    
        for i in top20_indexes:
            recommended_prods.append(list(indices)[i])
        
        return recommended_prods
    
    test_data = data.product_id
    filename_cossine="cosine_sim.sav"
    filename_index="indices.sav"

    loaded_indices = pickle.load(open(filename_index, 'rb'))
    loaded_cossine = pickle.load(open(filename_cossine, 'rb'))

    lst_recmd = recommendations(int(test_data), loaded_indices, loaded_cossine)

    #lst_recmd=[test_data]
    dict_out={"Product_ids":lst_recmd}
    return dict_out

class request_body_user(BaseModel):
    userid : str

@app.post('/predictuser')
def predictuser(data: request_body_user):
    def similarUsers(user_id, correlation_matrix, user_indices):
        recommended_users = []

        idx = user_indices[user_indices == user_id].index[0]
        score_series = pd.Series(correlation_matrix[idx]).sort_values(ascending=False)
        top20_indexes = list(score_series.iloc[1:21].index)
        for i in top20_indexes:
            recommended_users.append(list(user_indices)[i])
        return recommended_users

    def userRecommendations(sorted_ratings):
        recommended_prods = []
        len_rating = len(sorted_ratings)
        if (len_rating > 0 and len_rating < 21):
            recommended_prods = sorted_ratings['productid'][1:len_rating]
        if (len_rating > 20):
            recommended_prods = sorted_ratings['productid'][1:20]
        return list(recommended_prods)

    user_data = data.userid
    filename_corr = "corr_matrix.sav"
    filename_index_user = "user_indices.sav"
    filename_df = "df.sav"

    loaded_indices_user = pickle.load(open(filename_index_user, 'rb'))
    loaded_corr = pickle.load(open(filename_corr, 'rb'))
    loaded_df = pickle.load(open(filename_df, 'rb'))

    similar_users = similarUsers(int(user_data), loaded_corr, loaded_indices_user)
    simusers = pd.DataFrame(similar_users, columns=['userid'])

    sorted_ratings = pd.merge(simusers, loaded_df, on=['userid']).sort_values('rating', ascending=False)
    sorted_ratings['productid'] = sorted_ratings['productid'].astype(int)
    sorted_ratings = sorted_ratings.groupby('productid', as_index=False)['rating'].mean()
    sorted_ratings = sorted_ratings[sorted_ratings['rating'] > 2]

    lst_recmd = userRecommendations(sorted_ratings)

    dict_products = {"Product_ids": lst_recmd}
    return dict_products
