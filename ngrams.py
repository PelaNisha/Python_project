from collections import Counter
from nltk.corpus import stopwords 	
import nltk
import praw
import os
import json
import re
from urllib.parse import urlparse

id = ""
secret = ""
ps= ""
ua = ""
name = ""

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)

stop_words = set(stopwords.words('english'))

def collectUrlComt(topic):							
	comment_lower = ""
	url = []
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit=5):
		subUrl = submission.url
		uPar = urlparse(subUrl)
		hostNm = uPar.hostname
		if hostNm not in url:
			url.append(hostNm)
			print("##########")
		for word in submission.title.split():
			if word not in stop_words:
				word = word.lower()
				comment_lower = comment_lower+" "+word
		for comment in submission.comments[:5]:
			if hasattr(comment, "body"):
				for word in comment.body.split():
					if isUrl(word):
						wUrlPar = urlparse(word)
						wUrlNam = wUrlPar.hostname
						if wUrlNam not in url:
							url.append(wUrlNam)
							print("##########")
					elif word not in stop_words:
						word = word.lower()
						comment_lower = comment_lower+" "+word

	return countCmt(topic, url, comment_lower)

def isUrl(string):
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)      
	return [x[0] for x in url]	

def ifFile(topic):
	item= topic+'.json'
	if os.path.isfile(item):
		return parse(item)
	else:
		return collectUrlComt(topic)   

def countCmt(topic, u, t):
	ngrams = list(nltk.ngrams(t.split(), n=2))
	ngrams_count = {i : ngrams.count(i) for i in ngrams}
	return sortCmtPhrse(topic, u, ngrams_count)

def sortCmtPhrse(c, e, d):	
	item = c+".json"	
	worddict = {}		
	urldict = {}
	urldict['url'] = e				
	finalList = []
	finalList.append(urldict)
	sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
	for i in sort_orders[:20]:
		worddict['words'] = i[0]
		worddict['count'] = i[1]
		finalList.append(worddict)
		worddict = {}
	with open(item, "w+") as f:
		json.dump(finalList, f, indent = 2)
	return "saved in file"

def parse(top):
	print("File Present!")
	with open(top, 'r') as f:
		data = json.load(f)
	#Call retUrl to print the urls and retWord to print words	
	return 
	
def retUrl(data):
	return data[0]['url']

def retWord(data):
	for i in range(1, len(data)):
		print(data[i])
	return "End of file"	

topic = input("Enter the subreddit: ")  
result = ifFile(topic) 
print(result)
