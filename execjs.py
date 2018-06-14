#! /usr/bin/env python
# _*_  coding:utf-8 _*_

import execjs

def Encode(str):
    with open ('md5.js','r') as js:
        source = js.read()
        getpass = execjs.compile(source)
        password = getpass.call('hex_md5',str)
        print password

if __name__ == '__main__':
    with open ('pass.dict') as passwd:
        for ps in passwd:
            Encode(ps)
