# Pipeline Module

----

## Overview 
<p> This module contains several classes meant to provide a smooth process to clean text documents for preparation in NLP models, embedding generation, and other processes. Its goal is to provide a flexible way to pipeline and clean text while also allowing quick iteration and the ability to add your own functionality. </p>

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
<p> Please check the documentation below for the specific pipeline module to find out what names and parameters are supported.</p>

#### Example #1

<pre>
# Initialize corpus as a list of strings, where each string is a document
import text_pipeline as tp
docs = get_my_corpus()

t = tp.Tokenizer('spacy')
s = tp.Stemmer('nltk', stemmer='snowball')
pipeline = tp.Pipeline(t, s)
cleaned_docs = pipeline.apply(docs)
</pre>

#### Example #2

<pre>
# Initialize corpus as a list of strings, where each string is a document
import text_pipeline as tp
docs = get_my_corpus()

params = {
    'remove_stops': True,
    'remove_nums': True,
    }
t = tp.Tokenizer('spacy')
f = tp.TokenFilter('spacy', params)
s = tp.Stemmer('spacy')
f_2 = tp.TokenFilter('frequency', 5)
pipeline = tp.Pipeline(t, f, s, f_2)
cleaned_docs = pipeline.apply(docs)
</pre>

#### Example #3 

<pre>
# Initialize corpus as a list of strings, where each string is a document
import text_pipeline as tp
docs = get_my_corpus()

special_cases = [("don't", 
                [ {ORTH: "do"}, {ORTH: "n't", LEMMA: "not"}]
                )]
t = tp.Tokenizer('spacy') 
f = tp.TokenFilter(
        'spacy',
        {'add_special_case': special_cases}
        )
s = tp.Stemmer('nltk', stemmer='porter')
pipeline = tp.Pipeline(t, f, s)
cleaned_docs = pipeline.apply(docs)
</pre>

----

## Installation
You can install the module via `pip` by running `pip install text_pipeline` .

<p>
To install the various data needed for the underlying modules, we recommend you run the following command and provided script inside your virtual environment. If you need help setting up a virtual environment please check out <a href="http://docs.python-guide.org/en/latest/dev/virtualenvs/">The Hitchhiker's Guide to Python</a>, we personally recommend virtualenv.
</p>

<pre>
$ python -m spacy download en
$ python3 environment_setup.py
</pre>

----

## Usage

### Pipeline.py

<pre>
   <i> class </i> text_pipeline.<b>Pipeline</b>(<i>*args</i>) 
</pre>

#### Parameters:
<ul>
   <li><b>args:</b>    Instantiated objects to be applied to text <p> This is a variable length argument of objects to apply to the text. The objects must be listed in order that you wish to apply them. The onus is on the user to ensure the inputs and outputs of each class match.</p></li>
</ul>

#### Attributes:
<p> None</p>

#### Methods:
<ul>
   <li><b>apply(docs):</b>     Applies the pipeline to the text.
      <p><b>Parameters:</b>
         <ul><li><b>docs:</b> A list of strings, where each string represents a document.</li>
         </ul>
      </p>
      <p><b>Notes:</b>
         <p> Return will be a list of list of strings where strings are individual tokens or words.</p>
      </p>
   </li>
</ul>

----

### Tokenizer.py

<pre>
<i> class </i> text_pipeline.<b>Tokenizer</b>(<i>name</i>)
</pre>

#### Parameters:
<ul>
<li><b>name:</b>                string <p> The name of the tokenizer you wish to use.</p></li>
</ul>

#### Attributes:
<p> None</p>

#### Methods:
<ul>
<li><b>apply:</b> Runs the tokenizer as specified by parameter <i>name</i></li>
<li><b>spacy:</b> This helper method is executed by apply. It should not be accessed from outside the class.</li>
<li><b>nltk:</b> This helper method is executed by apply. It should not be accessed from outside the class.</li>
</ul>

#### Supported parameters for each <i>name</i>:

<ul>
   <li><b>spacy</b></li>
   <ul>
      <li>None</li>
   </ul> 
   <li><b>nltk</b></li>
   <ul>
      <li>None</li>
   </ul> 
</ul>

----

### TokenFilter.py

<pre>
<i> class </i> text_pipeline.<b>TokenFilter</b>(
                    <i>name</i>, 
			    <i>to_lower</i>=True, 
                            <i>lemmatize</i>=False, 
                            <i>remove_stops</i>=False, 
                            <i>remove_nums</i>=False,
                            <i>remove_oov</i>=False, 
                            <i>add_special_case</i>=None,
                            <i>remove_url</i>=True, 
                            <i>remove_email</i>=True, 
                            <i>remove_punct</i>=True)
</pre>

