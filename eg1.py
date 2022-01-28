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
        return {'type': 'success', 'data': data}

    except requests.exceptions.RequestException as e:  
        return {'type': 'error', 'error': 'Unknown error occured'}

def search_item(arg):
    item = arg+".json"
    if os.path.isfile(item):
        with open(item, 'r') as f:
            data = json.loads(f.read())
            return {'type': 'success', 'data': data}
    else:
     return append_json(arg)   

def parsh_json(response,a):
    lst=[]
    for item in response["data"]:
        for inde in a:
            char ={
                a['{inde}']:item[inde],
                # 'pub-data': item['publishOn'],
                # 'author':item['author']['name'],
            }
        lst.append(char)
    return lst

def append_json(a):
    mainList = []
    b = inp()
    for n in range (1,4):    
        url = "https://bg.annapurnapost.com/api/tags/news?page="+str(n)+"&per_page=20&tag="
        result = search(url,a)
        with open(a+".json", "w+") as f:
            mainList.extend(parsh_json(result,b))
            json.dump(mainList, f, indent = 4)
    return {'type': 'success', 'data': mainList}      


def inp():
    a = []
    number = input("enter the number of items you want to get info")
    for i in range(1,int(number)):
        ele = input()
        a.append(ele)
    return a   

argument = input("Enter the search item\n")
p =search_item(argument)
print(p)
