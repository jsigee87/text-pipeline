#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:56:01 2018

@author: Sanjana Kapoor 
@author: John Sigmon

Last modified: 6/26/18
"""

import os
import sys
import json
import pickle as pkl
import spacy
import en_core_web_sm
import logging.config
from nltk.tokenize import word_tokenize
from spacy.attrs import ORTH, LEMMA

logger = logging.getLogger()
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

class Tokenizer():
    
    apply = None
    dispatch_fun = None
    to_lower = True

    def __init__(self, name, *params):
        '''

        :param name {str} name of the tokenizer you wish to use

        :param *params {dict} params should be a python dictionary

        '''
        
        self.dispatch_fun = {
                'spacy' : self.spacy,
                'nltk' : self.nltk,
                }
        if name: 
            self.apply = self.dispatch_fun[name]
        for key in params:
            setattr(self, key, params[key])
        
        # Setup big files for vocab etc
        if name == 'spacy':
            import en_core_web_sm
            self.nlp = en_core_web_sm.load()

    def spacy(self, docs):
        '''
        Spacy tokenizer supports adding special cases. 

        The method takes the input docs, tokenizes them, and returns a list
        of lists of strings (tokens).

        : params {list[str]} documents to be tokenized

        : returns {list[list[str]]} tokenized documents

        '''
        
        # Tokenize
        tkns = []
        for doc in docs:
            if self.to_lower is True:
                doc = doc.lower()
            doc = self.nlp.tokenizer(doc)
            tkns.append([t.text for t in doc])

        return tkns 

    def nltk(self, docs):
        '''
        
        :param docs {list[str]} 

        :returns {list[list[str]]} tokenized docs

        '''
        
        # Tokenize
        tkns = []
        for doc in docs:
            if self.to_lower is True:
                doc = doc.lower()
            doc = word_tokenize(doc)
            tkns.append(doc)
        
        return tkns        
    
if __name__ == "__main__":
    # Must pass in filename to load a list of strings
    if len(sys.argv) is not 2:
        print("Usage: python3 Tokenizer.py <docs>")
        print("docs: path to a pickled list of strings")
        sys.exit()
    filename = sys.argv[1]
    with open(ROOT_PATH + '/' + filename, 'rb') as f:
        docs = pkl.load(f)
    
    # First make sure it works without specifying params
    #t_1 = Tokenizer('spacy')
    #t_1.apply(docs[:10])

    #t_2 = Tokenizer('nltk')
    #t_2.apply(docs[:10])

    # Then try arbitrary unsupported params
    #t_3 = Tokenizer('spacy', {'unsupportedparam': 'nonsense'})
    #t_3.apply(docs[:10])
    
    # Then try add_special_case

    test_case = [("don't", [{ORTH: "do"}, {ORTH: "n't", LEMMA: "not"}])]
    params = {'add_special_case': test_case, 'lemmatize': True, 'remove_stops': True}
    tester = Tokenizer('spacy', params)
    tester.apply(docs[:20])

