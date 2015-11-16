#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
import sys
import requests
data = "domain=" + sys.argv[1] + "&b2=1&b3=1&b4=1"
test = open('test.txt','w')
key = r"value=\"(.+?)\"><input"
headers = {"Content-type":"application/x-www-form-urlencoded","Referer":"http://i.links.cn/subdomain/"}
go = requests.post("http://i.links.cn/subdomain/",data=data,headers=headers)
response = re.findall(key,go.content)
for r in response:
	print r
	
	
	
	
---------------------------------
requests.post参数，如果没有定义data=,headers=多少的话，只能有两个参数
---------------------------------
