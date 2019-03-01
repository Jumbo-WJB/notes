import requests
from bs4 import BeautifulSoup
#(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,4})
def XHRe():
    with open('urls.txt') as urls:
        for url in urls:
            url = url.strip()
            url = 'http://' + url
            try:
                get = requests.get(url,timeout=5).text
                # print(get)
                soup = BeautifulSoup(get,'lxml')
                print(url,soup.title)
            except Exception as e:
                print(e)
                pass

XHRe()
