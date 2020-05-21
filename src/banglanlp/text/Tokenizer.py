from abc import ABCMeta, abstractmethod
import re

vowels = 'aeiou'
semivowels = 'wy'

class Tokenizer():
    
    def __init__(self):
        pass
    
    @abstractmethod
    def tokenize(self, word):
        tokens = []
        for char in word:
            tokens.append(char)
        return tokens

class BanglaCharTokenizer(Tokenizer):
    
    def __init__(self):
        super().__init__()
    
    def tokenize(self, word):
        return super().tokenize(word)
    
class EnglishCharTokenizer(Tokenizer):
    
    def __init__(self):
        super().__init__()
    
    def tokenize(self, word):
        return super().tokenize(word)
    
class EnglishBanglaCharTokenizer(Tokenizer):
    
    def __init__(self):
        super().__init__()
    
    def tokenize(self, word):
        tokens = []
        current_token = ''
        for char in word:
            if char is 'h' and (current_token != '' and current_token[-1] not in vowels and current_token[-1] not in semivowels):
                tokens.append(current_token + 'h')
                current_token = ''
            else:
                if current_token != '':
                    tokens.append(current_token)
                current_token = char
                
        if current_token != '':
            tokens.append(current_token)
                
        return tokens