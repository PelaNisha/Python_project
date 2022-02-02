import praw
import json
from pprint import pprint

id = "_A9_qXJrlNxXExhn-ZK8RQ"
secret = "VD0ySjDluZgk74q00tGe_HX-whWZwg"
ps= ""
ua = "first_app"
name = "__special"

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