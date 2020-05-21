from . Tokenizer import Tokenizer

class VocabularyBuilder():
    '''
    This class builds a vocabulary with the tokenizer provided
    '''
    
    def __init__(self, tokenizer):
        # Don't use 0 as it can be used as a default value in vector for length normalization
        self.tokenToIndex = {'<S>':1, '<E>': 2, '<U>' : 3}
        self.indexToToken = {1 : '<S>', 2 : '<E>', 3 : '<U>'}
        self.__index__  = 4
        
        if not isinstance(tokenizer, Tokenizer):
            raise AttributeError("input param tokenizer is not a Tokenizer instance")
        
        self.tokenizer = tokenizer

    def add_to_vocab(self, tokenlist):
        '''
        Adds a list of tokens into the vocabulary
        '''
        for token in tokenlist:
            if token not in self.tokenToIndex:
                self.tokenToIndex[token] = self.__index__ 
                self.indexToToken[self.__index__] = token
                self.__index__ += 1
    
    def build_vocab(self, series):
        '''
        Build a vocabulary with series as input
        '''
        
        if self.tokenizer is None:
            raise AttributeError("Tokenizer is not set.")
            
        for word in series.values:
            self.add_to_vocab(self.tokenizer.tokenize(word))
    
    def get_len(self):
        return self.__index__
    
    def text_to_vector(self, text):
        vec = [self.tokenToIndex['<S>']]
        tokens = self.tokenizer.tokenize(text)
        for token in tokens:
            if token in self.tokenToIndex:
                vec.append(self.tokenToIndex[token])
            else:
                vec.append(self.tokenToIndex['<U>'])
        vec.append(self.tokenToIndex['<E>'])
        return vec
    
    def vector_to_tokens(self, vector):
        tokens = []
        for elem in vector:
            tokens.append(self.indexToToken[elem])
        return tokens