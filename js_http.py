#http://tools.sharejs.com/beautify-javascript.html
import re
a = open('1.txt','r')
for b in a:
	# print b
	regex = "\"(\/\w{1,}\/\w{1,}.*)\""
	key = re.findall(regex,b)
	if len(key) > 0:
		print key
