#coding = utf-8
import socket
ports = [21,80,443,143,445]
def port_scan(host,port):
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket()
        s.connect((host,port))
        print '[+] %s open' % port
    except:
        print '[-] %s close' % port
        pass
for port in ports:

    port_scan('192.168.1.102',port)
