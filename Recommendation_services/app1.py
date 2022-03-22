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
