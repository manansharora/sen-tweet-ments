#!/usr/bin/env python3

import re

class Analyzer:
	""" Analyzes the input text and has a score function to return the sentiment score """

	def __init__(self):
		#positive = open("positive-words.txt", 'r')
		#negative = open("negative-words.txt", 'r')
		pass

	def score(self, text):
		text = re.sub('[^A-Za-z0-9]+', ' ', text)
		#text = re.sub(r'[()]+', ' ', text)
		#text = re.sub(r'+', ' ', text)
		words = text.split(" ")
		score = 0

		for word in words:
			found = False
			positive = open("positive-words.txt", 'r')
			negative = open("negative-words.txt", 'r')
			for line in positive.readlines():
				 if re.search(f"{word}$", line, re.I) and word != "": 
				 	score += 1
				 	found = True
				 	break
				
			if not found:
				for line in negative.readlines():
					if re.search(f'{word}$', line, re.I) and word != "": 
						score -= 1
						break
			positive.close();
			negative.close();
		return score	
