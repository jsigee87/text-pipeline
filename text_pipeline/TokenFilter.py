#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 6/26/18 

@author: Sanjana Kapoor
@author: John Sigmon

Last modified: 6/28/18
"""

import os
import sys
import json
import pickle as pkl
import spacy
import logging.config
from spacy.attrs import ORTH, LEMMA
from spacy.tokens import Doc

logger = logging.getLogger()
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

class TokenFilter():
    
    apply = None
    dispatch_fun = None

    # Default params
    to_lower = True

    # Supported params
    keep_alpha = False          # Keep only alphas
    keep_alpha_nums = True      # Keep only alphas and digits
    remove_stops = True
    remove_oov = False           # Out of Vocab
    remove_nums = False          # Removes anything resembling number
    add_special_case = None
    remove_url = True
    remove_email = True
    remove_punct = False
    threshold = None # Exclusive threshold

    def __init__(self, name, **params):
        '''

        :param name {str} name of the filtering you wish to use

        :param **params supported keywords are above as attributes

        '''
        
        self.dispatch_fun = {
                'spacy' : self.spacy,
                'nltk' : self.nltk,
                'frequency': self.frequency
                }
        
        # Choose library
        if name: 
            self.apply = self.dispatch_fun[name]
        
        # Parse params
        for key in params:
            setattr(self, key, params[key])
        logger.debug(vars(self))
        
        # Setup big files for vocab etc
        if name == 'spacy':
            #import en_core_web_md
            #self.nlp = en_core_web_md.load()
            import en_core_web_sm
            self.nlp = en_core_web_sm.load()
        
        if name == 'nltk':
            from nltk.corpus import words
            from nltk.corpus import stopwords
            if self.remove_stops is True:
                self.stop_words = set(stopwords.words('english'))

            if self.remove_oov is True:
                self.vocab = words.words() 
        
    def spacy(self, docs):
        '''
        Spacy tokenizer supports adding special cases. 

        The method takes the input docs, tokenizes them, and returns a list
        of lists of strings (tokens).

        : params {listlist[str]} documents to be filtered

        : returns {list[list[str]]} tokenized documents

        '''
        

        if self.add_special_case is not None:
            special_cases = self.add_special_case
            for pattern, replace in special_cases:
                logger.debug(type(pattern, replace))
                self.nlp.tokenizer.add_special_case(pattern, replace)
        
        # Tokenize
        tkns = []
        for doc in docs:
            # Intermediate steps are all tokens. Lemmatize at the end.
            # Add unicode text to tkns at end of intermediate steps
            # Pass over each doc multiple times to avoid complicated logic.
            doc = Doc(self.nlp.vocab,words=doc)
            if self.remove_stops is True:     
                doc = [t for t in doc if t.is_stop is False]

           # This functionality does not currently work on spacy end
           # if self.remove_oov is True:
           #     doc = [t for t in doc if t.is_oov is True] # keep if in vocab
            
            if self.keep_alpha is True:
                doc = [t for t in doc if t.is_alpha is True]

            if self.keep_alpha_nums is True:
                doc = [t for t in doc if t.is_alpha or t.is_digit is True]
                        
            if self.remove_punct is True:
                doc = [t for t in doc if t.is_punct is False]
            
            if self.remove_nums is True:
                doc = [t for t in doc if t.like_num is False]
            
            if self.remove_email is True:
                doc = [t for t in doc if t.like_email is False]
            
            if self.remove_url is True:
                doc = [t for t in doc if t.like_url is False]
            
            tkns.append([t.text for t in doc])

        
        return tkns 
    
    def nltk(self, docs):
        '''
        
        :param docs {list[list[str]]} 

        :returns {list[list[str]]} tokenized docs

        '''

        # Tokenize
        tkns = []
        for doc in docs:
        
            if self.remove_stops is True:
                doc = [w for w in doc if w not in self.stop_words]
            
            if self.remove_oov is True:
                doc = [w for w in doc if w in self.vocab]

            tkns.append(doc)
            
        return tkns        

    def frequency(self, docs):
        '''
        Remove words from the documents with frequency count under
        the threshold set by user. Threshold is exclusive (does not
        include the threshold itself).

        :params docs {list[list[str]]} documents

        :returns {list[list[str]]} filtered documents

        '''
        
        # Get frequency counts from doc
        freq_counts = {}
        for doc in docs:
            for w in doc:
                if w in freq_counts:
                    freq_counts[w] += 1
                else:
                    freq_counts[w] = 1

        # Get list of words that are to be removed
        remove_list = [w for w in freq_counts if freq_counts[w] < self.threshold]
        
        # Make new list of documents without words in remove_list
        return [[w for w in doc if w not in remove_list] for doc in docs]

if __name__ == "__main__":
    # Must pass in filename to load a list of strings
    if len(sys.argv) is not 2:
        print("Usage: python3 TokenFilter.py <docs>")
        print("docs: path to a pickled list of strings")
        sys.exit()
    filename = sys.argv[1]
    with open(ROOT_PATH + '/' + filename, 'rb') as f:
        docs = pkl.load(f)
