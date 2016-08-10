a = open('asp.txt','r')
dd = open('aspok.txt','w')
for b in a:
    if b[0] == '/':
        b = b[1:]
        cc = b.strip()
        print cc
        dd.write(cc + '\n')
    else:
        cc = b.strip()
        print cc
        dd.write(cc + '\n')

容我用笨的方式进行：
因为有的时候/admin和admin目录是一样的效果，用平常的去重软件是无法去重的，我就先把开头为/的给删掉，那么剩下的就全部是开头没有/的，然后用linux的uniq去重了。。。。
