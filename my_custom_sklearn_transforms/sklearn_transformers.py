from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
    
class FillNa(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        target0 = data[data['TARGET']==0]
        target1 = data[data['TARGET']==1]
        target2 = data[data['TARGET']==2]
        target0['koi_pdisposition']=target0['koi_pdisposition'].fillna('CANDIDATE')
        target1['koi_pdisposition']=target1['koi_pdisposition'].fillna('FALSE POSITIVE')
        target2['koi_pdisposition']=target2['koi_pdisposition'].fillna('CANDIDATE')
        
        data0 = pd.concat([target0, target1, target2])
        
        cols = ['koi_score', 'koi_fpflag_nt', 'koi_fpflag_ss',
       'koi_fpflag_co', 'koi_fpflag_ec', 'koi_period', 'koi_period_err1',
       'koi_period_err2', 'koi_time0bk', 'koi_time0bk_err1',
       'koi_time0bk_err2', 'koi_impact', 'koi_impact_err1', 'koi_impact_err2',
       'koi_duration', 'koi_duration_err1', 'koi_duration_err2', 'koi_depth',
       'koi_depth_err1', 'koi_depth_err2', 'koi_prad', 'koi_prad_err1',
       'koi_prad_err2', 'koi_teq', 'koi_insol', 'koi_insol_err1',
       'koi_insol_err2', 'koi_model_snr', 'koi_tce_plnt_num', 'koi_steff',
       'koi_steff_err1', 'koi_steff_err2', 'koi_slogg', 'koi_slogg_err1',
       'koi_slogg_err2', 'koi_srad', 'koi_srad_err1', 'koi_srad_err2', 'ra',
       'dec', 'koi_kepmag']
        
        data0[cols]=data0[cols].fillna(data0.mean().iloc[0])
        
        return data0
    
class CathegoricalData(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        
        data = pd.get_dummies(data, columns=['koi_pdisposition'])
        
        return data