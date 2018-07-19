
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

```python
stemmer_1 = Stemmer('spacy')

# or
stemmer_2 = Stemmer('nltk', stemmer='snowball')
 
# or
stemmer_3 = Stemmer('nltk', stemmer='porter')

# or
stemmer_4 = Stemmer('nltk', lemmatizer='wordnet')
```

