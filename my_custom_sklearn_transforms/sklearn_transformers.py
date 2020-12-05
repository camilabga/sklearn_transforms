from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

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
        
        return data0
    
    