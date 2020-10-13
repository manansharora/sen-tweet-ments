#!/usr/bin/env python3

import matplotlib.pyplot as plt

class Stats:
	
	def pieChart(self, frequencies):
		labels = ['Positive Tweets', 'Negative Tweets', 'Neither negative nor positive']


		plt.pie(frequencies, labels = labels, autopct='%1.2f%%')
		plt.axis('equal')

		plt.show()
		#plt.savefig('foo.png')
