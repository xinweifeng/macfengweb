#!/usr/bin/python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import web
urls = (
  "", "reblog",
  "/(.*)", "blog"
)
# render = web.template.render('templates/')
class reblog:
    def GET(self): raise web.seeother('/')

class blog:
    def GET(self, name):
        raise web.seeother('http://www.macfeng.net/')
# render.hello(name)
                
app_blog = web.application(urls, globals())
# app_hello = web.application(urls, globals())