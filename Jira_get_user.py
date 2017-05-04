import requests
import re
users = []
url = "http://www.chinabaiker.com/secure/BrowseProjects.jspa?selectedCategory=all"
body = requests.get(url).content
regex = "name=(.*?)\""
keyword = re.findall(regex,body)
for key in keyword:
	# print key
	users.append(key)

user = set(users)	
# print user
for u in user:
	print u
