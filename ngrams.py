from collections import Counter
from nltk.corpus import stopwords 	
import nltk
import praw
import os
import json
from pprint import pprint
import time
import re #regular expression

from urllib.parse import urlparse

id = ""
secret = ""
ps= ""
ua = ""
name = ""

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)

stop_words = set(stopwords.words('english'))

def subm(topic):											
	item = topic+'.json'						
	comment_lower = []
	url = []
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit=5):
		# print(submission.title)
		w = submission.url
		u = urlparse(w)
		uu = u.hostname
		if uu not in url:
			url.append(uu)
			print("##########")
		for word in submission.title.split():
			if word not in stop_words:
				word = word.lower()
				comment_lower.append(word)
		for comment in submission.comments[:5]:
			if hasattr(comment, "body"):
				for word in comment.body.split():
					if Find(word):
						w = urlparse(word)
						ww = w.hostname
						if ww not in url:
							url.append(ww)
							print("##########")
					elif word not in stop_words:
						word = word.lower()
						comment_lower.append(word)

	splt1(topic, str(url), str(comment_lower))

def Find(string):
	# findall() has been used to match string to url format
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)      
	return [x[0] for x in url]	

def iffile(topic):
	item= topic+'.json'
	if os.path.isfile(item):
		return parse(item)
	else:
		return subm(topic)   

def splt1(topic, u, t):
	ngrams = list(nltk.ngrams(t.split(' '), n=2))
	ngrams_count = {i : ngrams.count(i) for i in ngrams}
	sortD(topic, u, ngrams_count)

def sortD(c, e, d):	
	item = c+".json"	
	mydict = {}		
	urldict = {}
	urldict['url'] = e			
	keylist = []
	keylist.append(urldict)
	sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
	for i in sort_orders[:20]:
		mydict['words'] = i[0]
		mydict['count'] = i[1]
		keylist.append(mydict)
		mydict = {}
	with open(item, "w+") as f:
		json.dump(keylist, f, indent = 2)
	return keylist

def parse(top):
	with open(top, 'r') as f:
		data = json.load(f)
	return data


top = input("Enter the subreddit: ")  
result = iffile(top) 
print(result)
