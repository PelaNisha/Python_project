import requests
import json
import os
from pathlib import Path

def search(URL, a):
    url = URL+a
    timeout = 5
    try:
        response= requests.get(url, timeout=timeout)
        data = response.json()
        # return {'type': 'success', 'data': data}
        return data

    except requests.exceptions.RequestException as e:  
        return {'type': 'error', 'error': 'Unknown error occured'}

def search_item(arg, i):
    item = arg+".json"
    if os.path.isfile(item):
        with open(item, 'r') as f:
            data = json.loads(f.read())
            return {'type': 'success', 'data': data}
    else:
     return append_json(arg,i)   

def parsh_json(response):
    lst=[]
    for item in response["data"]:
        char ={
            'title': item['title'],
            'pub-data': item['publishOn'],
            'author':item['author']['name'],
        }
        lst.append(char)
    return lst

def append_json(a, i):
    mainList = []
    for n in range(1,int(i)+1):    
        url = "https://bg.annapurnapost.com/api/tags/news?page="+str(n)+"&per_page=20&tag="
        result = search(url,a)
        with open(a+".json", "w+") as f:
            mainList.extend(parsh_json(result))
            json.dump(mainList, f, indent = 4)
    return {'type': 'success', 'data': mainList}      


argument = input("Enter the search item\n")
i = input("Enter the number of pages\n")#added page input for user


p =search_item(argument,i)
print(p)
