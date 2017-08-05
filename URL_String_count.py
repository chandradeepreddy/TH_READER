import re
from collections import Counter


file = open('URL_String.txt', "r")
Url_text = file.readlines()

text_blob = []
for i in range(len(Url_text)):
	if 1==1:
		text_blob = text_blob +re.split(r'[^a-zA-Z]+', Url_text[i].strip().lower())
		print i
		#print text_blob


text_file = open("URL_String_Freq.txt", "w")

wordCount = Counter(text_blob)  

for i in wordCount:
	text_file.write( str(wordCount[i]) +" : "+ i)
	text_file.write( '\n')
	#print str(wordCount[i]) +" : "+ i

text_file.close()