import requests
import json
from pprint import pprint
url = "https://www.trustpilot.com/_next/data/categoriespages-consumersite-1638/categories/bank.json?page="

mst =[]

def search(finUrl):
	timeout = 5
	res= requests.get(finUrl, timeout=timeout)
	data = res.json()	
	return data

			
def fs():
	for i in range(2,6):
		final_url = url + str(i)+"&categoryId=bank"
		dat = search(final_url)
		for k in  dat['pageProps']['businesses']['allBusinessUnits']['businessUnits']:
			char = {
				'name':k['displayName'],
				'trustScore':k['trustScore'],
				'numberOfReviews':k['numberOfReviews'],
				'stars':k['stars'],
			}
			mst.append(char)
# 		if you want to filter with some conditions
# 		if k['numberOfReviews']>1000 and k['stars']>4:
# 			char = {
#				'name':k['displayName'],
# 				'trustScore':k['trustScore'],
# 				'numberOfReviews':k['numberOfReviews'],
# 				'stars':k['stars'],
# 				}
# 			mst.append(char)
	return mst
fin = fs()
pprint(fin) 
