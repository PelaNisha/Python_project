import requests
from pprint import pprint

headers = {"Authorization": "Bearer YOUR TOKEN HERE "}

response = requests.get('https://api.twitter.com/2/spaces/search?query=hello&space.fields=title,host_ids', headers=headers)

a = pprint(response.json())
pprint(a)
