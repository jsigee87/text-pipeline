# Author John Sigmon
# Created 6/26/18
# Modified 6/26/18

# Make dictionary for unit testing

import pickle as pkl

test_docs ={}
# Stop words
test_docs['stopwords_01'] = 'Except could i: What will I look like-This is a sentence'

# Out of Vocab
test_docs['oov_01'] = 'This sentence has only English gii oiwiem lalew. /kzskre sliejlw'

# Numbers
test_docs['numbers_01'] = 'This sentence $59 has ten no 1 numbers'

# Punctuation
test_docs['punct_01'] = 'This! sentence() ?has. no, [punctuation]'

# Emails
test_docs['emails_01'] = 'This sentence john@gmail.com has no paul@yahoo.net emails'

# URL
test_docs['url_01'] = 'This sentence www.enron.com has https://spacy.io no urls'

# Stemmer/ LEmmatizer
test_docs['stems_01'] = "Running don't doesn't crying going gone tested"

filename = 'test_docs.pkl'
with open(filename, 'wb') as f:
    pkl.dump(test_docs, f)
