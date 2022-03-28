"""Program to scrape the comments and obtain the user interaction on a comment
about who replied to whom, the comment and its keyword
"""

# modules used
from test import * # file as a package to impoet functions
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
	final_list = []
	subred = reddit.subreddit(topic)
	for submission in subred.hot(limit = 3):
		for comment in submission.comments[:10]:
			if hasattr(comment, "body"):
				original_comment_author = []
				replied_comment_author = []
				authors_dict = {}	
				comment_author = comment.author.name
				comment_body = comment.body

				if comment_author not in original_comment_author:
					authors_dict['comment author'] = comment_author
					authors_dict['comment body'] = comment_body
					original_comment_author.append(comment_author)
										
				for reply in comment.replies:
					replied_comment_author.append(reply.author.name)

				authors_dict['repliers'] = replied_comment_author
				authors_dict['repliers_count'] = len(replied_comment_author)
				final_list.append(authors_dict)

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
# 		url_ = []
# 		str_ = "" # concat the string to make a large a comment 
# 		for i in range(0,len(data)):
# 			for word in data[i]['comment body'].split():
# 				if is_url(word):
# 					url_in_comment = urlparse(word)
# 					url_hostname = url_in_comment.hostname
# 					if url_hostname not in url_:
# 						url_.append(url_hostname)
# 				if word not in stop_words:
# 					word = word.lower()
# 					str_.append(word)
# 		x =  count_keywords(topic, url_, str_)
# 		pprint(x)
	else:
		return commenters_names(topic)  


# Count the number of times a phrase was repeated
def count_keywords(topic, url_list, final_string):
	ngrams = list(nltk.ngrams(final_string.split(), n=2))
	ngrams_count = {i : ngrams.count(i) for i in ngrams}

	return sort_keywords_count(topic, url_list, ngrams_count)


topic = input("Enter the topic: ")
if_file(topic)
