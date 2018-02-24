import socket
import sys
def SubDomain():
    domain = sys.argv[1]
    with open('sub.txt') as sub:
        for subs in sub:
            subdomain = str(subs.strip()) + '.' + domain
            # print subdomain
            # print subs
            try:
                subconnect = socket.gethostbyname_ex(subdomain)
                print subconnect[0] + ':' + subconnect[2][0]
            except:
                pass
    

SubDomain()
