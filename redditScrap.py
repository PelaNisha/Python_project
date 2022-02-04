
import praw
import json
from pprint import pprint
import time

id = "_A9_qXJrlNxXExhn-ZK8RQ"
secret = "VD0ySjDluZgk74q00tGe_HX-whWZwg"
ps= "songjoongki"
ua = "first_app"
name = "__special"

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)

def search_for(item, l):
	lst=[]
	for i in reddit.subreddit(item).hot(limit=l):
		char ={
			'title':i.title,
			'url':i.url,
		}
		lst.append(char)
	return lst	

def comment_reply(topic,word):
    subred = reddit.subreddit(topic)
    for submission in subred.hot(limit = 10):
        submission.upvote()
        for comment in submission.comments:
            if hasattr(comment, "body"):
                comment_lower = comment.body.lower()
                # print(comment_lower)
                if word in comment_lower:
                    print(submission.url)
                    print(comment.body)
                    comment.reply("Reply from a puppet")
                    time.sleep(660)

              

choice = int(input("Enter your option:\n1.scrape data\n2.reply to comment\n"))

if choice == 1:
    search_item = input("Enter the item to search: ")
    search_limit = int(input("Enter the limit: "))
    result = search_for(search_item, search_limit)
    pprint(result)

elif choice == 2:
    topic,wordToSearch = input("Enter the topic and word to search: ").split()
    comment_reply(topic, wordToSearch)    
