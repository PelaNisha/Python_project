from gettext import find
from html5lib import serialize
import praw
from pprint import pprint
import re #regular expression
from collections import Counter


id = ""
secret = ""
ps= ""
ua = ""
name = ""

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)
topic = 'withyoualways'

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
	for submission in subred.hot(limit=2):
		# print(type(submission))
		for comment in submission.comments:
			if hasattr(comment, "body") and count<10:
				comment_lower = comment.body.lower()
				if Find(comment_lower) :
					with open("myfile.txt", "a+") as file1:
						# Writing data to a file
						file1.write(comment_lower+'\n')
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
	words = a.split()
	word_counts = Counter(words)
	for word, count in sorted(word_counts.items()):
		print('"%s" is repeated %d time%s.' % (word, count, "s" if count > 1 else ""))
	# print(max(count))

	
def Find(string):
	# findall() has been used to match string to url format
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)      
	return [x[0] for x in url]

a = input("enter the topic: ")
subm(a)
# print(b)
c = keyRead()
splt(c)