#### Parameters:
<ul>
<li><b>name:</b>                string <p> The name of the tokenizer you wish to use.</p></li>
<li><b>to_lower:</b>            boolean, optional, default True <p> When true this converts all text to lowercase. </p> </li>
<li><b>keep_alpha:</b>          boolean, optional, default False <p> If true, remove all tokens that are not alpha characters.</p></li>
<li><b>keep_alpha_nums:</b>     boolean, optional, default True <p> If true, remove all tokens that are not alpha characters or digits.</p></li>
<li><b>remove_stops:</b>        boolean, optional, default False <p> If true, remove stop words according to chosen tokenizer's stop word list.</p></li>
<li><b>remove_nums:</b>         boolean, optional, default False <p> If true, remove tokens that look like numbers.</p></li>
<li><b>remove_oov:</b>          boolean, optional, default False <p> If true, remove out of vocab words according to chosen tokenizer's vocabulary.</p></li>
<li><b>add_special_case:</b>    list[tuple(string, list[dict])], optional default None <p> Support for special cases in spacy. See example at beginning of Readme or Spacy documentation <a href="https://spacy.io/api/tokenizer">here</a> for more details.</p></li>
<li><b>remove_url:</b>          boolean, optional, default True <p> If true, remove tokens that look like urls.</p></li>
<li><b>remove_email:</b>        boolean, optional, default True <p> If true, remove tokens that look like emails.</p></li>
<li><b>remove_punct:</b>        boolean, optional, default False <p> If true, remove punctuation.</p></li>
<li><b>threshold:</b>           int, optional, default None <p> Removes words with frequency count below threshold. Bound is exclusive, i.e. remove if < threshold. </p></li>
</ul>

#### Attributes:
<p> None</p>

#### Methods:
<ul>
<li><b>apply:</b> Runs the tokenizer as specified by parameter <i>name</i></li>
<li><b>spacy:</b> This helper method is executed by apply. It should not be accessed from outside the class.</li>
<li><b>nltk:</b> This helper method is executed by apply. It should not be accessed from outside the class.</li>
<li><b>frequency:</b> This helper method is executed by apply. It should not be accessed from outside the class.</li>
</ul>

#### Supported parameters for each <i>name</i>:

<p> <b>spacy</b></p>
<ul>
   <li><b>to_lower</b></li> 
   <li><b>keep_alpha</b></li> 
   <li><b>keep_alpha_num</b></li> 
   <li><b>remove_stops</b></li> 
   <li><b>remove_num</b></li> 
   <li><b>add_special_case</b></li> 
   <li><b>remove_url</b></li> 
   <li><b>remove_email</b></li> 
   <li><b>remove_punct</b></li>
</ul>

<p><b>nltk</b></p>
<ul>
   <li><b>to_lower</b></li> 
   <li><b>remove_stops</b></li> 
   <li><b>remove_oov</b></li> 
</ul>

<p><b>frequency</b></p>
<ul>
   <li><b>threshold</b></li>
</ul>

----

### Stemmer.py

<pre>
<i> class </i> text_pipeline.<b>Stemmer</b>(<i>name</i>, 
			<i>stemmer</I>=None, 
		        <i>lemmatizer</i>=None)
</pre>

#### Parameters:
<ul>
<li><b>name:</b>                string <p> The name of the tokenizer you wish to use.</p></li>
<li><b>stemmer:</b>	str, optional, default None <p> When 'porter', PorterStemmer is used. When 'snowball', SnowballStemmer is used. </p></li>
<li><b>lemmatizer:</b>	str, optional, default None <p> When 'wordnet', WordNetLemmatizer is used. </p></li>
</ul>

#### Attributes:
<p> None</p>

#### Methods:
<ul>
<li><b>apply:</b> Runs the tokenizer as specified by parameter <i>name</i></li>
<li><b>spacy:</b> This helper method is executed by apply. It should not be accessed from outside the class.</li>
<li><b>nltk:</b> This helper method is executed by apply. It should not be accessed from outside the class.</li>
</ul>

#### Supported parameters for each name:

<p> <b>spacy</b></p>
<ul>
   <li><b>None</b></li> <p> Defaults to lemmatizer. </p> 
</ul>

<p><b>nltk</b></p>
<ul>
   <li><b>stemmer</b></li> 
   <li><b>lemmatizer</b></li> 
</ul>

#### Example Usage

<pre>
stemmer_1 = Stemmer('spacy')

# or
stemmer_2 = Stemmer('nltk', stemmer='snowball')
 
# or
stemmer_3 = Stemmer('nltk', stemmer='porter')

# or
stemmer_4 = Stemmer('nltk', lemmatizer='wordnet')
</pre>

----

## Testing

<p> If you wish to test the package after adding functionality or making modifictations, you can run the pre-existing unit tests yourself. From the terminal type:</p>
<pre>
$ cd text_pipeline_repository
$ ls 
 text_pipeline/    tests/    ...
$ python -m unittest tests.unit_tests
</pre>

## Contributing
<p> Thanks to Sanjana Kapoor for her help in writing this package, and thanks to Blaize Berry and Rachel Brynsvold for their insight and ideas. </p> 
<p> Contributions are welcome and encouraged. Email (johnsigmon@gmail.com) or pull request are both good ways to contribute.
</p>
