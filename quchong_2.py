yuan = open('360webscan_dic+anquan_dic.txt','r')
baocun = open('360webscan_dic+anquan_dic_ok.txt','w')
for y in yuan:
	y = y.strip()
	if y[0] != '/':
		baocun.write('/' + y + '\n')
	else:
		baocun.write(y + '\n')
    


//这里https://github.com/Jumbo-WJB/notes/blob/master/quchong_1.py应该把所有的字典都去掉了斜杠/，然后去重，那么去重以后呢，我发现如果字典里没有/的话，御剑无法扫，那么就加上/
