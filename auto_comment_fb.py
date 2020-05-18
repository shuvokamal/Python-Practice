import http.client
import  urllib
from bs4 import BeautifulSoup
import os
import json
import time

from pip._vendor.msgpack.fallback import xrange

access_token = 'EAACB2SY51FoBAC0yczZB2Jtv939MA5eitA2WzAJ6TBsMfUaOkmxaOycM4PmyKKSa5gR6gneJwWJTJzgQgIDxHPuKgdfrnrC9VeyQVqR7hnRsDat5hV5ZBjSLWVbfL6cstJpXaMiXHMBP8EXtGOLZAOyXLZCBmR1qPswnDxEKcCRo6FW82Dasg8t1ifvbj8WZBg0SiXwwJNwZDZD'
conn = http.client.HTTPSConnection("graph.facebook.com")
print('Please Wait!')


def comment(url):
    connect = http.client.HTTPSConnection("graph.facebook.com")
    connect.request("GET", url)
    for x in xrange(1000):
        print
        'commenting %d ' % x
        path = '/' + '1307427112785568' + '/comments'
        param_data = {'format': 'json',
                      'message': 'ki obostha bhai? Python coding kaam kore kina dekhtesi! :P',
                      'access_token': access_token
                      }
        connect = http.client.HTTPSConnection("graph.facebook.com")
        connect.request("POST", path, urllib.parse.urlencode(param_data), {})
        time.sleep(0.09)


url = '/1307427112785568'
comment(url)
print('DONE!')