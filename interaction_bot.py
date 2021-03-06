"""Program to scrape the comments and obtain the user interaction on a comment
about who replied to whom, the comment and its keywords
"""


# modules used
from test import * # file as a package to import functions
import praw	
import os
import json
from pprint import pprint
	
	
# bot id and other credentials
id_ = ""
secret = ""
ps= ""
ua = ""
name = ""


reddit = praw.Reddit(client_id = id_, client_secret = secret,
		     user_agent= ua, username= name, password = ps)


stop_words = set(stopwords.words('english'))


# Make a list of dicts for comment author, repliers, repliers count and comment body
def commenters_info_and_comment(topic):
	final_list = []
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit = 3):
		for comment in submission.comments[:10]:
			if hasattr(comment, "body"):
				replied_comment_author = []
				authors_dict = {}	
				comment_author = comment.author.name
				comment_body = comment.body
				authors_dict['comment author'] = comment_author
				authors_dict['comment body'] = comment_body

				for reply in comment.replies:
					replied_comment_author.append(str(reply.author))
				authors_dict['repliers'] = replied_comment_author
				authors_dict['repliers_count'] = len(replied_comment_author)
				final_list.append(authors_dict)
				
	li = sorted(final_list, key = lambda i: i['repliers_count'], reverse=True) # sort the dict acc to repliers_count

	return dump_json(li, topic)


# function to scrape the post and comments and save them into the file
def scrape_data(topic):
	item = topic+ '.json'
	if os.path.isfile(item): 
		return parse_(item)
	else:	
		final_list = []		
		submission_post = []
		sub_reddit = reddit.subreddit(topic)
		for submission in sub_reddit.hot(limit=3):
			word_dict = {}
			submission_post = submission.title
			word_dict['post'] = submission_post		
			comment_body = []
			for comment in submission.comments[:5]:	
				if hasattr(comment, "body"):
					comment_body.append(comment.body)
			word_dict['comments'] = comment_body
			final_list.append(word_dict)

		with open(topic+".json", "w+") as f:
			json.dump(final_list, f, indent = 2)
		return final_list		


# function to scrape the respective file and analyze the comments

# function to scrape the respective file and analyze the comments
def analyze_data(topic): # analyze comments
	item = topic+'.json'
	data = []
	if not os.path.isfile(item): 
		data =scrape_data(topic)
	else:
		data= parse_(item)		
	ws =[]
	for post in data:
		for sentence in post['comments']:
			for word in sentence.split():
				ws.append(word)	
	x =  count_keywords(ws)
	return x


# Dump the json response and also print the keywords for comments
def dump_json(final_list, top):
	with open(top+".json", "w+") as f:
		json.dump(final_list, f, indent = 2)
	print("Data Scrapped Successfully!!")


# To check is a file is already present for respective subreddit and 
# Scape the data is file is present
def if_file(topic):
	item = topic+'.json' # Subreddit json file naming format
	if os.path.isfile(item): 
		item_C = topic+"C"+".json" # Wordcount file naming format
		if os.path.isfile(item_C): # If wordcount file is already present then parse from the wordcount file
			parse_(item_C)	
			print("From saved C file")		
		else:
			data =  parse_(item) # parse the subreddit file
			words  =[] # list to store words 
			for i in range(0,len(data)):
				for word in data[i]['comment body'].split():
					if word not in stop_words:
						word = word.lower()
						words.append(word)
			x =  count_keywords(words)
			with open(topic+"C"+".json", "w+") as f: # create a new json file for the wordcount
				json.dump(x, f, indent = 2)
			print("Word Count Done Successfully!!")
	else:
		return commenters_info_and_comment(topic) 

	
# Count the number of times a phrase was repeated
def count_keywords(final_string):
	ngrams = list(nltk.ngrams(final_string, n=2))
	ngrams_count = {i : ngrams.count(i) for i in ngrams}

	return sort_keywords_count(ngrams_count)


# Sort the keywords phrase in descending order
def sort_keywords_count(keyword_count):		
	keywords_dict = {}					
	final_list = []
	sort_orders = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)

	for i in sort_orders[:20]:
		keywords_dict['words'] = i[0]
		keywords_dict['count'] = i[1]
		final_list.append(keywords_dict)
		keywords_dict = {}
	return final_list	
