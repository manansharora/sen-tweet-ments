#!/usr/bin/env python3

import sys
from tweet_dumper import *
from analyzer import Analyzer
from stats import Stats
from tqdm import tqdm

frequencies = [0, 0, 0]

def main():
	if len(sys.argv) != 3:
		sys.exit("Usage: ./tweet-sentiment <twitter username> <number of tweets to analyse>(without the <>)")
	
	username = sys.argv[1]
	count = int(sys.argv[2])

	if count is None:
		count = 1

	tweets = get_timeline(username, count)
	if tweets is None:
		return 
	
	analyzer = Analyzer()
	stats = Stats()
	sum = 0
	
	for tweet in tqdm(tweets):
		tweet_score = analyzer.score(tweet)
		sum += tweet_score
		if tweet_score > 0.0:
			frequencies[0] += 1
		elif tweet_score < 0.0:
			frequencies[1] += 1
		else:
			frequencies[2] += 1
	
	try:
		average = sum / len(tweets) 
	except ZeroDivisionError:
		raise RuntimeError("No tweets made")
	print(f"Sentiment average score = {average}")
	stats.pieChart(frequencies)	

if __name__ == "__main__":
	main()
