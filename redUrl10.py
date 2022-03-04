from gettext import find
from html5lib import serialize
import praw
from pprint import pprint
import re #regular expression

id = "_A9_qXJrlNxXExhn-ZK8RQ"
secret = "VD0ySjDluZgk74q00tGe_HX-whWZwg"
ps= "songjoongki"
ua = "first_app"
name = "__special"

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)
topic = 'redditdev'

def search_for(topic):
	lst=[]
	red = reddit.subreddit(topic)
	for i in red.hot(limit=3):
		char ={
			'title':i.title,
			'url':i.url,
		}
		lst.append(char)
	return lst	

def subm(topic):
	count = 0
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit=10):
		for comment in submission.comments:
			if hasattr(comment, "body"):
				comment_lower = comment.body.lower()
				if Find(comment_lower) and count<10:
					print(comment.body)
					count= count+1
				elif not Find(comment_lower):
					pass
						# comment.reply("Reply from a puppet")
						# time.sleep(660)
		print("*****************")
		count=0

def Find(string):
	# findall() has been used to match string to url format
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)      
	return [x[0] for x in url]

a = input("enter the topic: ")
print(subm(a))
# print(b)