# sen-tweet-ments
analyze tweets and measure the sentiments of a user
# Installation
Ensure that the prerequisites are fulfilled.
Install all packages mentioned in requirements.txt.
```bash
pip install <package name>
```

Following this, run 
```bash
./get_keys
```
to set up your API and API secret key.

# Usage
To analyze a text and get its sentiment score, run
```bash
./text_sentiment.py "<text>"
```

To analyze a user's (must be public) tweets, run
```bash
./tweet_sentiment.py <account name> <number of tweets to be analyzer>
```

Note that the maximum number of tweets which can be analyzed is limited to 3200 by Twitter's API.

# Examples
