from collections import Counter
from nltk.corpus import stopwords 	
import nltk
import praw
import os
import json
from pprint import pprint
import time
import re #regular expression


id = ""
secret = ""
ps= ""
ua = ""
name = ""

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)


stop_words = set(stopwords.words('english'))

def subm(topic):							#writes to the file and aso return the url lsit 				
	item = topic+'.txt'						
	comment_lower = []
	url = []
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit=5):
		# print(submission.title)
		w = submission.url
		u = urlparse(w)
		uu = u.hostname
		if uu not in url:
			# u = urlparse(w)
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
							# u = urlparse(word)
							url.append(ww)
							print("##########")
					elif word not in stop_words:
						word = word.lower()
						comment_lower.append(word)

	return str(url), str(comment_lower)	

def Find(string):
	# findall() has been used to match string to url format
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)      
	return [x[0] for x in url]	

def splt1( u, t):
	ngrams = list(nltk.ngrams(t.split(' '), n=2))
	ngrams_count = {i : ngrams.count(i) for i in ngrams}
	return u, ngrams_count

def sortD(c, e, d):	
	item = c+".txt"							#function to sort dict by value in descending order
	# print(e)
	# print("\n")
	sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
	with open(item, "w+") as file1:	
		file1.write(e)
		file1.write('\n')
		for i in sort_orders[:20]:
			s = str(i[0])+str(i[1])
			file1.write(s+'\n')
	
		# print(i[0], i[1])
	print("Done")	

top = input("Enter the subreddit: ")  
a, b = subm(top) #returns the url list and comments words in list
z, y = splt1(a, b)  # return url list and count of words 
sortD(top,z, y) #prints url lsit and words count in sorted
