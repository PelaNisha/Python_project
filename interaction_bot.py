"""Program to scrape the comments and obtain the user interaction on a comment
about who replied to whom.
"""

# modules used
import validators
from collections import Counter
from distutils import filelist
from nltk.corpus import stopwords 	
import nltk
import praw
import os
import json
import re # regular expression
from urllib.parse import urlparse 	


# bot id and other credentials
id = ""
secret = ""
ps= ""
ua = ""
name = ""


reddit = praw.Reddit(client_id = id,client_secret = secret,
					user_agent= ua,username= name, password = ps)


 
# function that collects url and comments from subreddit into list and string resp.
def commenters_names(topic):
	authors_dict = {}		
	final_list = []
	original_comment_author = []
	replied_comment_author = []

	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit = 3):
		print("url: ", submission.url)
		for comment in submission.comments[:10]:
			if hasattr(comment, "body"):
				comment_author = comment.author
				# print(comment_author)
				if comment_author not in original_comment_author:
					authors_dict['comment author'] = str(comment_author)
					original_comment_author.append(str(comment_author))
					final_list.append(authors_dict)
					
				for reply in comment.replies:
					# print(reply.author)
					
					replied_comment_author.append(str(reply.author))
				authors_dict['repliers'] = replied_comment_author
				replied_comment_author =[]
				authors_dict = {}

	with open(topic+".json", "w+") as f:
		json.dump(final_list, f, indent = 2)

topic = input("Enter the topic: ")
commenters_names(topic)
