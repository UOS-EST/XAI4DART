#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import os
sys.path.append('../')

import joblib
import numpy as np
import pandas as pd

from tqdm import tqdm

from utils.smiles2fing import Smiles2Fing
from sklearn.cross_decomposition import PLSRegression


pred_df_tmp = pd.read_excel('/application_EPAA/app_data.xlsx') 

na_idx1 = pred_df_tmp[pred_df_tmp.SMILES.isna()].index
na_idx2 = pred_df_tmp[pred_df_tmp.SMILES.isin([' '])].index
pred_df = pred_df_tmp.drop(na_idx1.append(na_idx2)).reset_index(drop=True)



# In[ ]:


#application function
def prediction(model, fingerprint_type):
    na_idx, x = Smiles2Fing(pred_df.SMILES, fingerprint_type=fingerprint_type)
    model_path = f'data/ATG_PPARa_TRANS/best_model_{fingerprint_type}_{model}.joblib'

    if not os.path.exists(model_path):
        print(f"Model file {model_path} does not exist!")
        return None

    with open(model_path, 'rb') as file:
        clf = joblib.load(file)

    if isinstance(clf, PLSRegression):
        pred = np.argmax(clf.predict(x), axis=1)
    else:
        pred = clf.predict(x)

    df_ = pd.concat([pred_df.drop(na_idx).reset_index(drop=True),
                     pd.DataFrame({'pred': pred})], axis=1)
    return df_

# main function
if __name__ == '__main__':
    models = ['gbt']  
    fingerprint_type = 'Morgan'  

    for m in tqdm(models):
        try:
            result = prediction(m, fingerprint_type)
            if result is not None:
                tmp = pd.merge(pred_df_tmp, result[['CasRN', 'pred']], how='left', on='CasRN')
                tmp.to_excel(f'data/ATG_PPARa_TRANS/app_result_{fingerprint_type}_{m}.xlsx', header=True, index=False) 
        except Exception as e:
            print(f"Error with model {m}: {e}")


# In[ ]:




