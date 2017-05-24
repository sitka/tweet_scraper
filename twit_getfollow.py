#Twitter API Keys are stored in a secret file
from twitter_API import consumer_key, consumer_secret, access_token, access_token_sectre
import tweepy
import csv
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_sectre)


#twitter is now authenticated


api = tweepy.API(auth)


#This loads up CSV file to write data to

csvFile = open('followers.csv', 'a')
csvWriter = csv.writer(csvFile)


#this will list the target user's list of followers

#followlist = ["jeffcharrison"]

for user in tweepy.Cursor(api.followers, screen_name="jeffcharrison").items(1):
	for account in tweepy.Cursor(api.followers).items(2):
		time.sleep(10)
		print user.screen_name, user.followers.screen_name,
		





#list1 = ['jeffcharrison', 'Bradsedal']

#print list1
 




#write rows to CSV file
#		analysis = TextBlob(tweet.text)
#		csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.retweet_count, tweet.user.screen_name, analysis.sentiment])
