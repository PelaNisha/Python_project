"""Program to scrape the comments and urls from a subreddit using 
reddit bot and python to extract the keywords and keyword prase
"""

# Modules used
from collections import Counter
from distutils import filelist
from nltk.corpus import stopwords 	
import nltk
import praw
import os
import json
import re 
from urllib.parse import urlparse

# Bot id and other credentials
id = ""
secret = ""
ps= ""
ua = ""
name = ""


reddit = praw.Reddit(client_id = id,client_secret = secret,
		     user_agent= ua,username= name, password = ps)


stop_words = set(stopwords.words('english'))

# Function that collects url and comments from subreddit into list and string resp.
def collect_url_Comment(topic):							
	comment_lower = ""
	url = []
	sub_reddit = reddit.subreddit(topic)

	for submission in sub_reddit.hot(limit=5):
		url_in_post = submission.url
		parse_url = urlparse(url_in_post)
		host_name = parse_url.hostname
		if host_name not in url:
			url.append(host_name)
		for word in submission.title.split():
			if word not in stop_words:
				word = word.lower()
				comment_lower = comment_lower+" "+word

		for comment in submission.comments[:5]:
			if hasattr(comment, "body"):
				for word in comment.body.split():
					if is_url(word):
						url_in_comment = urlparse(word)
						url_hostname = url_in_comment.hostname
						if url_hostname not in url:
							url.append(url_hostname)
					elif word not in stop_words:
						word = word.lower()
						comment_lower = comment_lower+" "+word

	return count_keywords(topic, url, comment_lower)


# Check if a string is a url
def is_url(string):
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+\
	[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+\
	(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)     

	return [x[0] for x in url]


# Check if a file is already present for respective subreddit
def if_file(topic):
	item= topic+'.json'
	if os.path.isfile(item):
		return parse(item)
	else:
		return collect_url_Comment(topic)   
	

# Count the number of times a phrase was repeated
def count_keywords(topic, url_list, final_string):
	ngrams = list(nltk.ngrams(final_string.split(), n=2))
	ngrams_count = {i : ngrams.count(i) for i in ngrams}

	return sort_keywords_count(topic, url_list, ngrams_count)


# Sort the keywords phrase in descending order
def sort_keywords_count(topic, url_list, keyword_count):	
	item = topic+".json"	
	words_dict = {}		
	url_dict = {}			# To combine the urls from post and comments into a dict
	url_dict['url'] = url_list				
	final_list = []
	final_list.append(url_dict)
	sort_orders = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)

	for i in sort_orders[:20]:
		words_dict['words'] = i[0]
		words_dict['count'] = i[1]
		final_list.append(words_dict)
		words_dict = {}
		
	with open(item, "w+") as f:
		json.dump(final_list, f, indent = 2)

	return final_list


# Parse the file for subreddit
def parse(top):
	print("File Present!")
	with open(top, 'r') as f:
		data = json.load(f)
	return data

	
# Call this function to return the urls from the file
def return_urls(data):
	return data[0]['url']


# Call this function to return the keyword phrases from the file
def return_words(data):
	for i in range(1, len(data)):
		print(data[i])
	return "End of file"	
