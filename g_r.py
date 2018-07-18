#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:Jumbo
#website:www.chinabaiker.com
import grequests
import requests
import os
ls = os.linesep



def dir_scanner(dicts):
    body = [grequests.get('http://music.163.com' + dict) for dict in dicts]
    resps = grequests.map(body,size=10)
    # print resps
    for resp in resps:
        if resp.status_code == 200 and ('404' in resp.content) == False:
            print resp.url
            result_list.append(resp.url + ls)

# def Get_sfx():
#     suffix = ['.orig', '~', '.~', '.original', '.swo', '.swp', '.txt', '.new', '.7z', '.tar.xz', '.tar.gz', '.rar', '.save', '.zip', '.bak', '.old']
#     for sfx in suffix:
#         sfx_body = [grequests.get(sfx_url.strip() + sfx) for sfx_url in result_list]
#         sfx_resps = grequests.map(sfx_body,size=10)
#         # print sfx_resps
#         for sfx_resp in sfx_resps:
#             if sfx_resp.status_code == 200 and ('404' in sfx_resp.content) == False:
#                 result_list.append(sfx_resp.url + ls)

    


def Get_sfx():
    suffix = ['.orig', '~', '.~', '.original', '.swo', '.swp', '.txt', '.new', '.7z', '.tar.xz', '.tar.gz', '.rar', '.save', '.zip', '.bak', '.old']
    for sfx_urls in result_list:
        for sfx in suffix:
            sfx_url = sfx_urls.strip() + sfx
            # print sfx_url
            sfx_body = requests.get(sfx_url)
            if sfx_body.status_code == 200 and ('404' in sfx_body.content) == False:
                print sfx_body.url 
            #     result_list.append(sfx_body.url + ls)
    

def save_file():
    with open('saveok.txt', 'w') as f:
        f.writelines(set(result_list))
    f.close()


if __name__ == "__main__":
    ok_list = []
    result_list = []
    dicts = []
    for dict in open('php.txt','r'):
        dict = dict.strip()
        dicts.append(dict)
    dir_scanner(dicts)
    Get_sfx()
    save_file()
    
print '----end-----'
