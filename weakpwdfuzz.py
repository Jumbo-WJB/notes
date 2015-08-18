import sys
key = sys.argv[1]
dic = open('dic.txt','r')
suc = open('ok.txt','w')
for a in dic:
    a = a.strip()
    a = a.replace("%username%",key)
    print a
    suc.write(a+'\n')
dic.close()
suc.close()




使用方法
python weakpwdfuzz.py chinabaiker
-------
chinabaiker
chinabaiker1
chinabaiker12
chinabaiker123
chinabaiker123
--------
dic.txt放模版字典，本目录有个规则，可以直接使用
