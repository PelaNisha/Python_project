from collections import Counter
from nltk.corpus import stopwords 	
import nltk
import praw
import os

id = "_A9_qXJrlNxXExhn-ZK8RQ"
secret = "VD0ySjDluZgk74q00tGe_HX-whWZwg"
ps= "songjoongki"
ua = "first_app"
name = "__special"

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)
topic = 'withyoualways'

stop_words = set(stopwords.words('english'))

def subm(topic):							#function to write the 10 comments from each post to a file	
	item = topic+'.txt'						#and convert comments to a large string
	comment_lower = ""
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit=2):
		for comment in submission.comments[:10]:
			if hasattr(comment, "body"):
				comment_lo = comment.body.lower()
				comment_lower = comment_lower + " "+comment_lo
				print("*****")
		print("*****************")
	with open(item, "w+") as file1:	
		file1.write(comment_lower)
	return comment_lower

def keyRead(top):	
	item= top+'.txt'
	if os.path.isfile(item):							#function to convert the string to a list of items
		with open(item, "r+") as file1:
			content =  file1.read()
			return content
	else:
		return subm(top)

def splt1(a):
	ngrams = list(nltk.ngrams(a.split(' '), n=2))
	ngrams_count = {i : ngrams.count(i) for i in ngrams}
	return ngrams_count

def sortD(d):								#function to sort dict by value in descending order
	sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
	for i in sort_orders:
		print(i[0], i[1])

top = input("Enter the subreddit: ")
x = keyRead(top)
y = splt1(x)
sortD(y)