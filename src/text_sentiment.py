#!/usr/bin/env python3

from analyzer import Analyzer
import sys

def main():
	analyzer = Analyzer()
	print(analyzer.score(sys.argv[1]))

if __name__ == '__main__':
	main()
