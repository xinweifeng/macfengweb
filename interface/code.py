#!/usr/bin/python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
#import time
import web
#import json
import json

from classdefine import MySysConfig
## config
#debug on/off release to set False
web.config.debug = True


urls = (
        '/test','test',
        '/(.*)', 'default',
)

class test:
        def GET(self):
                dict = {"name":"macfeng.net","age":1}
                web.header('Content-Type', 'application/json')
                return json.JSONEncoder().encode(dict)
                

class default:
        def GET(self,path):
                web.header('Content-Type', 'application/json')
                return "{\"firstName\": \"John\",\"lastName\": \"Smith\",\"age\": 25,\"path\":\"" + path +"\"}"

app = web.application(urls, globals())
application = app.wsgifunc()

