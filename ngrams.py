from collections import Counter
from nltk.corpus import stopwords 	
import nltk
import praw
import os

id = ""
secret = ""
ps= ""
ua = ""
name = ""

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)

stop_words = set(stopwords.words('english'))

def subm(topic):					
	item = topic+'.txt'						#and convert comments to a large string
	comment_lower = []
	url = []
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit=10):
		for comment in submission.comments:
			if hasattr(comment, "body"):
				for word in comment.body.split():
					if Find(word):
						if word not in url:
							url.append(word)
							print("##########")
					elif word not in stop_words:
						word = word.lower()
						comment_lower.append(word)
			
	with open(item, "w+") as file1:	
		file1.write(str(url))
		file1.write('*')
		file1.write(str(comment_lower))
	return url, comment_lower	

def Find(string):
	# findall() has been used to match string to url format
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)      
	return [x[0] for x in url]	

def keyRead(top):	
	item= top+'.txt'
	if os.path.isfile(item):							#function to convert the string to a list of items
		with open(item, "r+") as file1:
			content = file1.read()
			content_list = content.split("*")
			file1.close()
			return content_list[0],content_list[1]
	else:
		return subm(top)

def splt1(u, t):
	ngrams = list(nltk.ngrams(t.split(' '), n=2))
	ngrams_count = {i : ngrams.count(i) for i in ngrams}
	return u, ngrams_count

def sortD(e, d):								#function to sort dict by value in descending order
	print(e)
	print("\n")
	sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
	for i in sort_orders:
		print(i[0], i[1])

top = input("Enter the subreddit: ")
# subm(top)
a, b = keyRead(top)
z, y = splt1(a, b)
sortD(z, y)
