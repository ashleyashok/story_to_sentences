# Arrange sentences in a story in alphabetical order

import re

def story_to_sentences(filename):
	file = open(filename,'r')
	text = file.read()
	text = text.replace("------","")
	sentences = re.split('\n|(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
	sentences = filter(None, sentences)
	sentences = sorted(sentences, key=lambda s: s if s.isalnum() else re.sub(r"^[^a-zA-Z0-9]+", '', s))
	print(*sentences, sep = "\n")

	return sentences

file = 'ShortStory.txt'
sentences = story_to_sentences(file)

