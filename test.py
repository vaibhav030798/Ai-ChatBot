# import SyllableTokenizer() method from nltk

import nltk
from nltk.tokenize import word_tokenize
from nltk import SyllableTokenizer
	
# Create a reference variable for Class word_tokenize
tk = SyllableTokenizer()
	
# Create a string input
gfg = "hello my name is vaibhav"
	
# Use tokenize method
geek = tk.tokenize(gfg)
	
print(geek)
