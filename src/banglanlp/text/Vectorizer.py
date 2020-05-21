import pandas as pd
import numpy as np

class Vectorizer():
    
    #TODO : MAX_LEN as a parameter
    def __init__(self, vocab_builder):
        self.vocab = vocab_builder
        self.max_len = 0
    
    def fit_transform(self, data):
        return self.__vectorize(data)
    
    def transform(self, data):
        return self.__vectorize(data, False)
    
    def __vectorize(self, data, calculate_length=True):
        
        if type(data) == str:
            return np.array(self.vocab.text_to_vector(data), dtype=np.int32)
        
        if type(data) == pd.core.series.Series:
            vecs = np.array(data.apply(self.vocab.text_to_vector))
            if calculate_length:
                self.max_len = get_max_len(vecs)
            vec = np.zeros((data.shape[0],self.max_len), dtype=np.int32)
            for i in range(data.shape[0]):
                vec[i,0:len(vecs[i])] = vecs[i]
            
            return vec

    
# add to utils
def get_max_len(vectors):
    '''vectors is a np array/list of list'''
    max_len = 0
    for v in vectors:
        max_len = max(len(v), max_len)
    return max_len