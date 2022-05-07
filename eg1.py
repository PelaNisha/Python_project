import requests
import os 
import json


bearer_token = os.environ.get("BEARER_TOKEN")
user_agent = os.environ.get("User-Agent")

def read_file(file):
	with open(file, 'r') as f:
		data = json.loads(f.read())
		return data
		
def get_guest_token():

	url = "	https://api.twitter.com/1.1/guest/activate.json"
	Headers = {"Authorization":bearer_token, 'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0','content-type':'application/x-www-form-urlencoded'}
	
	response = requests.post(url, headers=Headers)
	b = response.json()
	token = b['guest_token']
	return token


def get_info():	
	token = read_file('token.json')
	url = 'https://twitter.com/i/api/graphql/Bhlf1dYJ3bYCKmLfeEQ31A/UserByScreenName?variables={"screen_name":"narendramodi","withSafetyModeUserFields":true,"withSuperFollowsUserFields":true}'
	Headers = {"Authorization":bearer_token,"User-Agent":user_agent,"x-guest-token" : token}
	response = requests.get(url, headers=Headers)
	if response.status_code != 200:
		print("hello")
		token = get_guest_token()
		f = open('token.json', 'r+')
		f.truncate(0) 
		save_to_file(token, 'token.json')
		get_info()
		
	# print("Status Code", response.status_code)
	return response.json()


def save_to_file(final_result,filename):
	with open(filename, "w+") as f:
		json.dump(final_result, f, indent = 2)


def get_user_data(x):
	y = x['data']['user']['result']['legacy']
	output = {'created at':y['created_at'], "description":y["description"],"followers_count":y["followers_count"],
			 "friends_count":y[ "friends_count"],"location":y["location"],"name":y["name"],}
	return output


x = get_info()
o = get_user_data(x)
save_to_file(o, 'file.json')
# get_guest_token()
