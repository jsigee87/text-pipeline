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
from tqdm import tqdm

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
            stems = [[stemmer.stem(w) for w in doc] for doc in tqdm(docs)]
        else:
            stems = [[lemmatizer.lemmatize(w) for w in doc] for doc in tqdm(docs)]
        
        logger.debug("Type of return: %s", type(stems))
        logger.debug("Length: %d", len(stems))
        logger.debug("Length of first entry: %d", len(stems[0]))
        return stems        
    
    def spacy(self, docs):
        '''
        Uses the lemma attribute of the spacy token.
        
        :params docs {list[list[str]]}
       
        :returns {list[list[str]]} stems of words or tokens

        '''
        from spacy.tokens import Doc
  
        stems = []
        for doc in tqdm(docs):
            doc = Doc(self.nlp.vocab, words=doc)
            stems.append([w.lemma_ for w in doc])
            del doc
        
        return stems
        #return [[w.lemma_ for w in Doc(self.nlp.vocab, words=doc)] for doc in docs]
