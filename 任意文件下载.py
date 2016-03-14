//任意文件下载，比如www.baidu.com/down.php?id=1

#coding= utf-8
import urllib
import requests
import re
i = 72
#print i
url = "http://www.baidu.com:8000/Liems/ExportWord?pkValue=%s" %i
#outfile = open(filename,'wb')
#outfile.write(result.read())
#outfile.close()
#print url
#urllib.urlretrieve(url,filename)
res = urllib.urlopen(url)
#print res
#print res.info()
aaaa = res.info()
print aaaa
filenameRe = re.compile(r'Content-Disposition: filename=\"(.*?)\"')
filename = re.findall(filenameRe,str(aaaa))
for x in filename:
    print x
    urllib.urlretrieve(url,x)

//这样就可以根据filename，什么文件就以什么文件名保存在本地。
