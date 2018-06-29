#! /usr/bin/env python3

# Author John Sigmon
# Created 6/28/18
# Last modified 6/28/18

from setuptools import setup

requirements = [
    'spacy',
    'nltk',
    ]

setup(
    name='text_pipeline',
    version='1.0',
    description='A module for processing text documents in preparation for' +
        ' various NLP models or other tasks that required cleaned text.',
    author='John Sigmon and Sanjana Kapoor',
    author_email='johnsigmon@gmail.com, sanjanakapoor793@gmail.com',
    packages=['text_pipeline'],
    license='MIT',
    install_requires=requirements
)
