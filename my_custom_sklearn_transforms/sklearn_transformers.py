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
    
class AdjustMeanSubject(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        data['NOTA_GO'] = data.apply(
            lambda row: ((row['NOTA_MF']+row['NOTA_EM']+row['NOTA_DE'])/3) if np.isnan(row['NOTA_GO']) else row['NOTA_GO'],axis=1
        )
        
        return data

class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        df = X.copy()
        df['REPROVACOES_H'] = df['REPROVACOES_DE'] + df['REPROVACOES_EM']
        df['REPROVACOES_E'] = df['REPROVACOES_MF'] + df['REPROVACOES_GO']
        df['MEDIA_H'] = (df['NOTA_DE']+df['NOTA_EM'])/2
        df['MEDIA_E'] = (df['NOTA_MF']+df['NOTA_GO'])/2

        return df
