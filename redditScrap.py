import praw
import json
from pprint import pprint

id = "the id"
secret = "the secret key"
ps= "Your password here"
ua = "Your app name"
name = "your Username"

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent= ua, username= name, password = ps)

#see all the properties of data
# subred = reddit.subreddit("learnpython")
# hot = subred.hot(limit=10)
# x = next(hot)
# print(dir(x))

# comment reply as a bot
# for submission in subred.hot(limit = 10):
#     for comment in submission.comments:
#         if hasattr(comment, "body"):
#             comment_lower = comment.body.lower()
#             if "is" in comment_lower:
#                 print(submission.url)
#                 # print(comment.body)
#                 comment.reply("This is a reply from another puppet")
#                 # time.sleep(660) ##to delay the next comment reply

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
