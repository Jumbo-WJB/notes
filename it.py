#coding=utf-8

import itchat
from itchat.content import *

@itchat.msg_register([TEXT], isGroupChat=True)
def xyz_reply(msg):
    group_list = [u'徐汇七大霸王']
    group_name = []
    for group in group_list:
        chat = itchat.search_chatrooms(name=group)
        # print chat[0]['UserName']
        # print chat
        if len(chat) > 0:
            group_name.append(chat[0]['UserName'])
    #         print chat[0]['UserName']
    # text = msg['Content']

    print msg['User']['NickName']
    if msg['User']['NickName'] == u'徐汇七大霸王':
        text = msg['Content']
        itchat.send('%s'%(text), toUserName=chat[0]['UserName'])





if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
