#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:02:44 2018

@author: s0k00rp
@author: John Sigmon

Last modified: 6/22/18
"""

import pickle as pkl
import sys
import os
import json
import logging.config

logger = logging.getLogger()
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

class Pipeline:
    
    steps = None

    def __init__(self, *args):
        """
        Set up basic pipeline attributes
        """
        
        self.steps = args

    def apply(self, docs):
        for step in self.steps:
            logger.info("Running step {}".format(step))
            docs = step.apply(docs)
        return docs

if __name__=="__main__":
    import Tokenizer as ct
    # Must pass in filename to load a list of strings
    if len(sys.argv) is not 2:
        print("Usage: python3 Pipeline.py <docs>")
        print("docs: path to a pickled list of strings")
        sys.exit()
    filename = sys.argv[1]
    with open(ROOT_PATH + '/' + filename, 'rb') as f:
        docs = pkl.load(f)

    t = ct.Tokenizer('spacy')
    pipeline = Pipeline(t)
    pipeline.apply(docs[:10])
