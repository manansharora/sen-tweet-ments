# sen-tweet-ments
Analyze tweets and measure the sentiments of a user's tweets

## Prerequisites
+ An approved Twitter developer account, and have activated the new developer portal experience. Access is available with active keys and tokens for a developer App that is attached to a Project created in the developer portal.
+ Python 3.6+ 

## Installation
Ensure that the prerequisites are fulfilled.
Install all the required packages mentioned in requirements.txt. Run the following command to install them at once
```bash
pip install -r /requirements/requirements.txt
```

Following this, run 
```bash
./get_keys
```
to set up your API and API secret key.

## Usage
To analyze a text and get its sentiment score, run
```bash
./text_sentiment.py "<text>"
```

To analyze a user's (must be public) tweets, run
```bash
./tweet_sentiment.py <account name> <number of tweets to be analyzer>
```

Note that the maximum number of tweets which can be analyzed is limited to 3200 by Twitter's API.

## Author
Manansh

## License
MIT
