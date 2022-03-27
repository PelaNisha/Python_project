"""Program to scrape the comments and obtain the user interaction on a comment
about who replied to whom.
"""

# modules used
from test import *
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


reddit = praw.Reddit(client_id = id_,client_secret = secret,
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
				comment_body = comment.body
				if comment_author not in original_comment_author:
					authors_dict['comment author'] = str(comment_author)
					authors_dict['comment body'] = str(comment_body)
					original_comment_author.append(str(comment_author))
					final_list.append(authors_dict)
					
				for reply in comment.replies:
					replied_comment_author.append(str(reply.author))

				authors_dict['repliers'] = replied_comment_author
				authors_dict['repliers_count'] = len(replied_comment_author)
				replied_comment_author =[]
				authors_dict = {}

	li = sorted(final_list, key = lambda i: i['repliers_count'], reverse=True)

	return second_step(li, topic)


def second_step(final_list, top):
	with open(top+".json", "w+") as f:
		json.dump(final_list, f, indent = 2)

# to check is a file is already present for respective subreddit
def if_file(topic):
	item= topic+'.json'
	if os.path.isfile(item):
		data =  parse_(item)
		pprint(data)
	else:
		return commenters_names(topic)  

topic = input("Enter the topic: ")
if_file(topic)
