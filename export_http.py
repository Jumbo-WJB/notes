from libnmap.parser import NmapParser
nmap_report = NmapParser.parse_fromfile('nmap.xml')
urls = [ (b.service + b.tunnel).replace('sl','') + '://' + a.address + ':' + str(b.port) + '/' for a in nmap_report.hosts for b in a.services if b.open() and b.service.startswith('http') ]
for x in urls:
    print x
