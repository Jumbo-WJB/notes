yy = open('2.txt','w')
from libnmap.parser import NmapParser
nmap_report = NmapParser.parse_fromfile('nmap.xml')
for xx in [ [(b.service + b.tunnel).replace('sl',''), a.address, b.port] for a in nmap_report.hosts for b in a.services if b.open() and b.service.startswith('http') ]:
    print xx
    print>>yy,xx
    f = open('2.txt','r')
    a = open('urlok.txt','w')
    for x in f:
        print>>a,x.replace("', '","://").replace("', ",":")
