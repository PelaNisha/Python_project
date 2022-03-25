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
id = "_A9_qXJrlNxXExhn-ZK8RQ"
secret = "VD0ySjDluZgk74q00tGe_HX-whWZwg"
ps= "songjoongki"
ua = "first_app"
name = "__special"


reddit = praw.Reddit(client_id = id,client_secret = secret,
					user_agent= ua,username= name, password = ps)


 
# function that collects url and comments from subreddit into list and string resp.
def commenters_names(topic):
	comment_replies = []
	original_comment = []
	original_comment = []

	original_comment_author = []
	replied_comment_author = []


	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit = 3):
		print("Title: ", submission.title)
		print("url: ", submission.url)
		print("Author: ", submission.author)
		# print("total comments: ", submission.num_comments)
		# print("Num of subs: ", submission.subreddit_subscribers)
		# print("Score: ", submission.score)
		for comment in submission.comments[:5]:
			if hasattr(comment, "body"):
				print(comment.author)
				# Check before replying to another comment
				if comment.id not in original_comment:
					original_comment.append(comment.id)
					original_comment_author.append(comment.author)
				else:
					for reply in comment.replies:
						comment.reply_sort = "new"
						comment.refresh()
						replies = comment.replies
					replied_comment_author.append(replies)
					
		print("**************")
		print(original_comment_author)
		print("---------------")
		print(replied_comment_author)
topic = input("Enter the topic: ")
commenters_names(topic)