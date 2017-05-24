#Twitter API Keys are stored in a secret file
from twitter_API import consumer_key, consumer_secret, access_token, access_token_sectre
import tweepy
import csv

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_sectre)


#twitter is now authenticated


api = tweepy.API(auth)



list1 = ['jeffcharrison', 'Bradsedal']

for account in list1:
	print(account)

	