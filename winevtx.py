import re
result = {'EventID':[],'TargetUserName':[],'IpAddress':[],'TimeCreated':[]}
EventID_regex = '\<EventID Qualifiers\=\"\"\>(\d*?)\<\/EventID\>'
TargetUserName_regex = '\<Data Name\=\"TargetUserName\"\>(.*?)\<\/Data\>'
IpAddress_regex = 'Data Name\=\"IpAddress\"\>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\<\/Data\>'
TimeCreated_regex = '\<TimeCreated SystemTime\=\"(.*?)\"\>\<\/TimeCreated\>'

def Get_EventID(f):
    for i in f:
        i = i.strip()
        # print i
        EventIDs = re.findall(EventID_regex,i)
        for EventID in EventIDs:
            EventID = EventID
            result['EventID'].append(EventID)


def Get_TargetUserName(f):
    for i in f:
        i = i.strip()
        # print i
        TargetUserNames = re.findall(TargetUserName_regex,i)
        for TargetUserName in TargetUserNames:
            if TargetUserName != None:
                TargetUserName = TargetUserName
                result['TargetUserName'].append(TargetUserName)


def Get_IpAddress(f):
    for i in f:
        i = i.strip()
        # print i
        IpAddresss = re.findall(IpAddress_regex,i)
        for IpAddress in IpAddresss:
            if IpAddress != None:
                IpAddress = IpAddress
                result['IpAddress'].append(IpAddress)


def Get_TimeCreated(f):
    for i in f:
        i = i.strip()
        # print i
        TimeCreateds = re.findall(TimeCreated_regex,i)
        for TimeCreated in TimeCreateds:
            if TimeCreated != None:
                TimeCreated = TimeCreated
                result['TimeCreated'].append(TimeCreated)



with open('security.xml') as f:
    Get_EventID(f)

with open('security.xml') as f:   
    Get_TargetUserName(f)

with open('security.xml') as f:   
    Get_IpAddress(f)

with open('security.xml') as f:   
    Get_TimeCreated(f)


# result = {'EventID':['4625','4624','1111'],'TargetUserName':['Administrator','test','qqqq'],'IpAddress':['1','2','3'],'TimeCreated':['a','b','c']}    
for i in range(len(result['EventID'])):
    if result['EventID'][i] == '4624':
        print result['EventID'][i] + '|' + result['TargetUserName'][i] + '|' + result['IpAddress'][i] + '|' + result['TimeCreated'][i]

