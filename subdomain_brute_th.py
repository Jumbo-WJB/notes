//python subdomain_brute_th.py chinabaiker.com
import socket
import sys
import threading
import Queue

class SubDomainBrute(object):
    def __init__(self,domain):
        self.domain = domain
        self.queue = Queue.Queue()


    def open_dict(self):
        for sub in open('sub.txt', 'r'):
            self.queue.put(sub.strip())




    def run(self):
        while not self.queue.empty():
            domain  = self.queue.get()
            self.domainbrute(domain)



    def domainbrute(self, domain):
        mutex.acquire()
        subdomain = domain + '.' + self.domain
        try:
            subconnect = socket.gethostbyname_ex(subdomain)
            print subconnect[0] + ':' + subconnect[2][0]
            mutex.release()
        except:
            pass

subdomain = sys.argv[1]
work = SubDomainBrute(subdomain)
mutex = threading.Lock()
work.open_dict()
for x in range(10):
    t = threading.Thread(target=work.run)
    t.start()
    t.join()
