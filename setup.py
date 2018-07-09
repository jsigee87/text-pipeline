#! /usr/bin/env python3

# Author John Sigmon
# Created 6/28/18
# Last modified 6/28/18

from setuptools import setup
import os
import sys

_ = os.path.abspath(os.path.dirname(__file__))

#try:
#    from pypandoc import convert
#    read_md = lambda f: convert(f, 'rst')
#except ImportError:
#    print("warning: pypandoc module not found, could not convert Markdown to RST")
#    read_md = lambda f: open(f, 'r').read()

#with open('README.md', 'rb') as f:
#    readme = f.read()

requirements = [
    'spacy',
    'nltk',
    ]

setup(
    name='text_pipeline',
    version='1.2.1',
    description='A module for processing text documents in preparation for' +
        ' various NLP models or other tasks that required cleaned text.',
    #long_description=readme,
    #long_description_content_type='text/markdown',
    author='John Sigmon and Sanjana Kapoor',
    author_email='johnsigmon@gmail.com, sanjanakapoor793@gmail.com',
    packages=['text_pipeline'],
    license='MIT',
    install_requires=requirements
)
