#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 6/25/18 

@author: John Sigmon

Last modified: 6/27/18
"""

import os
import sys
import json
import pickle as pkl
import logging.config

logger = logging.getLogger(__name__)
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

class Stemmer():
    
    apply = None
    nlp = None
    stemmer = None
    lemmatizer = None

    def __init__(self, name, stemmer=None, lemmatizer=None):
        self.dispatch_fun = {
            'nltk': self.nltk,
            'spacy': self.spacy
            }
        if name: 
            self.apply = self.dispatch_fun[name]
        self.stemmer = stemmer
        self.lemmatizer = lemmatizer
        
        if name is 'spacy':
            import en_core_web_sm
            self.nlp = en_core_web_sm.load()

    def nltk(self, docs):
        '''
        Runs NLTK stemmer or lemmatizer. Options are porter and snowball
        stemmer, or wordnet lemmatizer.

        :params docs {list[list[str]]}
       
        :returns {list[list[str]]} stems of words or tokens

        '''
        # No default stemmer currently        
        if self.stemmer == 'porter':
            from nltk.stem import PorterStemmer
            stemmer = PorterStemmer()
        if self.stemmer == 'snowball':
            from nltk.stem import SnowballStemmer
            stemmer = SnowballStemmer('english')
        if self.lemmatizer == 'wordnet':
            from nltk.stem import WordNetLemmatizer
            lemmatizer = WordNetLemmatizer()
        
        # Logic works if functionality not expanded. Check if expanded
        if self.stemmer is not None:
            stems = [[stemmer.stem(w) for w in doc] for doc in docs]
        else:
            stems = [[lemmatizer.lemmatize(w) for w in doc] for doc in docs]
        
        logger.debug("Type of return: %s", type(stems))
        logger.debug("Length: %d", len(stems))
        logger.debug("Length of first entry: %d", len(stems[0]))
        return stems        
    
    def spacy(self, docs):
        '''
        
        
        :params docs {list[list[str]]}
       
        :returns {list[list[str]]} stems of words or tokens

        '''
  
        # Slower but needed format if more logic is added
        #stems = []
        #for doc in docs:
            # No other options yet, just lemmatize
        #    stems.append([w.lemma_ for w in Doc(self.nlp.vocab, words=doc)])

        #  faster until more functionality needed
        from spacy.tokens import Doc
        return [[w.lemma_ for w in Doc(self.nlp.vocab, words=doc)] for doc in docs]

if __name__ == "__main__":
    import Tokenizer as ct
    # Must pass in filename to load a list of strings
    if len(sys.argv) is not 2:
        print("Usage: python3 Stemmer.py <docs>")
        print("docs: path to a pickled list of strings")
        sys.exit()
    filename = sys.argv[1]
    with open(ROOT_PATH + '/' + filename, 'rb') as f:
        docs = pkl.load(f)
    t = ct.Tokenizer('nltk')
    s = Stemmer('nltk', 'snowball')
    docs = t.apply(docs[:10])
    s.apply(docs)

