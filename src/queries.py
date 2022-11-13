## IMPORTING LIBRARIES
if "requests" not in dir():
    import requests
if "urllib" not in dir ():
    import urllib.parse
from dotenv import load_dotenv
if "os" not in dir():
    import os
if "datetime" not in dir():
    import datetime
from unidecode import unidecode

##### GETTING PASSWORDS

env_path = (os.path.join("", ".env"))
load_dotenv(env_path)
GP = os.getenv("THE_GUARDIAN")

### THE GUARDIAN REQUESTS

def guardian_get_tag(name):
    """
    Gets the Guardian tags id for a given query
    Arguments:
        name: str. query to retrive the tag id
    Returns:
        a string with the tag id
    """
    #validating input
    if type(name) != str:
        print("The function only accept strings")
        return None
    # setting request
    url = 'https://content.guardianapis.com/tags?'
    parameters = {
        'api-key': GP,
        'q': name,
    }
    url = url + urllib.parse.urlencode(parameters)
    try:
        response = requests.get(url)
    except:
        print("Network error please check your internet connection")
    if response.status_code == 200:
        response = response.json()
        results = response['response']['results']
        if results:
            for e in results:
                if unidecode(name.lower(), "utf-8") in unidecode(e['webTitle'].lower(), "utf-8"):
                 return e['id']
            print(f"{name} tag id not found")
            return None
        else:
            print(f"{name} tag id not found")
            return None
    else: 
        print(f"Unable to retrieve the tag id for {name}: Error {response.status_code}: {response.text}")  
        return None

def get_guardian_articles(query, datefrom=None, dateto=None):
    articles = []
    tag = guardian_get_tag(query)
    if not dateto:
        d = datetime.datetime.now()
        dateto = f"{d.year}-{d.month}-{d.day}"
    if not datefrom:
        d = datetime.datetime.now()
        datefrom = f"{d.year-2}-{d.month}-{d.day}"

    url = 'https://content.guardianapis.com/search?'
    parameters = {
        'api-key': GP,
        'tag': tag,
        'from-date': datefrom,
        'to-date': dateto,
        'order-by': 'newest',
        'page':1,
        'use-date':'published',
        'page-size': 100
    }
    if not parameters['tag']:
        del parameters['tag']
        parameters['q'] = query
    url2 = url + urllib.parse.urlencode(parameters)
    try:
        response = requests.get(url2)
    except:
        print("Network error please check your internet connection")
    if response.status_code == 200:
        response = response.json()
        pages = response['response']['pages']
        if pages < 10 and not parameters['q']:
            del parameters['tag']
            parameters['q'] = query
            url2 = url + urllib.parse.urlencode(parameters)
            try:
                response = requests.get(url2)
                if response.status_code == 200:
                    response = response.json()
                    pages = response['response']['pages']
                else: 
                    print(f"Unable to retrieve articles from {query}: Error {response.status_code}: {response.text}")
                    return None
            except:
                print("Network error please check your internet connection")
                return None
        results = response['response']['results']
        for e in results:
            art = {
                'date': e['webPublicationDate'],
                'title': e['webTitle'],
                'person': query
            }
            articles.append(art)
        for i in range(2, pages+1):
            parameters['page'] = i
            url2 = url + urllib.parse.urlencode(parameters)
            try:
                response = requests.get(url2)
                if response.status_code == 200:
                    response = response.json()
                    results = response['response']['results']
                    for e in results:
                        art = {
                            'date': e['webPublicationDate'],
                            'title': e['webTitle'],
                            'person': query
                        }
                        articles.append(art)
                else: 
                    print(f"Unable to retrieve articles from page {i} of {query}: Error {response.status_code}: {response.text}")
            except:
                print("Network error please check your internet connection")
    else: 
        print(f"Unable to retrieve articles from {query}: Error {response.status_code}: {response.text}")  
        return None
    return articles
