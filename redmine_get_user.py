import requests
import re
import time
number = range(1,66)
for n in number:
    url = 'http://chinabaiker.com/redmine/users/%s' % n
    #print n
    #print url
    headers = {"cookie":"_redmine_session=redminecookies"}
    geturl = requests.get(url,headers=headers)
    #time.sleep(1)
    #print geturl.content
    content1 = geturl.content
    regex = '\"mailto:(.*?)\"\>'
    key = re.findall(regex,content1)
    for k in key:
        print k
        if k == None:
            pass
