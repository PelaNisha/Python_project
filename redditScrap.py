import praw
import json
from pprint import pprint

id = "the id"
secret = "the secret key"
ps= "Your password here"
ua = "Your app name"
name = "your Username"

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)

def search_for(item, l):
	# options = ['hot', 'new', 'controv', 'top', 'gildsed']
	# o = options[choice-1]
	# print(o)
	lst=[]
	for i in reddit.subreddit(item).hot(limit=l):
		char ={
			'title':i.title,
			'url':i.url,
		}
		lst.append(char)
	return lst	

search_item = input("Enter the item to search: ")
search_limit = int(input("Enter the limit: "))

result = search_for(search_item, search_limit)
pprint(result)
# search_for(search_item, search_limit)
