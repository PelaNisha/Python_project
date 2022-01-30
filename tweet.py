import requests
from pprint import pprint

headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAACVqYgEAAAAAAMiRdOfcwm2QtKD1GBxBBhSmN1I%3D0nqn4wxKzg2vERilnjEo0tXCt2oRcGeJAA8yBMsbi7RY0scI3N"}

response = requests.get('https://api.twitter.com/2/spaces/search?query=hello&space.fields=title,host_ids', headers=headers)

a = pprint(response.json())
pprint(a)