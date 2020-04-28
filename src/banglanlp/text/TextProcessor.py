"""
    author(s) : Bihan Sen
    email(s) : senbihan@gmail.com
    date : 28/04/2020
"""

from abc import ABCMeta, abstractmethod
import re, string

class TextProcessor(object):
    """
    This is a generic class for cleaning and preprocessing text
    Inherit this class for your custom processor
    """

    def __init__(self, punc=string.punctuation):
        self.puncstr = punc
    
    @abstractmethod
    def process(self, text):
        pass


    def remove_punctuation(self, text):
        return text.translate(text.maketrans('', '', self.puncstr))




class EnglishWordProcessor(TextProcessor):
    """ Word Processor for English text"""
    
    def __init__(self):
        super().__init__()

    def process(self, text):
        text = super().remove_punctuation(text)
        text = remove_extra_space(text)
        text = to_lower(text)
        return text



BAD_SYMBOL = '—৷”…॥' # TODO: move to unicodebased removal

class BanglaWordProcessor(TextProcessor):
    """ Word Processor for Bangla text"""
    
    def __init__(self):
        super().__init__(BAD_SYMBOL)

    def process(self, text):
        text = super().remove_punctuation(text)
        text = remove_extra_space(text)
        return text



# Utility functions 

def remove_extra_space(text):
    return re.sub('\s+','\s',text).strip()

def to_lower(text):
    """
    Custom to lower method that should not lowercase abbreviations
    """
    return text if text.isupper() else text.lower()