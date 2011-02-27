#!/usr/bin/python
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)

import web
#import json
from twitter import Twitter,OAuth
from twapiconfig import TwApiConfig
web.config.debug = True

#tempaltes engine
#render = web.template.render('templates/',base='default_layout')
#render = web.template.render('templates/')
render = web.template.render('templates/')

path_prefix = '/mtp'
urls = (
        '/', 'reindex',
        '/t', 'tproxy',
        '/ti/(.*)','tproxyinterface',
        #prefix
        path_prefix,'reindex',
        path_prefix+'/', 'reindex',
        path_prefix+'/t','tproxy',
        path_prefix+'/ti/(.*)','tproxyinterface',
        '/(.*)', 'index',
)
apiConfig = TwApiConfig()
twitter_CONSUMER_KEY= apiConfig.CONSUMER_KEY
twitter_CONSUMER_SECRET=apiConfig.CONSUMER_SECRET
twitter_OAuthToken = apiConfig.OAuthToken
twitter_OAuthTokenKey = apiConfig.OAuthTokenKey
#json interface
class tproxyinterface:
    def GET(self,path):
        #web.header('Content-Type', 'application/json')
        #if (path[]'friends.list.html')
        #return "{\"firstName\": \"John\",\"lastName\": \"Smith\",\"path\":\"" + path.find('friends.list.html') +"\"}"
        #return "{\"firstName\": \"John\",\"lastName\": \"Smith\",\"path\":\"" + path +"\"}" 
        mtptwitter = Twitter(auth=OAuth(twitter_OAuthToken,twitter_OAuthTokenKey,twitter_CONSUMER_KEY,twitter_CONSUMER_SECRET),secure=True,api_version='1',domain='api.twitter.com')
        if path.find('friends.list.html')>=0:
            return render.tproxy_friends_list(mtptwitter.statuses.friends_timeline(count=30))
        else:
            #web.header('Content-Type', 'application/json')
            #twitterresult = reversed(mtptwitter.statuses.friends_timeline(count=15))
            return mtptwitter.statuses.friends_timeline(count=1)



class tproxy:
    def GET(self):
        return render.tproxy()

class reindex:
    def GET(self): raise web.seeother('/mtp/index')
    
class index:
    def GET(self, path):
        return render.index()

app = web.application(urls, globals())

##########web customs output region start##########
#customs  not found
#def notfound():
#    return web.notfound("404:Sorry, the page you were looking for was not found.")

    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))
#app.notfound = notfound

#customs internalerror
#def internalerror():
#    return web.internalerror("502:Bad Request.")

#app.internalerror = internalerror
##########web customs output region end##########

application = app.wsgifunc()