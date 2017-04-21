count=1
list_1 = []
list_2 = []
with open('cj.txt','r') as f:
	list_1 = f.readlines()
with open('da.txt','r') as f:
	list_2 = f.readlines()
for i in range(len(list_1)):
	if list_1[i] != list_2[i]:
		print count
		count+=1
    
    
    
//file.readlines()直接得到的就是一个列表，无需append
