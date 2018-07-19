----

## Overview 
<p> This package contains several modules/classes meant to provide a smooth process to clean text documents for preparation in NLP models, embedding generation, and other processes. Its goal is to provide a flexible way to pipeline and clean text while also allowing quick iteration and the ability to add your own functionality. The source code can be found <a href="https://github.com/jsigee87/text-pipeline">here</a>.</p>

<p> Separate modules are provided to execute individual pipeline steps. Each module requires a parameter called 
`name`
 to specify which underlying library to use, and a set of sometimes optional parameters to customize functionality. Modules are instantiated as objects and passed to the Pipeline constructor in the order you wish the steps to execute.</p>

## Quick Start
<p> Here are several code examples to get you started. As a note, the tokenizer module has the following input and output:</p>
<ul>
    <li><b>Input:</b>   List of strings representing a list of 'documents'</li>
    <li><b>Output:</b>  List of list of strings representing a list of documents split into words or tokens</li>
</ul>
<p> The other modules have the following input and output:</p>
<ul>
    <li><b>Input:</b>   List of list of strings representing a list of documents split into words or tokens</li>
    <li><b>Output:</b>  List of list of strings representing a list of documents split into words or tokens</li>
</ul>
<p> Please check the usage documentation for the specific module to find out what names and parameters are supported. Also note that each pipeline step will display a single progress bar, with the exception of frequency filtering, which will display three separate bars.</p>

#### Example #1

```python
# Initialize corpus as a list of strings, where each string is a document
import text_pipeline as tp
docs = get_my_corpus()

t = tp.Tokenizer('spacy')
s = tp.Stemmer('nltk', stemmer='snowball')
pipeline = tp.Pipeline(t, s)
cleaned_docs = pipeline.apply(docs)
```

#### Example #2

```python
# Initialize corpus as a list of strings, where each string is a document
import text_pipeline as tp
docs = get_my_corpus()

params = {
    'remove_stops': True,
    'remove_nums': True,
    }
t = tp.Tokenizer('spacy')
f = tp.TokenFilter('spacy', **params)
s = tp.Stemmer('spacy')
f_2 = tp.TokenFilter('frequency', 5)
pipeline = tp.Pipeline(t, f, s, f_2)
cleaned_docs = pipeline.apply(docs)
```

#### Example #3 

```python
# Initialize corpus as a list of strings, where each string is a document
import text_pipeline as tp
docs = get_my_corpus()

special_cases = [("don't", 
                [ {ORTH: "do"}, {ORTH: "n't", LEMMA: "not"}]
                )]
t = tp.Tokenizer('spacy') 
f = tp.TokenFilter(
        'spacy',
        add_special_case=special_cases
        )
s = tp.Stemmer('nltk', stemmer='porter')
pipeline = tp.Pipeline(t, f, s)
cleaned_docs = pipeline.apply(docs)
```

----

## Installation
You can install the module via `pip` by running `pip install text-pipeline` .

<p>
To install the various data needed for the underlying modules, we recommend you run the following commands inside your virtual environment. If you need help setting up a virtual environment please check out <a href="http://docs.python-guide.org/en/latest/dev/virtualenvs/">The Hitchhiker's Guide to Python</a>, we personally recommend virtualenv.
</p>

```bash
$ python -m spacy download en
$ python3
> import nltk
> nltk.download('punkt')
> nltk.download('wordnet')
> nltk.download('words')
> nltk.download('stopwords')
```

----

## Usage
<p> Please see readme inside the text_pipeline folder for further documentation.</p>

----

## Testing

<p> If you wish to test the package after adding functionality or making modifictations, you can run the pre-existing unit tests yourself. From the terminal type:</p>

```bash
$ cd text_pipeline_repository
$ ls 
 text_pipeline/    tests/    ...
$ python -m unittest tests.unit_tests
```

---

## Future Work

<p> Improve logging capabilities, including around progress bars.</p>
<p> Add functionality, including other tokenizers, other classes that can be pipeline steps (n-gram etc.)</p>
<p> Suggestions welcome!</p>

---

## Contributing
<p> Thanks to Sanjana Kapoor for her help in writing this package, and thanks to Blaize Berry and Rachel Brynsvold for their insight and ideas. </p> 
<p> Contributions are welcome and encouraged. Email (johnsigmon@gmail.com) or pull request are both good ways to contribute.
</p>
