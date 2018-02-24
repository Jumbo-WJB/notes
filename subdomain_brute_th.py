#python subdomain_brute_th.py chinabaiker.com 50
#author:Jumbo
import socket
import sys
import threading
import Queue

class SubDomainBrute(object):
    def __init__(self,domain,thread):
        self.domain = domain
        self.thread = thread
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

domain = sys.argv[1]
thread = sys.argv[2]
work = SubDomainBrute(domain,thread)
mutex = threading.Lock()
work.open_dict()
for x in range(int(thread)):
    t = threading.Thread(target=work.run)
    t.start()
    t.join()
