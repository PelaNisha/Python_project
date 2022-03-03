import praw
import json
from pprint import pprint
import time
import re #regular expression

id = ""
secret = ""
ps= ""
ua = ""



name = "__special"

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)
topic = 'withyoualways'

def search_for():
	lst=[]
	red = reddit.subreddit(topic)
	for i in red.hot(limit=3):
		char ={
			'title':i.title,
			'url':i.url,
		}
		lst.append(char)
	return lst	

def url_find():
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit = 3):
		# submission.upvote()
		for comment in submission.comments:
			if hasattr(comment, "body"):
				comment_lower = comment.body.lower()
				# print(comment_lower)
				if Find(comment_lower):
					# print(submission.url)
					print(submission.url)
					comment.reply("Sastodeal\n\nSastodeal is an ecommerce site....\n\nContact: +977142343242\n\nEmails: contact@sastodeal.com\n\nSocial: facebook.com/sastodeal instagram.com/sastodeal\n\nMore: https:/index.plugin.builders/api/site/?url=sastodeal")
					time.sleep(660)
				else:
					pass	

def Find(string):
  
	# findall() has been used to match string to url format
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)      
	return [x[0] for x in url]

url_find()
