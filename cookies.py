import requests
import re
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')                 //设置编码好把内容写入文件中
csv = open('lianxiren.txt','w')
for i in range(23):                    //循环次数
	print i
	url = "http://10.2.1.2:8080/manager/securityPolicy.do?method=detailed&userid=%s" %i   //i是循环值
	key = r"<td class=\"pvalue\">(.*?)<\/td>"
	cookies = {'JSESSIONID':'abcmnXlTUM9Z98bfQ_skv','testBanCookie':'test'}         //多个cookie值用逗号隔开
	get = requests.get(url,cookies = cookies)
	print get.text
	body = re.findall(key,get.text)
	for b in body:
		print b
		csv.write(b + '\n')            //末尾回车防止杂乱
