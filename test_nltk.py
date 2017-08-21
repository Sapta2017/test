import os
from nltk import pos_tag, word_tokenize, FreqDist

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")


str='''In the third category he included those Brothers (the majority) who saw nothing in Freemasonry but the external forms and ceremonies, and prized the strict performance of these forms without troubling about their purport or significance. Such were Willarski and even the Grand Master of the principal lodge. Finally, to the fourth category also a great many Brothers belonged, particularly those who had lately joined. These according to Pierre's observations were men who had no belief in anything, nor desire for anything, but joined the Freemasons merely to associate with the wealthy young Brothers who were influential through their connections or rank, and of whom there were very many in the lodge.Pierre began to feel dissatisfied with what he was doing. Freemasonry, at any rate as he saw it here, sometimes seemed to him based merely on externals. He did not think of doubting Freemasonry itself, but suspected that Russian Masonry had taken a wrong path and deviated from its original principles. And so toward the end of the year he went abroad to be initiated into the higher secrets of the order.What is to be done in these circumstances? To favor revolutions, overthrow everything, repel force by force?No! We are very far from that. Every violent reform deserves censure, for it quite fails to remedy evil while men remain what they are, and also because wisdom needs no violence. "But what is there in running across it like that?" said Ilagin's groom. "Once she had missed it and turned it away, any mongrel could take it," Ilagin was saying at the same time, breathless from his gallop and his excitement. '''

tokens = word_tokenize(str)
print (tokens)

'''Method 	Functionality
s.find(t) 	index of first instance of string t inside s (-1 if not found)
s.rfind(t) 	index of last instance of string t inside s (-1 if not found)
s.index(t) 	like s.find(t) except it raises ValueError if not found
s.rindex(t) 	like s.rfind(t) except it raises ValueError if not found
s.join(text) 	combine the words of the text into a string using s as the glue
s.split(t) 	split s into a list wherever a t is found (whitespace by default)
s.splitlines() 	split s into a list of strings, one per line
s.lower() 	a lowercased version of the string s
s.upper() 	an uppercased version of the string s
s.title() 	a titlecased version of the string s
s.strip() 	a copy of s without leading or trailing whitespace
s.replace(t, u) 	replace instances of t with u inside s'''

fdist = FreqDist(word.lower() for word in tokens if not [.,])
print (fdist.most_common(12))
