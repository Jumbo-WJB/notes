a = open('mail.txt','w')
x = open('xingming500.txt','r')
for f in x:
	f = f.strip()
	print f + '@chinabaiker.com'
	print>>a,f + '@chinabaiker.com'
	
	
	
zhangnan@chinabaiker.com
liuguizhen@chinabaiker.com
liuyu@chinabaiker.com
liujianjun@chinabaiker.com
zhangshuying@chinabaiker.com
lihongxia@chinabaiker.com
zhaoxiuying@chinabaiker.com
libo@chinabaiker.com
wangli@chinabaiker.com
zhangrong@chinabaiker.com
