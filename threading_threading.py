import threading
import Queue



def Getdict():
    pass_dict = open('2.txt','r')
    for password in pass_dict:
        queue.put(password)

        
def Reqpost():
    while True:
        mutex.acquire()
        password = queue.get()
        print password
        mutex.release()
        queue.task_done()    





queue = Queue.Queue()
mutex = threading.RLock()
threadlist = [threading.Thread(target=Reqpost) for x in xrange(10)]
for t in threadlist:
    t.daemon = True
    t.start()

Getdict()
queue.join()
