import re
mail = open('mail2.txt','r')  //mail2.txt为杂乱的，复制下来的邮箱记事本
key = r'<(.*?)>'
for m in mail:
	m = m.strip()
#	print m
	q = re.findall(key,m)
	for w in q:
		print w
		
		
		
		
		
哪里用到，比如，我们用foxmail进入了某个邮箱，可是不是qq exmail，不能导出通讯录，咋办？只能一个一个手动的从发件箱，收件箱里把邮件一个一个的抄到记事本里，然后抄完，记事本里肯定是乱糟糟的，里面不仅有我们需要提炼出来的邮箱，格式为xxxx@xxx.com，还有姓名，符号等杂七杂八的东西，那么，上面的程序可以帮助你。：）
