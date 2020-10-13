# Print a user's timeline. This will get up to 3,200 tweets, which
# is the maximum the Twitter API allows.

from TwitterAPI import TwitterAPI, TwitterPager

def get_timeline(SCREEN_NAME, max):
	
	with open("keys.txt", 'r') as f:
		consumer_key = f.readline()
		consumer_key = consumer_key.rstrip("\n")
		consumer_secret = f.readline()

	api = TwitterAPI(consumer_key,
					 consumer_secret,
					 auth_type='oAuth2')

	pager = TwitterPager(api, 
						 'statuses/user_timeline', 
						 {'screen_name':SCREEN_NAME, 'count':200})

	tweets = []
	count = 0
	for item in pager.get_iterator(wait=3.5):
		if 'text' in item:
			count += 1
			tweets.append(item['text'])
		if count > (max-1):
			break
	
	return tweets
