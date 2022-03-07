import praw
from nltk.corpus import stopwords 					#import stopwords
import re 								#regular expression
from collections import Counter

id = ""
secret = ""
ps= "s"
ua = ""
name = ""

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)

stop_words = set(stopwords.words('english'))

def search_for(topic): 							#function to return title and url for subreddit posts
	lst=[]
	red = reddit.subreddit(topic)
	for i in red.hot(limit=3):
		char ={
			'title':i.title,
			'url':i.url,
		}
		lst.append(char)
	return lst	

def subm(topic):							#function to write the 10 comments from each post to a file
	count = 0							#and convert comments to a large string
	comment_lower = ""
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit=2):
		for comment in submission.comments:
			if hasattr(comment, "body") and count<10:
				comment_lo = comment.body.lower()
				with open("myfile.txt", "a+") as file1:
					comment_lower = comment_lower + " "+comment_lo
					file1.write(comment_lower)
					count= count+1
		print("*****************")
		count=0

def keyRead():								#function to convert the string to a list of items
	li = []
	with open("myfile.txt", "r+") as file1:
		# print(file1.read())
		li.append(file1.read())
	return (str(li))

def splt(a):								#function to create the dict of words and their count
	my_dict = {}
	words = a.split()
	word_counts = Counter(words)
	for word, count in sorted(word_counts.items()):
		if word not in stop_words:
			my_dict[word] = [count]
	return my_dict
	
def sortD(d):								#function to sort dict by value in descending order
	sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
	for i in sort_orders:
		print(i[0], i[1])

def Find(string):							#funtion to return is a comment contains a url
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)      				# findall() has been used to match string to url format
	return [x[0] for x in url]

subr = input("enter the topic: ")					#input the subreddit
subm(subr)								#parse top 10 comments and convert them to single string
str_list = keyRead()							#create list of string item
d = splt(str_list)							#return dict with keys and their count
sortD(d)								#print the keys with value in descendin order
