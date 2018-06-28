#!/usr/bin/env python3

"""
Created on 6/26/18

@author: John Sigmon

Last modified: 6/26/18
"""

import os
import warnings
import pickle as pkl
import unittest
import TokenFilter as fltr
import Tokenizer as ctkn
import Stemmer as stm
import Pipeline as pipe

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

class TestPipeline(unittest.TestCase):
   
    def setUp(self):
        warnings.simplefilter('ignore')
        filename = 'test_docs.pkl'
        with open(ROOT_PATH + '/' + filename, 'rb') as f:
            self.test_docs = pkl.load(f)

    def test_spacy_stops(self):
        warnings.simplefilter('ignore')
        expected_output = [[':', 'look', 'like', '-', 'sentence']]
        docs = []
        docs.append(self.test_docs['stopwords_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': True,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'Spacy did not remove stop words')

    def test_nltk_stops(self):
        warnings.simplefilter('ignore')
        expected_output = [['except', 'could', ':', 'look', 'like-this', 'sentence']]
        docs = []
        docs.append(self.test_docs['stopwords_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': True,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('nltk')
        f = fltr.TokenFilter('nltk', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'NLTK did not remove stop words')
    
    def test_nltk_stops_02(self):
        warnings.simplefilter('ignore')
        expected_output = [['except', 'could', ':', 'look', 'like', '-', 'sentence']]
        docs = []
        docs.append(self.test_docs['stopwords_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': True,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('nltk', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'NLTK did not remove stop words')

    def test_spacy_oov(self):
        warnings.simplefilter('ignore')
        expected_output = [['this', 'sentence', 'has', 'only', 'english']]
        docs = []
        docs.append(self.test_docs['oov_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': False,
                'remove_oov': True,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': True,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'Spacy did not remove non English words')

    def test_nltk_oov(self):
        warnings.simplefilter('ignore')
        expected_output = [['this', 'sentence', 'only']]
        docs = []
        docs.append(self.test_docs['oov_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': False,
                'remove_oov': True,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': True,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('nltk')
        f = fltr.TokenFilter('nltk', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'NLTK did not remove non English words')

    def test_spacy_numbers(self):
        warnings.simplefilter('ignore')
        expected_output = [['this', 'sentence', '$', 'has', 'no', 'numbers']]
        docs = []
        docs.append(self.test_docs['numbers_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': False,
                'remove_oov': False,
                'remove_nums': True,
                'remove_url': False,
                'remove_email': True,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'Spacy did not remove numbers')

    def test_spacy_punct(self):
        warnings.simplefilter('ignore')
        expected_output = [['this', 'sentence', 'has', 'no', 'punctuation']]
        docs = []
        docs.append(self.test_docs['punct_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': False,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': True,
                'remove_punct': True
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'Spacy did not remove punctuation')

    def test_spacy_emails(self):
        warnings.simplefilter('ignore')
        expected_output = [['this', 'sentence', 'has', 'no', 'emails']]
        docs = []
        docs.append(self.test_docs['emails_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': False,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': True,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'Spacy did not remove emails')

    def test_spacy_url(self):
        warnings.simplefilter('ignore')
        expected_output = [['this', 'sentence', 'has', 'no', 'urls']]
        docs = []
        docs.append(self.test_docs['url_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': False,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': True,
                'remove_email': False,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'Spacy did not remove urls')

    def test_spacy_lemma(self):
        warnings.simplefilter('ignore')
        expected_output = [['run', 'not', 'not', 'cry', 'go', 'go', 'test']]
        docs = []
        docs.append(self.test_docs['stems_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': False,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        s = stm.Stemmer('spacy')
        p = pipe.Pipeline(t, f, s)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'Spacy did not lemmatize') 

    def test_nltk_snow_stemmer(self):
        warnings.simplefilter('ignore')
        expected_output = [['run', "n't", "n't", 'cri', 'go', 'gone', 'test']]
        docs = []
        docs.append(self.test_docs['stems_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': False,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        s = stm.Stemmer('nltk', stemmer='snowball')
        p = pipe.Pipeline(t, f, s)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'NLTK Snowball did not stem')

    def test_nltk_porter_stemmer(self):
        warnings.simplefilter('ignore')
        expected_output = [['run', "n't", "n't", 'cri', 'go', 'gone', 'test']]
        docs = []
        docs.append(self.test_docs['stems_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': False,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        s = stm.Stemmer('nltk', stemmer='porter')
        p = pipe.Pipeline(t, f, s)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'NLTK Porter did not stem')

    def test_nltk_lemmatizer(self):
        warnings.simplefilter('ignore')
        expected_output = [['running', "n't", "n't", 'cry', 'going', 'gone', 'tested']]
        docs = []
        docs.append(self.test_docs['stems_01'])
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': False,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': False,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        s = stm.Stemmer('nltk', lemmatizer='wordnet')
        p = pipe.Pipeline(t, f, s)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output, 
                'NLTK lemmatiZZZZzer did not lemmatize')

    def test_remove_non_alphas_01(self):
        warnings.simplefilter('ignore')
        expected_output = [
                ['look', 'like', 'sentence'],
                ['sentence', 'numbers'],
                ['sentence', 'punctuation'],
                ['sentence', 'emails']
                ]
        docs = [
                self.test_docs['stopwords_01'],
                self.test_docs['numbers_01'],
                self.test_docs['punct_01'],
                self.test_docs['emails_01'],
                ]
        params = {
                'keep_alpha': True,
                'keep_alpha_nums': False,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': False,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output) 
    
    def test_remove_non_alphas_02(self):
        warnings.simplefilter('ignore')
        expected_output = [
                ['look', 'sentence'],
                ['sentence', 'numbers'],
                ['sentence', 'punctuation'],
                ['sentence', 'john', 'paul', 'emails']
                ]
        docs = [
                self.test_docs['stopwords_01'],
                self.test_docs['numbers_01'],
                self.test_docs['punct_01'],
                self.test_docs['emails_01'],
                ]
        params = {
                'keep_alpha': True,
                'keep_alpha_nums': False,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': False,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('nltk')
        f = fltr.TokenFilter('spacy', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output) 

    def test_remove_non_alphas_03(self):
        warnings.simplefilter('ignore')
        expected_output = [
                ['look', 'like', 'sentence'],
                ['sentence', '59', '1', 'numbers'],
                ['sentence', 'punctuation'],
                ['sentence', 'emails']
                ]
        docs = [
                self.test_docs['stopwords_01'],
                self.test_docs['numbers_01'],
                self.test_docs['punct_01'],
                self.test_docs['emails_01'],
                ]
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': True,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': False,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('spacy')
        f = fltr.TokenFilter('spacy', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output) 
    
    def test_remove_non_alphas_04(self):
        warnings.simplefilter('ignore')
        expected_output = [
                ['look', 'sentence'],
                ['sentence', '59', '1', 'numbers'],
                ['sentence', 'punctuation'],
                ['sentence', 'john', 'paul', 'emails']
                ]
        docs = [
                self.test_docs['stopwords_01'],
                self.test_docs['numbers_01'],
                self.test_docs['punct_01'],
                self.test_docs['emails_01'],
                ]
        params = {
                'keep_alpha': False,
                'keep_alpha_nums': True,
                'remove_stops': True,
                'remove_oov': False,
                'remove_nums': False,
                'remove_url': False,
                'remove_email': False,
                'remove_punct': False
                }
        
        t = ctkn.Tokenizer('nltk')
        f = fltr.TokenFilter('spacy', **params)
        p = pipe.Pipeline(t, f)
        test_output = p.apply(docs)
        self.assertEqual(test_output, expected_output) 
    
if __name__=="__main__":
    unittest.main()
