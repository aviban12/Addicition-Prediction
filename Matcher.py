# Import the Matcher and initialize it with the shared vocabulary
from spacy.matcher import Matcher
import spacy
nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)
# Create a pattern matching two tokens: "iPhone" and "X"
pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]

# Add the pattern to the matcher
matcher.add('IPHONE_X_PATTERN', None, pattern)
data = 'New iPhone X release date leaked as Apple reveals pre-orders by mistake'
doc = nlp(data)
# Use the matcher on the doc
matches = matcher(doc)
print(matches)
print('Matches:', [doc[start:end].text for match_id, start, end in matches])
