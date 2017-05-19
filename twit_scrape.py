 
#Twitter API Keys are stored in a secret file
from twitter_API import consumer_key, consumer_secret, access_token, access_token_sectre
import tweepy
import csv
from textblob import TextBlob

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_sectre)

#twitter is now authenticated


api = tweepy.API(auth)


csvFile = open('FPM4.csv', 'a')
csvWriter = csv.writer(csvFile)


#this is the Twitter query

for tweet in tweepy.Cursor(api.search,
					q = "#ourvoicesarevital", 
					since = "2017-05-17",
					until = "2017-05-18",
					lang = "en").items(10):

#write rows to CSV file
		analysis = TextBlob(tweet.text)
		csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.retweet_count, tweet.user.screen_name, analysis.sentiment])
		print tweet.created_at, tweet.text, analysis.sentiment,

csvFile.close()


#for tweet in public_tweets:
#	print(tweet.text)
#	analysis = TextBlob(tweet.text)
#	print(analysis.sentiment)

#

	