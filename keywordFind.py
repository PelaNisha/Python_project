from gettext import find
from html5lib import serialize
import praw
import nltk
from nltk.corpus import stopwords
from pprint import pprint
import re #regular expression
from collections import Counter

from sqlalchemy import null


id = ""
secret = ""
ps= ""
ua = ""
name = ""

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)
topic = 'withyoualways'

stop_words = set(stopwords.words('english'))

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
	comment_lower = ""
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit=2):
		# print(type(submission))
		for comment in submission.comments:
			if hasattr(comment, "body") and count<10:
				comment_lo = comment.body.lower()
				with open("myfile.txt", "a+") as file1:
						# Writing data to a file
					comment_lower = comment_lower + " "+comment_lo
					file1.write(comment_lower)
					# print(comment.body)
					count= count+1
				
						# comment.reply("Reply from a puppet")
						# time.sleep(660)
		print("*****************")
		count=0

def keyRead():
	li = []
	with open("myfile.txt", "r+") as file1:
		# print(file1.read())
		li.append(file1.read())
	return (str(li))

def splt(a):
	my_dict = {}
	words = a.split()
	word_counts = Counter(words)
	for word, count in sorted(word_counts.items()):
		if word not in stop_words:
			my_dict[word] = [count]
		# my_dict
		# print('"%s" is repeated %d time%s.' % (word, count, "s" if count > 1 else ""))
	# print(max(count))
	return my_dict
	
def sortD(d):
	sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
	for i in sort_orders:
		print(i[0], i[1])

def Find(string):
	# findall() has been used to match string to url format
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)      
	return [x[0] for x in url]

a = input("enter the topic: ")
subm(a)
# print(b)
c = keyRead()
# print(type(splt(c)))
d = splt(c)
# print(d)
sortD(d)
# print(f)
