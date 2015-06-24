import hashlib
y = open('md5test.txt','w')
md5 = hashlib.md5()
a = range(1434958800,1434959220)
for x in a:
	f =  "xsser_TPdqsI_4_" + str(x)
	b = md5.update(str(f))
	c = md5.hexdigest()
	print c
	print>>y,c
